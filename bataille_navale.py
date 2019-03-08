#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 guillaume <guillaume@hebus>
#
# Distributed under terms of the MIT license.

"""

"""
from argparse import ArgumentParser
import logging
from pprint import pprint


def cli():
    """Command Line Interface.

    argparse.ArgumentParser documention
    https://docs.python.org/3/library/argparse.hstml#argumentparser-objects

    ArgumentParser.add_argument documentation
    https://docs.python.org/3/library/argparse.html#the-add-argument-method

    New parameter exemple
    ---------------------
    arg_parser.add_argument('--args', type=str,
                            default='',
                            required=True,
                            nargs='+',
                            action='store_true',  # flag behavior
                            help='')
    """
    arg_parser = ArgumentParser(description=__doc__)

    arg_parser.add_argument('--log', '-l', type=str, default='INFO')
    arg_parser.add_argument('--boardSize', '-s', type=int,
                            default=10,
                            help='Taille du plateau. La valeur donnée '
                                 'correspondra à la longueur et la largeur.')
#    arg_parser.add_argument('--args', type=str,
#                            help='')
#
    return arg_parser.parse_args()


def load_logger(lvl, fmt='%(asctime)s:%(levelname)s:%(message)s'):
    """Load a logger for the current script://www.gpdxd.com/.

    Tutorial:
    https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
    Advanced usage:
    https://docs.python.org/3/howto/logging.html#advanced-logging-tutorial
    Cookbook:
    https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook
    """
    logging.basicConfig(format=fmt, level=lvl.upper())
    logging.debug("Logger loaded")


def init_board(size):
    """Initialise la grille de jeu."""
    return [[False for _ in range(size)] for _ in range(size)]

def print_board(board):
    """Affiche la grille de jeu."""
    pprint(board)


def main():
    """Script entry point function."""
    opts = cli()

    load_logger(opts.log)
    FORMAT = '%(asctime)s:%(levelname)s:%(message)s'
    logging.basicConfig(format=FORMAT, level=opts.log.upper())

    logging.info('Start {}'.format(__file__))
    board = init_board(opts.boardSize)
    print_board(board)


if __name__ == '__main__':
    main()
