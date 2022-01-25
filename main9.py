import click
import datetime
from enum import Enum
import random
import logging
from pathlib import Path

logfile = 'log_1.log'

log = logging.getLogger("my_log")
log.setLevel(logging.INFO)
FH = logging.FileHandler(logfile)
basic_formater = logging.Formatter('%(asctime)s : [%(levelname)s] : %(message)s')
FH.setFormatter(basic_formater)
log.addHandler(FH)

@click.group()
def test():
    pass

@test.command()
@click.option('--hours', is_flag=True) 
def newyear(hours):
    date_sys= datetime.datetime.now()
    date_newy=datetime.datetime(2023,1,1)
    delta=date_newy-date_sys
    hours_1 = delta.total_seconds()// 3600
    if hours: 
        click.echo(print(f'Дней до нового года {int(hours_1//24)} и {int(hours_1%24)} часов'))
    else:
        click.echo(print(f'Дней до нового года {int(hours_1//24)}'))

@test.command()
def toy():
    class Toys(Enum):
        RED = "Red Ball"
        PURPLE = "Puple Angel"

    click.echo(print(random.choice(list(Toys)).value))

@test.command()
def prename():
    try:
        for x in Path('directory/').iterdir():
            p = x.parent / (x.stem.replace('-', '/') + '.txt')
            p.parent.mkdir(parents=True, exist_ok=True)
            x.rename(p)   
        log.info("finish program")
    except Exception as Ex:
	    log.error(Ex)

if __name__ == '__main__':
    test()