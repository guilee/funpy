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


class GameBoard(object):
    """Plateau de jeu."""

    def __init__(self, size):
        self._size = size
        self._board = None

    def initialize(self):
        """Initialise la grille de jeu."""
        self._board =  [[False for _ in range(self._size)]
                        for _ in range(self._size)]

    def _cell_rendering(self, cell_size, cell_value, h_border_char='-',
            v_border_char='|', cell_content_char={True: [['X']], False: [[' ']]}):
        """Calcule le rendu d'une cellule.
        
        Cela comporte le cadre et le contenu (le cas échéant) de la cellule.
        """
        cell_render = []
        total_cell_size = cell_size + 1
        h_cell_border_tmpl = ('{:'+ h_border_char + '^' +
                              '{}'.format(total_cell_size) + '}')
        h_cell_border = h_cell_border_tmpl.format('')

        cell_render.append(h_cell_border)

        for i in range(cell_size):
            line = v_border_char
            for j in range(cell_size):
                logging.debug("cell content rendering[%s]: i=%s j=%s val='%s'",
                              cell_value, i, j,
                              cell_content_char[cell_value][i][j])
                line += cell_content_char[cell_value][i][j]
            cell_render.append(line)

        logging.debug('Cell render: %s', cell_render)

        return cell_render

    def _board_rendering(self, cell_size):
        """Calcule le rendu du plateau de jeu."""
        board_render = []

        for row in self._board:
            row_render = []
            for cell_value in row:
                row_render.extend(self._cell_rendering(cell_size, cell_value))
            board_render.append(row_render) 

        logging.debug('Board render: %s', board_render)

        return board_render

    def print_board(self, cell_size=1):
        """Affiche la grille de jeu."""
        p_size = (self._size + 1) + (self._size * cell_size)

        header = ' {}'.format(' '.join([str(i)
                                        for i in range(1, self._size+1)]))

        print(header)
        board_render = self._board_rendering(cell_size)

        top_line = [row[0] for row in board_render]
        top_line.append(top_line[0][0])
        print(''.join(top_line))
        for i in range(1, len(board_render[0])):
            printable_line = [row[i] for row in board_render]
            printable_line.append(printable_line[0][0])
            print(''.join(printable_line))
        print(''.join(top_line))

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
    arg_parser.add_argument('--cellSize', '-c', type=int,
                            default=1,
                            help="Taille d'une cellule à l'affichage.")
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


def main():
    """Script entry point function."""
    opts = cli()

    load_logger(opts.log)
    FORMAT = '%(asctime)s:%(levelname)s:%(message)s'
    logging.basicConfig(format=FORMAT, level=opts.log.upper())

    logging.info('Start {}'.format(__file__))
    board = GameBoard(opts.boardSize)
    board.initialize()
    logging.info(board._board)
    board.print_board(cell_size=opts.cellSize)


if __name__ == '__main__':
    main()
