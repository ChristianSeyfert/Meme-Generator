from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

from typing import List


class TXTIngestor(IngestorInterface):
    """Creating a class for importing txt files"""
    viableFormats = ['txt']

    @classmethod
    def parse(cls, path: str, system_path):
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        QuoteModels = []
        document = open(path, 'r')

        for line in document:
            items = line.split('-')
            new_quote = QuoteModel(items[0], items[1])
            print(new_quote)
            QuoteModels.append(new_quote)

        return QuoteModels
