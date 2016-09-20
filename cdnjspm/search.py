# -*- coding: utf-8 -*-
# Created by wushuyi on 2016/9/20 0020.
from sys import path
import click
from cdnjspm.api import search as api_search
from cdnjspm.cli import cli


@cli.command(help='search package for cdnjs')
@click.argument('name')
@click.option('--all', is_flag=True, help='list all search')
def search(name, **kwargs):
    _all = kwargs.get('all')
    results = api_search(name)
    if _all is False:
        results = results[0:20]
    for result in results:
        click.echo(result['name'])
