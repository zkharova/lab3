import math
from math import sin

Ox_offset = -3  # смещения по осям Х и У
Oy_offset = -3
t = 0
width = 600
height = 600
all_values = []
pixel = []
STEP = 0.01
while t <= 12 * math.pi:
    x = round(sin(t + math.pi / 2), 2)
    y = round(sin(2*t), 2)
    pixel.append(x)
    pixel.append(y)
    all_values.append(tuple(pixel))  # добавляем в список всех знач. кортеж пиксель, сост. из 2х элементов
    pixel.clear()
    t += STEP

with open('result.bmp', 'w+b') as f:  # Открываю файл на запись в двоичнм режиме
    f.write(b'BM')
    f.write((154).to_bytes(4, byteorder='little'))
    f.write((0).to_bytes(2, byteorder='little'))
    f.write((0).to_bytes(2, byteorder='little'))

    f.write((122).to_bytes(4, byteorder='little'))
    f.write((108).to_bytes(4, byteorder='little'))
    f.write((600).to_bytes(4, byteorder='little'))
    f.write((600).to_bytes(4, byteorder='little'))
    f.write((1).to_bytes(2, byteorder='little'))
    f.write((32).to_bytes(2, byteorder='little'))
    f.write((3).to_bytes(4, byteorder='little'))
    f.write((32).to_bytes(4, byteorder='little'))
    f.write((2835).to_bytes(4, byteorder='little'))
    f.write((2835).to_bytes(4, byteorder='little'))
    f.write((0).to_bytes(4, byteorder='little'))
    f.write((0).to_bytes(4, byteorder='little'))

    f.write(b'\x00\x00\xFF\x00')
    f.write(b'\x00\xFF\x00\x00')
    f.write(b'\xFF\x00\x00\x00')
    f.write(b'\x00\x00\x00\xFF')

    f.write(b' niW')
    f.write((0).to_bytes(36, byteorder='little'))
    f.write((0).to_bytes(4, byteorder='little'))
    f.write((0).to_bytes(4, byteorder='little'))
    f.write((0).to_bytes(4, byteorder='little'))

    f.write(b'\x00\x00\x00\xFF')
    for y_counter in range(600):  # красим пиксели черным,если их занчение есть в списке всех значений
        Ox_offset = -3
        for x_counter in range(600):
            if (Ox_offset, Oy_offset) in all_values:
                f.write(b'\x00\x00\x00\xFF')
            else:
                f.write(b'\xFF\xFF\xFF\xFF')
            Ox_offset = round(Ox_offset + STEP, 2)
        Oy_offset = round(Oy_offset + STEP, 2)
    f.close()