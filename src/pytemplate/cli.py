"""
This module serves as the main entry point into the CLI application.
You can see as much by looking at the pyproject.toml "entrypoint" section.

You can remove this and replace it with a classic main.py if you wish.
"""

import click

from .addition import addition

_context_settings: dict = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=_context_settings, invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """
    Pytemplate - A Sample application for creating python projects.
    Licensed under the MIT License.
    """
    if ctx.invoked_subcommand is None:
        click.echo(
            "Pytemplate - A Sample application for creating python projects.\nLicensed under the MIT License.\n\nTry running again with 'add' subcommand and two numbers."
        )
        exit(0)


@click.command()
@click.argument(
    "number1",
    type=click.FLOAT,
    required=1,
    metavar="[NUM1]",
)
@click.argument(
    "number2",
    type=click.FLOAT,
    required=1,
    metavar="[NUM2]",
)
def add(number1: float, number2: float) -> None:
    """
    Add the two selected numbers together.
    """
    result = str(addition.add(number1, number2))

    click.echo("Your result is: " + result)


cli.add_command(add)
