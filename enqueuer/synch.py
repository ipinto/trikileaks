#!/usr/bin/python
# -*- coding: utf-8 -*-

import db_manager
import settings
import twitter_client


def clean_tweet(status):
    return {
        'id': status.id_str,
        'user': status.user.screen_name.encode('utf-8', 'ignore'),
        'date_created': status.created_at.encode('utf-8', 'ignore'),
        'text': status.text.encode('utf-8', 'ignore')
    }


if __name__ == "__main__":
    tweets = twitter_client.get_last_tweets(settings.TRIKIMAILU_HASHTAG)
    tweets = filter(lambda x: x.retweeted_status is None, tweets)

    for tweet in tweets: db_manager.save(clean_tweet(tweet))
