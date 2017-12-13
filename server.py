#!/usr/bin/env python3

from os import remove as remove_file
from os.path import exists as file_exists
from sys import argv as args
from subprocess import PIPE, STDOUT, run as run_command
from xmlrpc.server import SimpleXMLRPCServer as RPCServer
from contextlib import suppress


def create_file(filename, data):
    data = data.data
    with open(filename, "wb") as f:
        f.write(data)

def delete_file(filename):
    if file_exists(filename):
        return remove_file(filename)

def call(command):
    command.insert(0, "avrdude")
    res = run_command(command, stdout=PIPE, stderr=STDOUT)
    return (res.returncode, res.stdout.decode("ascii"))

def main():
    address = args[1].split(":")
    address = (address[0], int(address[1]))

    rpc = RPCServer(address, allow_none=True)
    for f in (create_file, delete_file, call):
        rpc.register_function(f)

    print("Listening on %s:%s" % address)
    with suppress(KeyboardInterrupt):
        rpc.serve_forever()
    print("\nBye!")


if __name__ == "__main__":
    main()
