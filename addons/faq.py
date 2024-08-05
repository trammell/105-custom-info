import logging

from rasa.utils.endpoints import EndpointConfig
from rasa.core.information_retrieval import (
    SearchResultList,
    SearchResult,
    InformationRetrieval,
)
from typing import Any, Dict, List

from psycopg import Connection


logger = logging.getLogger(__name__)


class PostgresIR(InformationRetrieval):
    """
    Custom InformationRetrieval class using postgres fulltext search.
    """

    def connect(self, config: EndpointConfig) -> None:
        """Parameter `pguri` is defined in file `endpoints.yml`."""
        self.conn = Connection.connect(config.kwargs["pguri"])
        logger.info("Got database connection: %s", self.conn)

    async def search(
        self, query: str, tracker_state: Dict[str, Any], threshold: float = 0.0
    ) -> SearchResultList:
        """
        Search the database for relevant results. Order by score.
        """
        sr = []
        logger.info("Search query %s, threshold %s", query, threshold)
        with self.conn.cursor() as cur:
            sql = """
                SELECT title, body, ts_rank_cd(body_search, phraseto_tsquery('english', %s)) AS score
                FROM issues
                WHERE body_search @@ phraseto_tsquery('english', %s)
                ORDER BY score LIMIT 3
            """
            cur.execute(sql, (query, query))
            for title, body, score in cur.fetchall():
                logger.info("Search result: %s, %s, %s", title, body, score)
                sr.append(SearchResult(text=body, score=score, metadata={}))

        return SearchResultList(results=sr, metadata={})
