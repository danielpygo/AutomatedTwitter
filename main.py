import tweepy
import json
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

    api = tweepy.API(auth, wait_on_rate_limit = True)
    for User in search_for_users(api,'python')[:5]:
        print()
        print("**************")
        print(json.dumps(User._json, indent =4 ))
        print("**************")
        print()

    # f = open('to_tweet.txt', 'r+')
    # d = f.readlines()
    # f.seek(0)
    # for tweet in d:
    #     api.update_status(tweet)
    #     if tweet.rstrip() != "remove this line":
    #         f.write(tweet)
    # f.truncate()
    # f.close()

    # api.lookup_users(user_ids=None, screen_names=None, include_entities=None)


if __name__ == '__main__':
    main()
