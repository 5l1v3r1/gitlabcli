import requests, os, sys

def clone_all(api_url, user, token, username):
    headers = {"Private-Token": "%s" % token}
    login = requests.get(api_url + 'users/' + username + '/projects', headers=headers)

    repos = []
    c = 1

    for repo in login.json():
        repos.append(repo["http_url_to_repo"])


    for url in repos:
        git = url.split('/')[-1]
        if os.path.isdir(('./repos/%s/%s' % (username, git))):
            pass
        else:
            os.makedirs('./repos/%s/%s' % (username, git))

    for url in repos:
        git = url.split('/')[-1]
        print('\033[32mDownloading [%i/%i]\033[0m' % (int(c), len(repos)))
        os.system('git clone %s ./repos/%s/%s' % (url, username, git))
        c+=1
