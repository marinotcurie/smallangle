import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def cmd_group():
    pass
    
@cmd_group.command()

@click.option(
    "-n",
    "--number",
    default = 1
)


def sin(number):
    """Calculates the sin values between 0 and 2pi with given amount of steps

    Args:
        number (int): the amount of steps
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)


@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default = 1
)

def tan(number):
    """Calculates the tan values between 0 and 2pi with given amount of steps

    Args:
        number (int): the amount of steps 
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    cmd_group()
    
