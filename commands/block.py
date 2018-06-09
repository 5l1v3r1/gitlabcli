import requests, sys, os
from prettytable import PrettyTable

def block(api_url, user, token, user_id):
    headers = {"Private-Token": "%s" % token}
    login = requests.post(api_url + 'users/' + user_id + '/block', headers=headers)

    if login.status_code == 201:
        print('\033[32m[OK]\033[0m blocked %s' % user_id)
    else:
        print('\033[31m[%s]\033[0m Cannot block user' % login.status_code)

def unblock(api_url, user, token, user_id):
    headers = {"Private-Token": "%s" % token}
    login = requests.post(api_url + 'users/' + user_id + '/unblock', headers=headers)

    if login.status_code == 201:
        print('\033[32m[OK]\033[0m unblocked %s' % user_id)
    else:
        print('\033[31m[%s]\033[0m Cannot unblock' % login.status_code)

def blocks(api_url, user, token):
    headers = {"Accept": "application/vnd.github.giant-sentry-fist-preview+json"}
    login = requests.get(api_url + 'user/blocks', auth=(user,token), headers=headers)

    data = login.json()
    c = 0

    header = "Username".ljust(25), "Profile".ljust(35), "Site Admin"
    print('\033[34m{0[0]} {0[1]} {0[2]}\033[0m'.format(header))

    table = PrettyTable(['Username', 'Profile', 'Site Admin']) # Header
    table.align = "l" # Text Align left

    for i in range(len(data)):
        result = data[i]["login"], data[i]["html_url"], data[i]["site_admin"]
        table.add_row([result[0], result[1], result[2]])
        c+=1

    print(table)
    print('\033[32mFound %i blocked users\033[0m' % int(c))
