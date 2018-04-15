from PIL import Image, ImageChops

point_table = ([0] + ([255] * 255))

def black_or_b(a, b):
    a = a.convert('L')
    #a = ImageChops.invert(a)
    b = b.convert('L')
    #b = ImageChops.invert(b)
    diff = ImageChops.difference(a, b)
    #diff = diff.convert('L')
    new = ImageChops.invert(diff)
    #diff = diff.point(point_table)
   # new = diff.convert('RGB')
    #new.paste(b, mask=diff)
    #new = ImageChops.invert(diff)
    return new

    


a = Image.open('b0.jpg')
b = Image.open('b1.jpg')
c = Image.open('b2.jpg')
d = Image.open('b3.jpg')
e = Image.open('b4.jpg')
f = Image.open('b5.jpg')
g = Image.open('b6.jpg')
h = Image.open('b7.jpg')
i = Image.open('b8.jpg')
j = Image.open('b9.jpg')
k = Image.open('b10.jpg')
l = Image.open('b11.jpg')
result1 = black_or_b(a, b)
result2 = black_or_b(c, d)
result3 = black_or_b(e, f)
result4 = black_or_b(g, h)
result5 = black_or_b(i, j)
result6 = black_or_b(k, l)
result7 = black_or_b(result1, result2)
result8 = black_or_b(result3, result4)
result9 = black_or_b(result5, result6)
result10 = black_or_b(result7, result8)
result11 = black_or_b(result8, result9)
result12 = black_or_b(result10, result11)
result12.save('z_B.png')
print(result12.histogram(),"\n")