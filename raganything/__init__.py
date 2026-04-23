"""RAG-Anything: A multimodal RAG framework that handles any type of document.

Supports text, images, tables, equations, and other modalities through
an integrated pipeline built on top of LightRAG.
"""

from raganything.raganything import RAGAnything
from raganything.modalprocessors import (
    ImageProcessor,
    TableProcessor,
    EquationProcessor,
    GeneralProcessor,
)

__version__ = "0.1.0"
__author__ = "HKUDS"
__license__ = "MIT"

__all__ = [
    "RAGAnything",
    "ImageProcessor",
    "TableProcessor",
    "EquationProcessor",
    "GeneralProcessor",
]
