# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     proxy_pool
   Description :   Proxy pool entry point
   Author :        JHao
   date：          2020/6/19
-------------------------------------------------
   Change Activity:
                   2020/6/19:
-------------------------------------------------
"""
__author__ = 'JHao'

import click
from helper.launcher import startServer, startScheduler
from setting import BANNER, VERSION

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=VERSION)
def cli():
    """ProxyPool CLI tool"""


@cli.command(name="schedule")
def schedule():
    """ Start the scheduler """
    click.echo(BANNER)
    startScheduler()


@cli.command(name="server")
def server():
    """ Start the API server """
    click.echo(BANNER)
    startServer()


if __name__ == '__main__':
    cli()
