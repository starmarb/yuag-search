"""File to run the server properly through Command Line"""
from sys import argv, exit, stderr
import argparse
from luxapp import app


def main():
    """Command Line Functions. Checks if port is correctly entered"""
    parser = argparse.ArgumentParser(description="The YUAG search application")
    parser.add_argument("port",  help="the port at which the server should listen")
    args = parser.parse_args()
    print(args)
    if len(argv) != 2:
        print('Usage: runserver.py [-h]  port', file=stderr)
        exit(1)

    try:
        port = int(argv[1])
    except Exception:
        print('Port must be an integer.', file=stderr)
        exit(1)

    try:
        app.run(host='0.0.0.0', port=port, debug=True)
    except Exception as ex:
        print(ex, file=stderr)
        exit(1)

if __name__ == '__main__':
    main()
