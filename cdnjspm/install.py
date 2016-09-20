# -*- coding: utf-8 -*-
# Created by wushuyi on 2016/9/20 0020.
import click
from cdnjspm.api import grab as api_grab, asset_url, get_file
from cdnjspm.cli import cli

IDEALLY_SKIP = ['-alpha', '-beta', '-rc']


@cli.command(help='install package')
@click.argument('name')
@click.argument('version')
def install(**kwargs):
    name = kwargs.get('name')
    need_version = kwargs.get('version')
    results = api_grab(name).get('assets')
    for result in results:
        version = result.get('version')
        if any(tag in version for tag in IDEALLY_SKIP):
            continue
        if need_version == version:
            get_file(name, need_version, result.get('files'))
