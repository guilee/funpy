import logging
# import os.path
# import sys


def cli():
    """ Command Line Interface """
    # argparse.ArgumentParser documention
    # https://docs.python.org/3/library/argparse.html#argumentparser-objects
    arg_parser = ArgumentParser(description=__doc__)

    # ArgumentParser.add_argument documentation
    # https://docs.python.org/3/library/argparse.html#the-add-argument-method
    arg_parser.add_argument('--log', '-l', type=str, default='INFO')
    arg_parser.add_argument('--args', type=str,
#                            default='',
#                            required=True,
#                            nargs='+',
#                            action='store_true',  # flag behavior
                            help="")

    return arg_parser.parse_args()


def load_logger(lvl, fmt='%(asctime):%(level)s:%(message)s'):
    """ Load a logger for the current script

        Tutorial:
        https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
        Advanced usage:
        https://docs.python.org/3/howto/logging.html#advanced-logging-tutorial
        Cookbook:
        https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook
    """
    logging.basicConfig(format=fmt, level=opts.log.upper())
    logging.debug("Logger loaded")


def main():
    opts = cli()

    load_logger(opts.log)
    FORMAT = '%(asctime):%(level)s:%(message)s'
    logging.basicConfig(format=FORMAT, level=opts.log.upper())

    logger.info("Start {}".format(__file__))
    print(opts)


if __name__ == '__main__':
    main()
