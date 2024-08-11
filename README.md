# About
This project started as a funny way to connect with friends in 2020, and it barely evolved a bit.
It's a really simple bot for Telegram, to help play DnD remotely and have a really simple chatbot with some funny and internal jokes.
Uploaded as a pet project to explore some API integrations, and some internal group jokes.

# Setup 
## Using docker-compose

1. Modify the apikeys in the `docker-compose.yml` file.
2. Run `docker compose up`.
3. Enter the database container and create the tables and files in `db/sql_creation.sql`.
4. Run!

## Using Python3
Create a virtual environment and install everything listed on `requirements.txt`
```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

# TODO:
- [X] Code refactor
- [X] Add logs
- [X] Cap maximum number of dice rolled
- [ ] Add tests
- [X] Docker/Docker compose for setup
- [X] GPT or so integration (for Radwolf)
- [ ] Add a /cast command?
- [ ] Add /djrad command (Puts a random song from spotify)
- [X] Rock And Stone
