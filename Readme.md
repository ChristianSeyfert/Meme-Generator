# Meme Generator

The Meme Generator ingests pictures of dogs (or any pictures you add) and a quote and creates a Meme.

## Installation

Use the pip manager in order to install the pending requirements via requirements.txt.

```bash
pip install requirements
```

## Usage

There are two different options for using this file, one via app.py and one via meme.py.

```bash
With Meme.py you can you the script via inputing 3 additional parsers, one for the link, one for the quote 
and one for the author.
Additionally you have to input one parser for the system_path, this is the directory of meme.py. The default
folder is /Users/Chris/Desktop/src/.
```

```bash
With app.py you will start a flask server where you can create random memes. The templates for this are included
in _data/ folder.
You can also create customized memes. For this you will need to input the URL of the image as well as a quote
and the author in the browser.
```

## Contributing
The script is based on the lessons of Intermediate Python, an Udacity class for advanced python training. Additionally references have been made via StackOverflow and the Knowledge Base of Udacity.

## License
Udacity