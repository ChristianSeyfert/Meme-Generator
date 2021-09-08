class QuoteModel():
    """Class for encapsulating the body and the author"""
    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __str__(self):
        return f'The author is {self.author} and his quote is {self.body}'

    def __repr__(self):
        return f'Quote: ({self.author}, - {self.body})'
