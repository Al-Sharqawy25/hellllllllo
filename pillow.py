import PIL

from PIL import Image, ImageFilter

# img_path = Image.open('1632507145167.jpg')
before = Image.open('1632507145167.jpg')
# img_path.show()
# img_path.save('programmer.png')
# after = before.filter(ImageFilter.BoxBlur(5))
after = before.convert('L')
after.save('programmer.png')
