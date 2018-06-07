import requests, json

def edit_repo(api_url, user, token, item, value, repo):
    payload = {"name": repo, item: value}
    login = requests.post(api_url + 'repos/' + user + '/' + repo, auth=(user,token), data=json.dumps(payload))

    if login.status_code == 200:
        print('\033[32m[OK]\033[0m Repo edited')
    else:
        print('\033[31m[%s]\033[0m Cannot edit repo' % login.status_code)
