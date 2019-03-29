x, y, z = 6, 5, 4
small = x if (x < y and x < z) else (y if y < z else z)
print('Smallest Number:', small)
