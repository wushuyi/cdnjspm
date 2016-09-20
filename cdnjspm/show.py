# -*- coding: utf-8 -*-
# Created by wushuyi on 2016/9/20 0020.
import click
from cdnjspm.api import grab as api_grab
from cdnjspm.cli import cli

IDEALLY_SKIP = ['-alpha', '-beta', '-rc']


@cli.command(help='show package version')
@click.argument('name')
@click.option('--all', is_flag=True, help='list all version')
def show(name, **kwargs):
    _all = kwargs.get('all')
    results = api_grab(name).get('assets')
    if _all is False:
        results = results[0:20]
    for result in results:
        version = result.get('version')
        if any(tag in version for tag in IDEALLY_SKIP):
            continue
        click.echo(version)
