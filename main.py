import random
import numpy as np
from PIL import Image

def get_neighbors_wall_count(x_index: int, y_index: int, noise: [str]) -> int:
    # returns number of walls adjacent (incl. diagonals)
    wall_count = 0
    for y in range(-1, 2):
        for x in range(-1, 2):
            if x == y == 0: continue  # don't count self
            x_check = x_index + x
            y_check = y_index + y
            if 0 > x_check or x_check >= len(noise[0]) or 0 > y_check or y_check >= len(noise)\
              or noise[y_check][x_check] == WALL:
                wall_count += 1
    return wall_count


def iterate(grid: [str]) -> [str]:
    next_grid = grid.copy()
    for y in range(len(grid)):
        row = list(next_grid[y])
        for x in range(len(grid[y])):
            row[x] = WALL \
                if get_neighbors_wall_count(x, y, grid) > wall_threshold else FLOOR
        # next_grid[y] = ''.join(row)
        next_grid[y] = row
    return next_grid


WALL = 255
FLOOR = 0
noise_grid = []
cellular_grid = []
noise_density = 0.5
wall_threshold = 4
iterations = 2

if __name__ == '__main__':
    width = 800
    height = 800
    for y in range(height):
        noise_grid.append([])
        for _ in range(width):
            noise_grid[-1].append(FLOOR)

    # generate noise
    for y in range(height):
        row = list(noise_grid[y])
        for x in range(width):
            if random.random() <= noise_density:
                row[x] = WALL
        # noise_grid[y] = ''.join(row)
        noise_grid[y] = row

    for y in noise_grid:
        print(y)

    cellular_grid = noise_grid.copy()
    print('\nCellular grid:')
    for i in range(iterations):
        print(f'\n\nIteration: {i}')
        cellular_grid = iterate(cellular_grid)
        for y in cellular_grid:
            print(y)

    # bits = np.array(cellular_grid)
    # bits = np.packbits(bits)
    # bits.tofile('image.png')
    image = Image.fromarray(np.uint32(cellular_grid), 'L')
    image.save('pil_image.png')



