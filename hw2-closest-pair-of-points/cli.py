import argparse
from exceptions import ArgumentError


class Cli:
    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Find out the closest pair of points')
        parser.add_argument(
            "--brutal",
            help="add brutal force solution",
            action="store_true")
        parser.add_argument(
            "--nlogn",
            help="add nlogn solution, this would be the default method",
            action="store_true")
        parser.add_argument(
            "-s",
            "--show",
            help="plot the points in the end",
            action="store_true")
        parser.add_argument(
            "-e",
            "--edit",
            help="edit the points in the gui",
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
            help="generate N points, conflict with -r")
        parser.add_argument(
            "-w",
            "--write",
            metavar="write",
            type=str,
            nargs=1,
            help="write points to file, useful with -g")
        parser.add_argument(
            "-t",
            "--test",
            metavar="T",
            type=int,
            nargs=1,
            help="do N tests, instead of normal run")
        self.parser = parser
        self.brutal = None
        self.nlogn = None
        self.show = None
        self.edit = None
        self.read = None
        self.generate = None
        self.write = None
        self.test = None

    def parse(self):
        args = self.parser.parse_args()
        self.__set(args, "show")
        self.__set(args, "edit")
        self.__set0(args, "read")
        self.__set0(args, "generate")
        self.__set0(args, "write")
        self.__set0(args, "test")
        self.__set(args, "brutal")
        self.__set(args, "nlogn")
        if not self.read and not self.generate and not self.edit:
            self.edit = True
        if self.read and self.generate:
            self.parser.print_help()
            raise ArgumentError("-r and -g conflicts")
        if not self.brutal and not self.nlogn:
            self.nlogn = True
        return self

    def __set0(self, args, name):
        attr = getattr(args, name)
        if attr:
            setattr(self, name, attr[0])

    def __set(self, args, name):
        attr = getattr(args, name)
        setattr(self, name, attr)

    def __str__(self):
        return ("show=%s, edit=%s, read=%s, write=%s, generate=%s, "
                "brutal=%s, nlogn=%s") % (
                    self.show, self.edit, self.read, self.write, self.generate,
                    self.brutal, self.nlogn)


cli = Cli()
