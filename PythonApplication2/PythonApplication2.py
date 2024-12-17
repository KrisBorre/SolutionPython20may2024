import numpy as np

array = np.array([1, 2, 3])
print(array)

# [1 2 3]


def add_numbers(a, b):
    return a + b


print(add_numbers(2, 3))

# 5

from colorama import Fore, Style, init

# Initialize colorama (only required on Windows)
init()

print(Fore.RED + "This is red text")
print(Fore.GREEN + "This is green text")
print(Style.RESET_ALL + "Back to normal")    


def add_numbers(a: int, b: int) -> int:
    return a + b

result = add_numbers(5, 10)  


import click

@click.command()
@click.option('--name', default='World', help='Name to greet.')
def greet(name):
    click.echo(f"Hello, {name}!")

if __name__ == '__main__':
    greet()

# python script.py --name Alice


