import argparse
from exceptions import ArgumentError


class Cli:
    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Find out the closest pair of points')
        parser.add_argument(
            "-i",
            "--interactive",
            help=(
                "plot the points in the end. "
                "if -f or -g is not specified, let user input data from gui"),
            action="store_true")
        parser.add_argument(
            "-r",
            "--read",
            metavar="file",
            type=str,
            nargs=1,
            help="read points from file, conflict with -g")
        parser.add_argument(
            "-g",
            "--generate",
            metavar="N",
            type=int,
            nargs=1,
            help="generate N points, must also specify -w, conflict with -r")
        parser.add_argument(
            "-w",
            "--write",
            metavar="write",
            type=str,
            nargs=1,
            help="write points to file, useful with -g")
        self.parser = parser
        self.interactive = None
        self.read = None
        self.generate = None
        self.write = None

    def parse(self):
        args = self.parser.parse_args()
        self.__set(args, "interactive")
        self.__set0(args, "read")
        self.__set0(args, "generate")
        self.__set0(args, "write")
        if not self.read and not self.generate and not self.interactive:
            self.interactive = True
        if self.read and self.generate:
            self.parser.print_help()
            raise ArgumentError("-r and -g conflicts")
        if self.generate and not self.write:
            self.parser.print_help()
            raise ArgumentError("-w is also needed when -g is specified")
        return self

    def __set0(self, args, name):
        attr = getattr(args, name)
        if attr:
            setattr(self, name, attr[0])

    def __set(self, args, name):
        attr = getattr(args, name)
        setattr(self, name, attr)

    def __str__(self):
        return "interactive=%s, read=%s, write=%s, generate=%s" % (
            self.interactive, self.read, self.write, self.generate)


cli = Cli()
