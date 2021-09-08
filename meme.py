import os
import random
import argparse

from QuoteEngine.Ingestor import Ingestor
from QuoteEngine.QuoteModel import QuoteModel
from meme.MemeEngine import MemeEngine


def generate_meme(system_path, path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    print(os.getcwd())
    img = None
    quote = None
    if path is None:
        images = os.path.join(system_path, '_data/photos/dog')
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]
        img = random.choice(imgs)
    else:
        imgs = []
        for root, dirs, files in os.walk(path):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)

    if body is None:

        DogQuotes = os.path.join(system_path, '_data/DogQuotes')
        dogs = []
        for root, dirs, files in os.walk(DogQuotes):
            dogs = [os.path.join(root, name) for name in files]
        quotes = []
        for dog in dogs:
            helper = []
            helper = Ingestor.parse(dog, system_path)
            quotes.extend(helper)

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine(os.path.join(system_path, 'static/'))
    result = meme.make_meme(system_path, img, quote.body, quote.author)
    return result


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Create a meme.")
    parser.add_argument('--system_path', type=str,
                        default='/Users/Chris/Desktop/src/')
    parser.add_argument('--path', type=str, default=None)
    parser.add_argument('--body', type=str, default=None)
    parser.add_argument('--author', type=str, default=None)

    args = parser.parse_args()
    system_path = args.system_path
    path = args.path
    body = args.body
    author = args.author
    print(generate_meme(system_path, args.path, args.body, args.author))
