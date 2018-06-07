import os, sys

def clone(url):
    git = url.split('/')[-1]

    if os.path.isdir(('./repos/%s' % git)):
        os.system('git clone %s ./repos/%s' % (url, git))
    else:
        os.makedirs('./repos/%s' % git)
        os.system('git clone %s ./repos/%s' % (url, git))
