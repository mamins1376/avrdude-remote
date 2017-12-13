#!/usr/bin/env python3

from sys import exit, argv as args
from xmlrpc.client import ServerProxy, Binary


class RPCHandle(object):
    def __init__(self, address):
        address = "http://%s" % address
        self.server = ServerProxy(address, allow_none=True)

    def send(self, filename):
        with open(filename, 'rb') as f:
            content = f.read()
        return self.server.create_file(filename, Binary(content))

    def delete(self, filename):
        return self.server.delete_file(filename)

    def call(self, command):
        return self.server.call(command)


def main():
    address = args[1]

    # extract files to be sent
    files = filter(lambda arg: arg.count(":") in (2, 3), args)
    files = map(lambda arg: arg.split(":")[2], files)

    rpc = RPCHandle(address)

    for file in files:
        rpc.send(file)

    (retcode, stdout) = rpc.call(args[2:])
    print(stdout)
    exit(retcode)


if __name__ == "__main__":
    try:
        main()
    except ConnectionRefusedError:
        print("Connection refused")
