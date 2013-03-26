# -*- coding: utf-8 -*-
import twitter


try:
    import twitter_app_settings
except ImportError:
    # Must be a logging report
    print("twitter_app_settings.py file missing")
    raise
else:
    API = twitter.Api(
                consumer_key=twitter_app_settings.CONSUMER_KEY,
                consumer_secret=twitter_app_settings.CONSUMER_SECRET,
                access_token_key=twitter_app_settings.ACCESS_TOKEN_KEY,
                access_token_secret=twitter_app_settings.ACCESS_TOKEN_SECRET
            )


def on_twitter(twit, bot_logger, simulate):
    """
    Publish a message on twitter
    param:
        twit: string
        run_test: if True, publish on twitter. If False, only log the output,
                  but DO NOT update twitter account(for test purpose)
    """
    if(not simulate):
        status = API.PostUpdate(twit)
    bot_logger.info("PostUpdate: {}".format(twit))
