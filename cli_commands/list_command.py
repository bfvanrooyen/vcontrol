import argparse
from subprocess import call
import command_base

class ListCommand(BaseCommand):
  def parse_arguments(subparsers):
      list_parser = subparsers.add_parser('list', help='List available Virtual Machines')
      list_parser.set_defaults(func=handle_command)
    
  def handle_command(args):
      call(['vboxmanage', 'list', 'vms'])
