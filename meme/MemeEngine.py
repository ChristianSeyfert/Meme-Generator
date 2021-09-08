from PIL import Image, ImageDraw, ImageFont
from typing import List
import random
import os


class MemeEngine():

    def __init__(self, out_path):
        """Output directory is set to tmp
        and checking if the directory already exists"""

        self.out_path = out_path

        if not os.path.isdir(self.out_path):
            os.mkdir(self.out_path)

    def make_meme(self, system_path, img, quote_body, quote_author, width=400):
        """function has been named make_meme in meme.py,
        therefore the naming scheme has to be carried
        over. The width is defined as 500px as given in
        the task in case no other value is given"""

        outfile = os.path.join(self.out_path, f'{random.randint(0,1000)}.jpg')
        image = Image.open(img)
        ratio = width/float(image.size[0])
        height = int(ratio*float(image.size[1]))
        new_image = image.resize((width, height), Image.NEAREST)

        draw = ImageDraw.Draw(new_image)
        message = quote_body + quote_author
        font = ImageFont.truetype(font=os.path.join
                                  (system_path, "fonts/LilitaOne-Regular.ttf"),
                                  size=20)
        draw.text((10, 30), message, font=font, fill='white')

        new_image.save(outfile, 'JPEG')
        return outfile
