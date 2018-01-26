import click

from .settings import Config

from .camera.core import camera_main
from .client.core import client_main
from .middleman.core import middleman_main
from .central.core import central_main

fog_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('-v', '--verbose', is_flag=True,
              help='Enables verbose mode.')
@fog_config
def cli(config, verbose):
    config.verbose = verbose


@cli.command()
@fog_config
def client(config):
    if config.verbose:
        click.echo("We are in the edge layer")
    client_main()


@cli.command()
@click.argument('video', required=False)
@click.option('--n', default=1, help="Number of videos")
@click.option('-r', default=False, is_flag=True, help="Randomize videos")
@fog_config
def camera(config, video, n, r):
    if config.verbose:
        click.echo("We are in the edge layer")
    camera_main(video, n, r)


@cli.command()
@fog_config
def middleman(config):
    if config.verbose:
        click.echo("We are in the fog layer")
    middleman_main()


@cli.command()
@fog_config
def central(config):
    if config.verbose:
        click.echo("We are in the cloud layer")
    central_main()


def main():
    cli()
