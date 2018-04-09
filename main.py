import tweepy
import json
import time
import random
def setup():
    """
    my auth.txt looks like:
        CONSUMER_KEY = #
        CONSUMER_SECRET = #
        ACCESS_TOKEN = #
        ACCESS_TOKEN_SECRET = #
    """
    creds = {}
    f =  open('auth.txt', 'r')
    setup = f.readlines()
    for line in setup:
        args = [ s.lstrip(' ').rstrip() for s in line.split("=")]
        creds[args[0]] = args[1] #get rid of \n at end
    print(creds)
    f.close()
    return creds
def search_for_users(api, search_term):
    return api.search_users(search_term)
def main():
    creds = setup()
    CONSUMER_KEY = creds['CONSUMER_KEY']
    CONSUMER_SECRET = creds['CONSUMER_SECRET']
    ACCESS_TOKEN = creds['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = creds['ACCESS_TOKEN_SECRET']

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    while True:
        try:
            api = tweepy.API(auth, wait_on_rate_limit = True)
            user_searches = ['python', 'UT Austin', 'UT2019', 'Computer Science',
            'pythonic']
            for search in user_searches:
                for user in search_for_users(api,search):
                    if user.followers_count < 300:
                        user.follow()

            for follower in tweepy.Cursor(api.followers).items():
                follower.follow()

            searches = [
                'UT Austin',
                'Computer Science',
                'Javascript',
                'Rust programming',
                'Dropbox',
                'Amazon',
                'MIT',
                'Microsoft',
                'LSTM',
                'SGD',
                'Machine Learning',
                'Deep Learning',
                'Pythonic',
                'Golang',
                'UT2019',
                'Google Deep Mind',
                'Data Science'
            ]
            numberOfTweets = "Number of tweets you wish to interact with"
            for search in searches:
                for tweet in tweepy.Cursor(api.search, search).items(50):
                    if tweet.user.followers_count < 180:
                        tweet.user.follow()
                    try:
                        tweet.favorite()
                        print('Favorited the tweet')
                    except StopIteration:
                        break
            f = open('to_tweet.txt', 'r+')
            d = f.readlines()
            f.seek(0)
            if not d:
                continue
            if random.random() < .05:
                api.update_status(d[0])
                d.pop(0)
            for tweet in d:
                f.write(tweet)
            f.truncate()
            f.close()
            time.sleep(5 * 60)
        except tweepy.TweepError as e:
            print('Hit limit' + str(e))
            time.sleep(15 * 60)
        except tweepy.RateLimitError:
            print('Hit the rate limit')
            time.sleep(15 * 60)
        except Exception as e:
            print('Unhandled Exception? ' + str(e))
            time.sleep(15 * 60)

    # api.lookup_users(user_ids=None, screen_names=None, include_entities=None)


if __name__ == '__main__':
    main()
