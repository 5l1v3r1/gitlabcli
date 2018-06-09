import requests

def create_user(api_url, user, token, email, password, username, name):
    headers = {"Private-Token": "%s" % token}
    payload = {'email': '%s' % email, 'password': '%s' % password, 'username': '%s' % username, 'name': '%s' % name}
    login = requests.post(api_url + 'users', headers=headers, data=payload)

    if login.status_code == 201:
        print('\033[32m[OK]\033[0m User created: %s' % username)
    else:
        print('\033[31m[%s]\033[0m Cannot create user' % login.status_code)

def delete_user(api_url, user, token, user_id):
    headers = {"Private-Token": "%s" % token}
    login = requests.delete(api_url + 'users/' + user_id, headers=headers)

    if login.status_code == 204:
        print('\033[32m[OK]\033[0m User deleted: %s' % user_id)
    else:
        print('\033[31m[%s]\033[0m Cannot delete user' % login.status_code)
