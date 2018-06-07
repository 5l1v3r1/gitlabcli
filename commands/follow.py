import requests, sys, os

def follow(api_url, user, token, username):
    login = requests.put(api_url + 'user/following/' + username, auth=(user,token))

    if login.status_code == 204:
        print('\033[32m[OK]\033[0m Now following %s' % username)
    else:
        print('\033[31m[%s]\033[0m Cannot follow user' % login.status_code)

def unfollow(api_url, user, token, username):
    login = requests.delete(api_url + 'user/following/' + username, auth=(user,token))

    if login.status_code == 204:
        print('\033[32m[OK]\033[0m Unfollowed %s' % username)
    else:
        print('\033[31m[%s]\033[0m Cannot unfollow' % login.status_code)
