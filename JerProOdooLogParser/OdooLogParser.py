#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse, odoo_log_parser, os, sys, importlib

def Main(exec_name, exec_argv):
    """
    Program entry-point - Parses the command line arguments and
    invokes corresponding semantics.
        exec_name   The bin name used to call the program.
        exec_argv   Array of program arguments to parse.
    """
    # Cmdline config:
    parser = argparse.ArgumentParser(description='A program for parsing and resuming Odoo logs.')
    parser.add_argument('--odoolog', type=str,
        help=('Odoo ligfile path.'))
    args = parser.parse_args(args=exec_argv)

if __name__ == "__main__": exit(Main(exec_name=sys.argv[0], exec_argv=sys.argv[1:]))