# -*- coding: utf-8 -*-
# Created by wushuyi on 2016/9/20 0020.
import requests
import os

ENDPOINT = 'https://api.cdnjs.com/libraries'
CDN = 'https://cdnjs.cloudflare.com/ajax/libs'
CHUNK_SIZE = 1024


def api(data):
    response = requests.get(ENDPOINT, params=data)
    if response.ok:
        res = response.json()['results']
        return res
    else:
        raise Exception('Unable to fetch results.')


def search(text, fields=None):
    data = {'search': text}
    if fields is not None:
        if isinstance(fields, list):
            fields = ','.join(fields)
        data['fields'] = fields
    return api(data)


def grab(name):
    response = requests.get('{}/{}'.format(ENDPOINT, name))
    if response.ok:
        res = response.json()
        return res
    else:
        raise Exception('Unable to fetch results.')


def asset_url(pkg, version, file):
    return '/'.join([CDN, pkg, version, file])


def mkdirs(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)


def get_file(pkg, version, files):
    package_name = pkg
    if not os.path.exists(package_name):
        os.mkdir(package_name)
    os.chdir(package_name)
    if not os.path.exists(version):
        os.mkdir(version)
    os.chdir(version)

    print('Installing {0} version {1}...'.format(package_name, version))
    print()
    for asset in files:
        url = asset_url(package_name, version, asset)
        dirname = os.path.dirname(asset)
        if dirname:
            mkdirs(dirname)
        path = os.path.join(os.getcwd(), asset)
        short_name = path.split('powser_components')[-1]
        print('Downloading', short_name, '... ', end='')

        with open(asset, 'wb') as f:
            response = requests.get(url, stream=True)
            if not response.ok:
                print('Failed!')
                return -1
            for chunk in response.iter_content(CHUNK_SIZE):
                f.write(chunk)
            print('Done.')

    print()
    print('Successfully installed.')
