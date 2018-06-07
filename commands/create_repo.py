import requests, json, sys, os

def create_repo(api_url, user, token, repo):
    headers = {"Private-Token": "%s" % token}
    payload = {'name': '%s' % repo, 'description': 'Created with Gitlab API', 'visibility': 'public'}
    login = requests.post(api_url + 'projects', headers=headers, data=payload)

    if login.status_code == 201:
        print('\033[32m[OK]\033[0m Project created')
    else:
        print('\033[31m[%s]\033[0m Cannot create project')
