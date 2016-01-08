from subprocess import call
from cli_commands.command_base import BaseCommand

class StartCommand(BaseCommand):
    def parse_arguments(self, subparsers):
        list_parser = subparsers.add_parser('start', help='Start a Virtual Machine')
        list_parser.add_argument('vm', help='Virtual Machine UUID')
        list_parser.set_defaults(func=self.handle_command)
    
    def handle_command(self, args):
        print(args)
        call(['vboxmanage', 'startvm', args.vm])
