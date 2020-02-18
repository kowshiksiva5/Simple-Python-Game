import array
import pygame

score = array.array('i', [0, 0])
compare = array.array('i', [0, 0])
moving = array.array('i', [1, 1, 9])
size = 48
var = array.array('i', [1, 1])
time_arr = array.array('i', [0, 0, 0, 0])
time_arr1 = array.array('i', [0, 0, 0, 0])

# init for arrays
a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
b = array.array('i', [0, 0, 0, 0])
c = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
c[4] = 1
c[7] = 1
c[10] = 1
c[13] = 1
d = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
d[5] = 1
d[8] = 1
d[11] = 1
d[14] = 1

# y coordinates for obstacles
arr = array.array('i', [2 * size, 3 * size, 4 * size, 6 * size, 7 * size, 9 * size, 10 * size, 12 * size, 13 * size, 0])
arr[9] = 15 * size
brr = [5, 8, 11, 14]
for i in range(4):
    brr[i] = brr[i] * size

# display screen
display_width = 1000
display_height = 816
gameDisplay = pygame.display.set_mode((display_width, display_height))

# colours declaration
black = (0, 0, 0)
blue = (134, 180, 188)
grey = (128, 128, 128)
