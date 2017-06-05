import settings
import twitter
import urllib


def get_last_tweets(hashtag):
    api = twitter.Api(consumer_key=settings.TW_CONSUMER_KEY,
                      consumer_secret=settings.TW_CONSUMER_SECRET,
                      access_token_key=settings.TW_ACCESS_TOKEN_KEY,
                      access_token_secret=settings.TW_ACCESS_TOKEN_SECRET)

    params = {
        'q': hashtag,
        'result_type': 'recent',
        'count': settings.NUMBER_OF_RESULTS
    }
    return api.GetSearch(raw_query=urllib.urlencode(params))
