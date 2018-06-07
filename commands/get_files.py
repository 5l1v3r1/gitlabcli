import requests

def get_files(api_url, user, token, id):
    headers = {"Private-Token": "%s" % token}
    login = requests.get(api_url + 'projects/' + id + '/repository/tree', headers=headers)

    data = login.json()
    header = "Path".ljust(70), "Type".ljust(20)
    print('\033[37m{0[0]} {0[1]}\033[0m'.format(header))

    for i in range(len(data)):
        path = data[i]["path"]
        _type = data[i]["type"]
        print('%s %s' % (path.ljust(70), _type.ljust(20)))

        if _type == 'tree':
            get_dir_files(api_url, user, token, id, path)

# Search all levels
def get_dir_files(api_url, user, token, id, path):
    headers = {"Private-Token": "%s" % token}
    login = requests.get(api_url + 'projects/' + id + '/repository/tree?path=' + path, headers=headers)

    data = login.json()
    for i in range(len(data)):
        path = data[i]["path"]
        _type = data[i]["type"]
        print('%s %s' % (path.ljust(70), _type.ljust(20)))
        if _type == "tree":
            return get_dir_files(api_url, user, token, id, path) # Search all levels
