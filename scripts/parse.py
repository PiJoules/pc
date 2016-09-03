#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import print_function

from pc.parser import Parser
from utils import base_parse_args

import json


def get_args():
    from argparse import ArgumentParser
    parser = ArgumentParser(
        description="Print the resulting parse tree in JSON.")

    args = base_parse_args(parser)
    return args


def main():
    args = get_args()

    filename = args.filename
    parser = Parser(filename)
    parse_tree = parser.parse()
    print(json.dumps(parse_tree.json(), indent=4))
    return 0


if __name__ == "__main__":
    main()
