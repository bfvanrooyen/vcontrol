from abc import ABCMeta, abstractmethod

class BaseCommand(metaclass=ABCMeta):
    @abstractmethod
    def parse_arguments(self, subparsers):
        return
    @abstractmethod
    def handle_command(self, args):
        return
