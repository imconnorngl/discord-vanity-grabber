# Discord Vanity Grabber

> Simple Python script for grabbing vanity URLs on Discord. Given a vanity, guild and Discord user token, the script will attempt to claim the vanity for the given guild as soon as it becomes available.

---

## Getting Started

The following instructions will get you up and running with the Discord Vanity Grabber.

---

## Dependencies

1. [Python (3.8+)](https://www.python.org/)

---

## Setup:

_The following steps should be under the pretence that the prerequistes are installed and are functioning correctly._

First step in the process is the clone the repository:

```sh
$ git clone https://github.com/imconnorngl/discord-vanity-grabber.git
$ cd discord-vanity-grabber
```

Next, you need to fill in the following variables within the script's `config.py` file:

```py
# Discord User Token
# This can be found by pressing Ctrl+Shift+I in Discord, Application > Local Storage > Token.
# This token must have admin privileges in the guild you want to change the vanity of.
TOKEN = ""

# Discord Vanity
# This is the vanity you want to change to.
VANITY = ""

# Discord Guild ID
# This is the ID of the guild you want to change the vanity of.
GUILD_ID = ""
```

That's about it! You're now ready to run the script. To do so, run the following command:

```sh
$ python main.py
```

You should then see the following output:
```sh
Starting checker...
Checking...
Vanity is not available, waiting...
```

The script will then continue to check the availability of the vanity every 10 seconds. Once the vanity becomes available, the script will claim it and exit with the following output:
```sh
Vanity is available, changing...
```
