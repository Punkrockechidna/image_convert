from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img.save('blur','png')

# filtered_img = img.convert('L')
# filtered_img.save('grey.png','png')

# filtered_img = img.convert('L')
# crooked = filtered_img.rotate(90)
# crooked.save('crooked.png','png')
# crooked.show()

# resize = filtered_img.resize((300,300))
# resize.save('resize.png','png')

filtered_img = img.convert('L')
box = (100,100,400,400)
region = filtered_img.crop(box)
region.save("crop.png", 'png')
