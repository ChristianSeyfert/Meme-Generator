from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

import docx
from typing import List


class DOCXIngestor(IngestorInterface):
    """Using the docx class from lesson 4"""
    viableFormats = ['docx']

    @classmethod
    def parse(cls, path: str, system_path):
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        QuoteModels = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                new_quote = QuoteModel(parse[0], parse[1])
                QuoteModels.append(new_quote)

        return QuoteModels
