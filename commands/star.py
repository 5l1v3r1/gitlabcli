import requests

def star(api_url, user, token, id):
    headers = {"Private-Token": "%s" % token}
    login = requests.post(api_url + 'projects/' + id + '/star', headers=headers)

    if login.status_code == 201:
        print('\033[32m[OK]\033[0m You starred %s' % id)
    else:
        print('\033[31m[%i]\033[0m Failed to star project' % login.status_code)

def unstar(api_url, user, token, id):
    headers = {"Private-Token": "%s" % token}
    login = requests.post(api_url + 'projects/' + id + '/unstar', headers=headers)

    if login.status_code == 201:
        print('\033[32m[OK]\033[0m Removed star from %s' % id)
    else:
        print('\033[31m[%i]\033[0m Failed to unstar project' % login.status_code)
