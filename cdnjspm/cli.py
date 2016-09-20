# -*- coding: utf-8 -*-
# Created by wushuyi on 2016/9/20 0020.
import click
from cdnjspm import __VERSION_STR__


@click.group()
def cli():
    pass


@cli.command(help='print version')
def version():
    print("cdnjspm version {0}".format(__VERSION_STR__))
