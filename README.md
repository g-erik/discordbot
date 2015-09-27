# discordbot
A modular bot for the free voice/text messaging software Discord, written for Python 3.

# Dependencies
To run discordbot you need the following packages for Python 3:

* discord.py - API for Discord ([info for contributors](https://github.com/Rapptz/discord.py))
  * `pip install discord.py`
* praw - API for the Reddit module
  * `pip install praw`
* urbandict - API for the Urban Dictionary module
  * `pip install urbandict`
* wolframalpha - API for the Wolfram Alpha moudle
  * `pip install wolframalpha`

# Usage
Start the bot via `python3 discordbot.py`.

On startup you will be asked for the Discord login credentials as well as for your Wolfram Alpha API Key. You can also specify these details if you create a file called `.login` in the discordbot folder with the following content:
```
mail mailadress@domain.com
pw yourpassword
waapi yourwolframalphaapikey
```
Some commands are restricted for the common user. You can add the Discord IDs of the users that are authorized to do administrative tasks in a file called `.auth` so that they can execute said commands.

# To do list
* Clean code and add comments
* Isolate the modules so that they can be enabled or disabled dynamically
* Add additional modules
* Improve stability (recover from connection problems)
