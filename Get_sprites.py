from PIL import Image


def get_img():
    img = Image.open('NES_Sprites.png')
    # print(img.format, img.size, img.mode)
    # img.show()
    box = (0, 1, 15, 16)
    region = img.crop(box)
    # region.show()
    return region
