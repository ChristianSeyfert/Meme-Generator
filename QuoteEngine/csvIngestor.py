from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

import pandas
from typing import List


class CSVIngestor(IngestorInterface):
    """Using the csv class from lesson 4"""
    viableFormats = ['csv']

    @classmethod
    def parse(cls, path: str, system_path):
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        QuoteModels = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            print()
            new_quote = QuoteModel(row['body'], row['author'])
            QuoteModels.append(new_quote)

        return QuoteModels
