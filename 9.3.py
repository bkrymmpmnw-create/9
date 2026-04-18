from PIL import Image, ImageFilter
folder = open("cat.jpg")
for i in range(1,6):
    filename = f'{i}.jpg'
    with Image.open(f'{folder}//{i}.jpg'):
            filtered = img.filter(ImageFilter.CONTOUR)
            filtered.save(f'f{folder}\\filtered_{i}.jpg')
            print(f'Обработан: {i}.jpg -> filtered_{i}.jpg')
print("Готово")