"""
Created on September 8th, 2021

@author Chris
"""
import random
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine.Ingestor import Ingestor
from QuoteEngine.QuoteModel import QuoteModel
from meme.MemeEngine import MemeEngine


def setup(system_path: str):
    """ Load all resources """
    print(system_path)
    DogQuotes = os.path.join(system_path, '_data/DogQuotes')
    dogs = []
    for root, dirs, files in os.walk(DogQuotes):
        dogs = [os.path.join(root, name) for name in files]
    quotes = []
    for dog in dogs:
        helper = []
        helper = Ingestor.parse(dog, system_path)
        quotes.extend(helper)

    images = os.path.join(system_path, '_data/photos/dog')
    imgs = []
    for root, dirs, files in os.walk(images):
        imgs = [os.path.join(root, name) for name in files]
    return quotes, imgs


system_path = input('What is working directory of this file?')
app = Flask(__name__, static_url_path=os.path.join(system_path, 'tmp/'))
meme = MemeEngine(os.path.join(system_path, 'static/'))
quotes, imgs = setup(system_path)


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    print(f'This are the {quote} in the file')
    path = meme.make_meme(system_path, img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    image_url = request.form["image_url"]
    temp_image = os.path.join(system_path, f'static/{random.randint(0,1000)}.jpg')
    image_data = requests.get(image_url, stream=True).content
    with open(temp_image, 'wb') as f:
        f.write(image_data)

    quote_body = request.form["body"]
    print(quote_body)
    quote_author = request.form["author"]
    print(quote_author)
    path = meme.make_meme(system_path, temp_image, quote_body, quote_author)
    os.remove(temp_image)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
