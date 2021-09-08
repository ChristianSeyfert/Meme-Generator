from .IngestorInterface import IngestorInterface
from .txtIngestor import TXTIngestor
from .QuoteModel import QuoteModel

from typing import List
import os
import random
import subprocess


class PDFIngestor(IngestorInterface):
    """Class for importing pdf files using the lesson complex strategies
    the in the class presented way apparently does not work anymore,
    found a strategy on stackoverflow to solve this problem
    (line 23 - 25)"""
    viableFormats = ['pdf']

    @classmethod
    def parse(cls, path: str, system_path):
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        file = os.path.join(system_path, f'static/{random.randint(0, 100)}.txt')
        with open(file, 'w'):
            cmd = f"./pdftotext -layout -nopgbrk {path} {file}"
            subprocess.call(cmd, shell=True, stderr=subprocess.STDOUT)

        QuoteModels = []
        new_file = open(file, 'r')
        for line in new_file.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                items = line.split('-')
                new_quote = QuoteModel(items[0], items[1])
                QuoteModels.append(new_quote)

        new_file.close()
        os.remove(file)
        return QuoteModels
