import argparse

from subprocess import call

def parse_arguments():
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    parser.add_argument("ls", action="store_true", help="List available Virtual Machines")
    args = parser.parse_args()

    if args.ls:
       call(["vboxmanage", "list", "vms"]) 
