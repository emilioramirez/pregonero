# -*- coding: utf-8 -*-
import bot


bot = bot.TwitterBot(name="Monty",
                     priority=None,
                     tag='',
                     tweets_day=4,
                     simulate=False,
                     log_file_name="pregonero.log")
bot.run()
