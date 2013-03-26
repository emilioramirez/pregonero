# -*- coding: utf-8 -*-
import random
import logging.config
from time import sleep
from datetime import datetime
from query_json import Query
import publish


class TwitterBot():

    def __init__(self, name="", priority=None, tag='', tweets_day=4,
            log_file_name="pregonero.log", simulate=False):
        """
        Initialize bot
        param:
            priority: int for filter messages of this priority
            tag: string for filter messages of this tag
            tweets_day: int for amount of tweet per day
            log_file_name: string for file name of log
            enable_tweet: boolean, if True publish messages on twitter
        """
        self.name = " ".join([__name__, name])
        self.priority = priority
        self.tag = tag
        self.tweets_day = tweets_day
        self.simulate = simulate
        self.init_logging(log_file_name)
        try:
            self.messages = Query()
        except IOError:
            self.logger.exception("File 'messages.json' is missing.")
            raise
        except:
            self.logger.exception("Problem with 'messages.json' file.")
            raise
        self.logger.info("Bot init successful")

    def filter(self):
        """
        Return a list of messages with candidate tweets
        """
        if(self.priority and self.tag):
            # Return messages with priority and tag
            self.logger.info("Get messages for priority: {} and tag: {}".format(
                self.priority, self.tag)
            )
            return self.messages.get_by_tag_priority(
                self.priority, self.tag)
        elif(self.priority or self.tag):
            if(self.priority):
                # Return only messages with priority
                self.logger.info("Get messages for priority: {}".format(
                    self.priority)
                )
                return self.messages.get_by_priority(self.priority)
            if (self.tag):
                # Return only messages with tag
                self.logger.info("Get messages for tag: {}".format(
                    self.tag)
                )
                return self.messages.get_by_tag(self.tag)
        else:
            # Return all messages
            self.logger.info("Get all messages")
            return self.messages.get_all()

    def daily_tweets(self):
        """
        Tweet a 'tweets_day' amount of tweet daily, sleep a random time. Must
        be called once time daily.
        """
        self.logger.info("Start daily tweets")
        # Loads messages into self.messages
        # Filter messages
        tweets = self.filter()
        # Publish tweets_day number of twits per day
        cicles = range(self.tweets_day)
        cicles.reverse()
        for i in cicles:
            try:
                # choose a random message
                tweet = random.choice(tweets)
            except IndexError:
                # No more tweets
                break
            # Publish on twitter
            publish.on_twitter(tweet['text'], self.logger, self.simulate)
            # Drop the message of the list
            tweets.pop(tweets.index(tweet))
            # Sleep a random time (in seconds) between 60 and
            # (remaining_time / remaining_tweets)
            # to tweet again
            remaining_time = self.calculate_delta_time().seconds
            remaining_tweets = float(i + 1)
            seconds = round(random.uniform(60,
                remaining_time / remaining_tweets))
            self.logger.info("Sleep to next tweet: " + str(seconds) +
                " seconds")
            sleep(seconds)
        self.logger.info("Stop daily tweets")

    def calculate_delta_time(self):
        """
        Returns the remaining time till it be morrow
        """
        current_date = datetime.now()
        tomorrow_date = datetime(current_date.year,
                                 current_date.month,
                                 current_date.day + 1)
        return tomorrow_date - current_date

    def init_logging(self, file_name):
        """
        Enable logging
        This initializate config must be in another place
        """
        dictLogConfig = {
            "version": 1,
            "handlers": {
                        "fileHandler": {
                            "class": "logging.handlers.RotatingFileHandler",
                            "formatter": "default",
                            "filename": file_name,
                            "maxBytes": 10240,
                            "backupCount": 3
                        },
                        "console": {
                            "class": "logging.StreamHandler",
                            "formatter": "default",
                            "stream": "ext://sys.stdout"
                        }
            },
            "formatters": {
                "default": {
                    "format": ("%(asctime)s - %(name)s - %(levelname)s - " +
                               " %(message)s")
                }
            },
            "loggers": {
                self.name: {
                    "handlers": ["fileHandler", "console"],
                    "level": "DEBUG",
                }
            }
        }
        logging.config.dictConfig(dictLogConfig)
        self.logger = logging.getLogger(self.name)

    def run(self):
        """
        Main function of the bot, run it indefinitely, daily tweet
        """
        self.logger.info("Start Running")
        # This must be change in future version by something like
        # "run from_date to_date" and not while true
        while(True):
            self.daily_tweets()
            # Sleep until tomorrow
            delta = self.calculate_delta_time()
            self.logger.info("Sleep remaining day time: " +
                str(delta.seconds) + " seconds")
            sleep(delta.seconds)
        self.logger.info("Stop Running")