import argparse

from subprocess import call

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--list", action="store_true", help="List available Virtual Machines")
    args = parser.parse_args()

    if args.list:
       call(["vboxmanage", "list", "vms"]) 
