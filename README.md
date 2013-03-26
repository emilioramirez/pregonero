Pregonero v.0.1
===============

Bot written in python to inform periodically stuff in twitter. Useful for anounce events, conference, meetings, schedules, automatically.

THIS PROJECT MUST NOT BE USE FOR SPAM PURPOSE.

Feature:

* Make 'x' tweets daily (randomly) of a priority and/or tag.

Initial config
--------------

###Virtualenv

Create a [virtualenv](http://www.virtualenv.org/en/latest/) and install the requirements

    (virtualenv)$ pip install -r requirements.pip

###Twitter app settings

You will need to log in with the bot's account and register a new app to make a bot. From this site, change the app's Application Type to "Read, Write, and Access direct messages". Then after that, click the "Update this Twitter Application's settings" button to get the four following pieces of info:

* Consumer key
* Consumer secret
* Access token
* Access token secret

These four pieces of info (and not the account's username/password) are used to log in with the Python API and perform actions.

Then complete 'twitter_app_settings.py.template' file with the above information and rename it to 'twitter_app_settings.py'


Messages
--------

The messages must be in a json file with this structure (see messages.json for an example or modify the file):

    [
        {
            "text": "Test Messaje 1",
            "priority": 1,
            "tags": ["tag1"]
        },
        {
            "text": "Test 000 Messaje 2",
            "priority": 5,
            "tags": ["tag2"]
        }
    ]

Run Pregonero
-------------

Run the 'example_bot_1.py':

    (virtualenv)$ python example_bot_1.py

###Create and/or personalize more bots

To create another instance of pregonero (see example_bot_1.py). You can create and run a example_bot_2.py with:

    import bot

    bot = bot.TwitterBot(name="Monty", # a verbose name for identify 2 or more instances in logs (default '')
                         priority=1, # filter all message of priority 1 (default None)
                         tag='tag2', # filter all message of tag tag2 (default '')
                         tweets_day=5, # make 5 twits per day (default 4)
                         simulate=True, # dont twit on the twitter account, only simulate (default False)
                         )
    bot.run()

TODO
----

A lot of stuff, this version is experimental but works ;)

* Better querys
* Tweet between to dates (from_date, to_date)
* Every message have an expiration date or a enable date
* Make a request for info to the bot
* Make a facebook udpate?