import operator
from PIL import Image

im = Image.open("a1.jpg")
im = im.convert("P")
im2 = Image.new("P",im.size,255)

im = im.convert("P")
print(im.histogram(),"\n")
his = im.histogram()


values = {}

for i in range(256):
  values[i] = his[i]

for j,k in sorted(values.items(), key=operator.itemgetter(1), reverse=True)[:10]:
  print (j,k)

temp = {}

for x in range(im.size[1]):
  for y in range(im.size[0]):
    pix = im.getpixel((y,x))
    temp[pix] = pix
    if pix == 0 or pix == 243 or pix == 244 or pix == 245 or pix == 246 or pix == 247: # these are the numbers to get
      im2.putpixel((y,x),0)

im2.save("output.gif")
im2.show()