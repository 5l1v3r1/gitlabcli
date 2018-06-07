import requests, sys, os

def delete_repo(api_url, user, token, id):
    headers = {"Private-Token": "%s" % token}
    login = requests.delete(api_url + 'projects/' + id, headers=headers)

    if login.status_code == 202:
        print('\033[32m[OK]\033[0m Project deleted')
    else:
        print('\033[31m[%s]\033[0m Cannot delete project' % login.status_code)
