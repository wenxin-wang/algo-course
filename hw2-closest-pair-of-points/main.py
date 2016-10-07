from cli import cli
from factory import Factory

def main():
    fac = Factory(cli.parse())
    print(fac.get_points())
    if cli.interactive:
        fac.plot()


if __name__ == "__main__":
    main()
