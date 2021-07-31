import os
import random

def generate_field():
    field = list()
    for _ in range(25):
        field.append( [random.choice([True, False]) for _ in range(25)] )
    return field


def draw(field):
    os.system('cls')
    for row in field:
        for cell in row:
            if cell:
                print('■', end='')
            else:
                print('□', end='')
        print()

if __name__ == '__main__':
    draw(generate_field())