import os
import random

def generate_field(x_size, y_size):
    field = list()
    for _ in range(x_size):
        field.append( [random.choice([True, False]) for _ in range(y_size)] )
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
    draw(generate_field(25, 25))