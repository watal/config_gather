# -*- coding:utf-8 -*-

import multiprocessing as mp
import subprocess
import sys
import os

import yaml

HOST_PATH = 'hosts.yml'


# def config_gather():
#     '''  '''
# モジュールを呼び出して並列実行するようにする

def main():
    # ホスト一覧取得
    if os.path.exists(HOST_PATH):
        with open(HOST_PATH, 'r') as f:
            try:
                host = yaml.load(f, Loader=yaml.FullLoader)
            except ValueError:
                sys.stderr.write('Failed to load host file')
                sys.exit(-1)
    else:
        sys.stderr.write('Failed to load host file')
        sys.exit(-1)

    for i, j in host['host'].items():
        subprocess.check_call('sh modules/{}.sh "{}" "{}" "{}" "{}"'.format(
            j['vender'], i, j['address'], j['id'], j['password']), shell=True)


if __name__ == '__main__':
    main()
