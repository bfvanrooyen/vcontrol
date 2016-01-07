from subprocess import call
from cli_commands.command_base import BaseCommand

class ListCommand(BaseCommand):
  def parse_arguments(self, subparsers):
      list_parser = subparsers.add_parser('list', help='List available Virtual Machines')
      list_parser.set_defaults(func=self.handle_command)
    
  def handle_command(self, args):
      call(['vboxmanage', 'list', 'vms'])
