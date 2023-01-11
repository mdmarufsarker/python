from PIL import Image

bee = Image.open('bee22.png')
red = Image.open('red.jpg')
blue = Image.open('blue.png')

blue.putalpha(255)
blue.putalpha(280)
print(blue)
