"""Gold Nugget Extractor - Extract insights from books using OpenAI Agents SDK and OpenRouter."""
from gold_nugget_extractor.agent import (
    GoldNuggetExtractor,
    VectorDBClient,
    create_gold_nugget_agent,
    create_openrouter_client,
)
from gold_nugget_extractor.state import load_state, save_state, get_processed_chapters, mark_chapter_processed
from gold_nugget_extractor.nuggets import save_gold_nugget, check_duplicate
from gold_nugget_extractor.index import generate_book_index, generate_book_summary

__version__ = "0.1.0"
__all__ = [
    "GoldNuggetExtractor",
    "create_gold_nugget_agent",
    "create_openrouter_client",
    "load_state",
    "save_state",
    "get_processed_chapters",
    "mark_chapter_processed",
    "VectorDBClient",
    "save_gold_nugget",
    "check_duplicate",
    "generate_book_index",
    "generate_book_summary",
]
