# -*- coding: utf-8 -*-
from time import sleep
from signal import alarm, signal, SIGALRM
from sys import stdout, exit
import logging


def signal_handler(signum, frame):
    if signum == SIGALRM:
        exit(0)

signal(SIGALRM, signal_handler)


def animation_scroll(s):
    while(True):
        yield s
        s = s[-1] + s[:-1]


def animation_sprites(sprites):
    logging.debug("Set sprites animator generator with {}".format(sprites))
    # normalize sprites length
    max_length = len(max(sprites, key=len))
    logging.debug("max sprites length = {}".format(max_length))
    normalized_sprites = ['{:<{onset}}'.format(sprite, onset=max_length)
                          for sprite in sprites]
    logging.debug("normalized sprites {}".format(normalized_sprites))

    while(True):
        yield normalized_sprites[0]
        normalized_sprites = normalized_sprites[1:] + [normalized_sprites[0]]


def animate(generator, speed=1, timeout=0):
    alarm(timeout)
    while(True):
        print(next(generator), sep='', end='\r', flush=True)
        sleep(speed)


def cli():
    from argparse import ArgumentParser
    arg_parser = ArgumentParser(description=__doc__)
    arg_parser.add_argument('--animeScroll', type=str)
    arg_parser.add_argument('--animeSprites', type=str, nargs='+')
    arg_parser.add_argument('--speed', '-s', type=float, default=1.0)
    arg_parser.add_argument('--timeout', '-t', type=int, default=0)
    arg_parser.add_argument('--log', '-l', type=str, default='INFO')

    return arg_parser.parse_args()


if __name__ == '__main__':
    opts = cli()
    FORMAT = '%(asctime):%(level)s:%(message)s'
    logging.basicConfig(format=FORMAT, level=opts.log.upper())
    if opts.animeScroll:
        animation = animation_scroll(opts.animeScroll)
    elif opts.animeSprites:
        animation = animation_sprites(opts.animeSprites)
    animate(animation, speed=opts.speed,
            timeout=opts.timeout)
