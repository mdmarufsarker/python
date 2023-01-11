from PIL import Image

img = Image.open('bee22.png')

# img.show()

print(img.size)
print(img.format_description)
'''
(1080, 1080)
Portable network graphics
'''

# crop image
x = 0
y = 0
w = 100
h = 100
# img.crop((x, y, w, h))

# halfway = 1993 / 2
# x = halfway - 200
# w = halfway + 200
# y = 800
# h = 1257
# img.crop((x,y,w,h))

# copy image
crp = img.crop((x, y, w, h))
img.paste(im=crp, box=(0, 0))

# resize image
img.resize((3000, 500))

# rotate image
img.rotate(90)


