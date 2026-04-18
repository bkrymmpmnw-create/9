from PIL import Image
img = Image.open('cat.jpg')
img.resize((img.width//3, img.height//3)).save('cat_small.jpg')
img.transpose(Image.FLIP_LEFT_RIGHT).save('cat_mirror_h.jpg')
img.transpose(Image.FLIP_TOP_BOTTOM).save('cat_mirror_v.jpg')