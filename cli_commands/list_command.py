import argparse

from subprocess import call

def parse_arguments():
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    parser.add_argument("list", help="List available Virtual Machines", nargs="?", default="")
    args = parser.parse_args()

    if args.list == "list":
       call(["vboxmanage", "list", "vms"]) 
