import requests

def add_email(api_url, user, token, user_id, email):
    headers = {"Private-Token": "%s" % token}
    payload = {'email': '%s' % email}
    login = requests.post(api_url + 'users/' + user_id + '/emails', headers=headers, data=payload)

    if login.status_code == 201:
        print('\033[32m[OK]\033[0m Email added for user id: %s' % user_id)
    else:
        print('\033[31m[%s]\033[0m Cannot add email' % login.status_code)
