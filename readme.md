![version](https://img.shields.io/badge/version-3.0.3-orange.svg)

![MIT](https://img.shields.io/github/license/DrLarck/discordballz)
[![discordguild](https://discordapp.com/api/guilds/531560539638202368/widget.png)](https://discord.gg/gwpJgtS)

# Discord Ball Z

Hello and welcome to the official **Discord Ball Z** repository.

## Technical informations :

Here are some technical informations about the project :

- Language : `english`
- Programming language : ![python3](https://img.shields.io/badge/python-3.7-yellow.svg)
- Libraries : ![discord.py](https://img.shields.io/badge/discord-py-blue.svg)
- Database : ![postgresql](https://img.shields.io/badge/postgre-sql-blue.svg?logo=postgresql)

## How to make it work ?

**Discord Ball Z** doesn't support the older versions of **Python** such as **Python 2**. You shouldn't have any problem using **Python 3**.

First of all, to run **Discord Ball Z** you have to create a **Discord Application** [here](https://discordapp.com/developers/applications/).

Once you have created a **Bot** on the **Discord** web-app, get the **Token** of your app and replace the `token` variable in `configuration > bot.py > token`.

*Note : We highly recommend you to use `os.environ['key']` to store your `token`.*

Then, you'll need to **configure** your **database**.

**Discord Ball Z** uses **PostgreSQL** by default, you can get **PostgreSQL** [here](https://www.postgresql.org/download/).

Once you have installed **PostgreSQL**, configure as following :

1. Go to `programs > PostgreSQL > 12 > data` then open `postgresql.conf` and edit those lines as following :

```bash
listen_addresses = '*'
port = 5432
```

2. Go back to `data` folder, and edit the `pg_hba.conf` by replacing the lines by this :

```bash
host    replication     all             0.0.0.0/0            md5
host    replication     all             ::0/0                
```

3. Once you've done, it open your **terminal** and type the following commands to create a database and start working with it :

```bash
$psql -U postgres
# enter the default password
$CREATE USER user_name WITH PASSWORD 'user_password';
$CREATE DATABASE database_name;
$GRANT ALL PRIVILEGES ON DATABASE database_name TO user_name;

# then test 
$psql -d database_name -U user_name
```

## Run the bot

Once you've configured everything, open your **terminal** and type :

```bash
$python3 -B main.py
```

*Last update : 11/02/20 - 17:22 France by **DrLarck***