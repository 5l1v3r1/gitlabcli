#!/usr/bin/python
# This is most likely the stupidest thing I have ever coded.

import requests

def delete_all(api_url, user, token):
    headers = {"Private-Token": "%s" % token}
    login = requests.get(api_url + 'users/' + user + '/projects', headers=headers)

    repos = login.json()
    c = 0

    for i in range(len(repos)):
        repo = repos[i]["id"]
        delete = requests.delete(api_url + 'projects/' + id, headers=headers)
        c+=1
        print('\033[31mDeleted %s [%i/%i]\033[0m' % (repo, int(c), len(repos)))
