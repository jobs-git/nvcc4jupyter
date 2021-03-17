import argparse


def get_argparser():
    parser = argparse.ArgumentParser(description='NVCCPlugin params')
    parser.add_argument("-t", "--timeit", action='store_true',
                        help='flag to return timeit result instead of stdout')
    return parser


def print_out(out: str):
    # Ensure that we're working with a string
    try:
        out = out.decode()
    except (UnicodeDecodeError, AttributeError):
        pass
    
    for l in out.split('\n'):
        print(l)
