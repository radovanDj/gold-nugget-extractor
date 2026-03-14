"""State management module for tracking processing progress."""
import json
import os
from pathlib import Path


STATE_FILE = Path("output-folder/processing-state.json")


def load_state() -> dict:
    """Load the current processing state from JSON file."""
    if STATE_FILE.exists():
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"books": {}}


def save_state(state: dict) -> None:
    """Save the processing state to JSON file."""
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)


def get_processed_chapters(book_name: str) -> list:
    """Get list of already processed chapters for a book."""
    state = load_state()
    return state.get("books", {}).get(book_name, {}).get("processed_chapters", [])


def mark_chapter_processed(book_name: str, chapter_ref: str, nugget_count: int) -> None:
    """Mark a chapter as processed in the state file."""
    state = load_state()
    if book_name not in state["books"]:
        state["books"][book_name] = {"processed_chapters": [], "nuggets": {}}
    
    if chapter_ref not in state["books"][book_name]["processed_chapters"]:
        state["books"][book_name]["processed_chapters"].append(chapter_ref)
    
    state["books"][book_name]["nuggets"][chapter_ref] = nugget_count
    save_state(state)


def get_book_state(book_name: str) -> dict:
    """Get the state for a specific book."""
    state = load_state()
    return state.get("books", {}).get(book_name, {})


def get_all_books() -> list:
    """Get list of all books in the state."""
    state = load_state()
    return list(state.get("books", {}).keys())


def get_nugget_count(book_name: str, chapter_ref: str) -> int:
    """Get the number of nuggets for a specific chapter."""
    state = load_state()
    return state.get("books", {}).get(book_name, {}).get("nuggets", {}).get(chapter_ref, 0)
