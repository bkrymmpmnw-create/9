from PIL import Image, ImageDraw, ImageFont
folder = r'D:\UserFolders\Desktop\lab9'
for i in range(1, 6):
    img = Image.open(f"{folder}\\{i}.jpg")
    draw = ImageDraw.Draw(img)
    text = "bet"
    font = ImageFont.load_default()
    draw.text((50,50),text, font = font, fill = (255,255,255))
    img.save(f"{folder}\\bet_{i}.jpg")
    print(f'Обработан:{i}.jpg')
print('Готово')