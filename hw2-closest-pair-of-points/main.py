from cli import cli
from factory import Factory

def main():
    fac = Factory(cli.parse())
    if cli.test:
        print(fac.test(cli.test))
    else:
        fac.solve()


if __name__ == "__main__":
    main()
