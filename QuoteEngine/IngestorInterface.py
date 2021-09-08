from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract Base Class for the ingestors with two class methods"""
    viableFormats = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        for viableFormat in cls.viableFormats:
            if viableFormat in path:
                return True
            else:
                return False

    @classmethod
    @abstractmethod
    def parse(cls, path: str, system_path):
        pass
