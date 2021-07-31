import os
import random
import time

LIVE = True
DEAD = False

def generate_field(x_size, y_size):
    field = list()
    for _ in range(x_size):
        field.append( [random.choice([True, False]) for _ in range(y_size)] )
    return field

def validate_coord(value, max_value):
    if value < 0:
        return max_value
    elif max_value < value:
        return 0
    return value

def get_around_cells(x, y, field):
    y_max = len(field) - 1
    x_max = len(field[0]) - 1

    around_cells = list()
    for i in range(3):
        for j in range(3):
            cell_x = x+j-1
            cell_y = y+i-1
            if x == cell_x and y == cell_y:
                continue
            cell_x = validate_coord(cell_x, x_max)
            cell_y = validate_coord(cell_y, y_max)
            around_cells.append(field[cell_y][cell_x])
    return around_cells

def eval_cell(x, y, field):
    around_cells = get_around_cells(x, y, field)
    live_count = around_cells.count(LIVE)

    if field[y][x] == DEAD:
        if live_count == 3:
            return LIVE
        else:
            return DEAD

    if field[y][x] == LIVE:
        if 2 <= live_count and live_count <= 3:
            return LIVE
        elif live_count <= 1:
            return DEAD
        elif 4 <= live_count:
            return DEAD

def eval_cells(field):
    new_field = list()
    for y in range(len(field)):
        new_field.append(list())
        for x in range(len(field[0])):
            new_field[y].append(eval_cell(x, y, field))
    return new_field

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
    x_size = 25
    y_size = 25
    field = generate_field(x_size, y_size)
    
    while True:
        time.sleep(0.2)
        new_field = eval_cells(field)
        draw(new_field)
        field = new_field
    