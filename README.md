# About
This project started as a funny way to connect with friends in 2020, and it barely evolved a bit.

It's a really simple bot for Telegram, to help play DnD remotely and have a really simple chatbot with some funny and internal jokes.

Uploaded as a pet project to explore some IA and Telegram API integrations, aside from some internal group jokes.

## Commands
`Note: All commands, prompt and content is in spanish, in case of wanting it in other language, you'd have to change all the texts`
- Roll any combination of d&d available dices (d2, d4, d6, d8, d10, d12, d20, d100).
- Get advise from Radwolf (Gemini's `gemini-pro` model with a prompt to be a Wolf therapist).
- Rock and stone!
- Bless a dice roll with 1d4.
- Multiple other text commands.

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
