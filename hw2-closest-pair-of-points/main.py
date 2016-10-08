import sys
print(sys.version)
from cli import cli
from factory import Factory

def main():
    fac = Factory(cli.parse())
    if cli.test:
        fac.test()
    elif cli.compare:
        fac.compare()
    else:
        fac.solve()


if __name__ == "__main__":
    main()
