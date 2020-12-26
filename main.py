from struct import pack
from math import sin, cos, pi


def create_pixels(start, stop, step):
    x_min = y_min = float("inf")
    t = start
    x = []
    y = []
    pixels = []
    i = 0
    while t <= 2*pi:
        x.append(round((1+cos(t))*cos(t), 2))
        y.append(round((1 + cos(t)) * sin(t), 2))
        pixels.append((x[i],y[i]))
        t += step
        i += 1
    x_min = min(x)
    y_min = min(y)
    pixels.reverse()
    return pixels, x_min, y_min


def create_bmp_header(width, height):
    filetype = 19778
    reserved_1 = 0
    reserved_2 = 0
    offset = 62
    filesize = offset + 1 * width * height
    return pack("<HL2HL", filetype, filesize, reserved_1, reserved_2, offset)


def create_info_header(width, height):
    header_size = 40
    planes = 1
    bits_per_pixel = 8
    compression = 0
    image_size = 0
    x_pixels_per_meter = 0
    y_pixels_per_meter = 0
    total_colors = 2
    important_colors = 0
    return pack(
        "<3L2H6L",
        header_size,
        width,
        height,
        planes,
        bits_per_pixel,
        compression,
        image_size,
        x_pixels_per_meter,
        y_pixels_per_meter,
        total_colors,
        important_colors,
    )


color_1 = (255, 255, 255,0)
color_2 = (219, 3, 252,0)

def write_file(start, stop, step, width, height, filename,color_1,color_2):
    with open("{}.bmp".format(filename), "wb") as f:
        f.write(create_bmp_header(width, height))
        f.write(create_info_header(width, height))
        f.write(pack("<8B", *color_1, *color_2))
        pixels, x_min, y_min = create_pixels(start, stop, step)

        y_pix = y_min
        for i in range(height):
            x_pix = x_min
            for j in range(width):
                if (x_pix, y_pix) in pixels:
                    f.write(pack("<B", 1))
                else:
                    f.write(pack("<B", 0))
                x_pix = round(x_pix + step, 2)
            y_pix = round(y_pix + step, 2)


if __name__ == "__main__":
    write_file(0, 10*pi,0.01, 500, 500, "img",color_1,color_2)
print(type(color_1))
