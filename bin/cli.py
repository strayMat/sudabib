#! /usr/bin/env python
import logging

import click

from sudabib.constants import LOG_LEVEL
from sudabib.utils import hello

logging.basicConfig(
    level=logging.getLevelName(LOG_LEVEL),
    format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
)


@click.group()
@click.version_option(package_name="sudabib")
def cli():
    pass


@cli.command()
def main() -> None:
    """sudabib Main entrypoint"""
    click.secho(hello(), fg="green")


if __name__ == "__main__":
    cli()
