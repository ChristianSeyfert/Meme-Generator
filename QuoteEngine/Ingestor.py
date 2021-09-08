from .IngestorInterface import IngestorInterface
from .csvIngestor import CSVIngestor
from .docxIngestor import DOCXIngestor
from .txtIngestor import TXTIngestor
from .pdfIngestor import PDFIngestor

from typing import List


class Ingestor(IngestorInterface):
    """Class for encapsulating the 4 helper classes for each extension"""
    ingestors = [CSVIngestor, DOCXIngestor, TXTIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str, system_path):
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path, system_path)
