# -*- coding: utf-8 -*-
"""Main module."""
import sys

import click


@click.command()
def main(args=None):
    click.echo("Replace this message by putting your code into "
               "satio.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
