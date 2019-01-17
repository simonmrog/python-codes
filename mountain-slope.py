# Program used for hiking, to calculate the slope of a mountain based
# on data given by a gps program

import math
import click

@click.group ()
def main ():
    pass


# implementation for command line using click framework
@main.command ()
@click.argument ("r1")
@click.argument ("y1")
@click.argument ("r2")
@click.argument ("y2")
def c (r1, y1, r2, y2):
    # r1, r2 in kms and y1, y2 in metres
    """ Calculates the slope with parameters: r1, y1, r2, y2 """
    delta_r = abs (float (r1) - float (r2)) * 1000 #delta_r in metres
    delta_y = abs (float (y1) - float (y2)) #delta_y is already in metres
    m_percent = delta_y / math.sqrt (delta_r ** 2 - delta_y ** 2) * 100
    click.echo ("Slope: %.2f%%" % m_percent)


if __name__ == "__main__":
  main ();
