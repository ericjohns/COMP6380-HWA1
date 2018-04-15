from PIL import Image, ImageChops

point_table = ([0] + ([255] * 255))

def black_or_b(a, b):
    diff = ImageChops.difference(a, b)
    diff = diff.convert('L')
    diff = diff.point(point_table)
    new = diff.convert('RGB')
    new.paste(b, mask=diff)
    return new

def black_or_b(c, d):
    diff = ImageChops.difference(c, d)
    diff = diff.convert('L')
    diff = diff.point(point_table)
    new = diff.convert('RGB')
    new.paste(b, mask=diff)
    return new

def black_or_b(x, y):
    diff = ImageChops.difference(x, y)
    diff = diff.convert('L')
    diff = diff.point(point_table)
    new = diff.convert('RGB')
    new.paste(b, mask=diff)
    return new

a = Image.open('a0.jpg')
b = Image.open('a1.jpg')
c = Image.open('a2.jpg')
d = Image.open('a3.jpg')
x = black_or_b(a, b)
y = black_or_b(c, d)
z = black_or_b(x, y)
z.save('z.png')