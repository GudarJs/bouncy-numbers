import click

from bouncy.utils import is_bouncy, calculate_least_number


@click.group()
def cli():
    pass

@cli.command()
@click.option('--proportion', default=99, help='Proportion of bouncy numbers')
def calculate(proportion):
    least_number = calculate_least_number(proportion)
    click.echo('The least number for which the proportion of bouncy numbers is exactly {}% is: {}'.format(proportion, least_number))

@cli.command()
@click.option('--number', help='Number to check if is bouncy')
def checknumber(number):
    is_number_bouncy = is_bouncy(number)
    click.echo('Number "{}" is bouncy: {}'.format(number, is_number_bouncy))
    