# 


## Resources

* <https://www.postgresqltutorial.com/postgresql-indexes/postgresql-full-text-search/>
* https://rasa.com/docs/rasa-pro/concepts/policies/custom-information-retrievers
* https://www.postgresql.org/docs/current/textsearch-controls.html#TEXTSEARCH-RANKING
https://stackoverflow.com/questions/12933805/best-way-to-use-postgresql-full-text-search-ranking

* 



```shell
# This template is for poetry v1.8
poetry --version

# Rasa does not support python versions greater than 3.10; you may need to
# point it to a supported python install
poetry env use /usr/local/bin/python3.10

# install Rasa and dependencies as versioned in the lock file
poetry install

# if necessary, update dependencies (WARNING: this may take a while)
poetry upgrade

# check the Rasa and python versions
poetry run rasa --version

# start developing your bot
poetry run rasa init --template calm --no-prompt
```
