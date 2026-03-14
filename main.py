#!/usr/bin/env python3
"""Main entry point for Gold Nugget Extractor."""
import argparse
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from gold_nugget_extractor import GoldNuggetExtractor


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Gold Nugget Extractor")
    parser.add_argument("book_name", help="Name of the book to process")
    parser.add_argument("--model", default=None, help="LLM model to use (OpenRouter format)")
    parser.add_argument("--output-dir", default="output-folder", help="Output directory")
    args = parser.parse_args()
    
    # Set output directory
    import gold_nugget_extractor.state as state_module
    state_module.STATE_FILE = Path(args.output_dir) / "processing-state.json"
    
    # Run extraction
    extractor = GoldNuggetExtractor(args.book_name, args.model)
    result = extractor.run()
    
    print(f"\nExtraction complete!")
    print(f"Book: {result['book_name']}")
    print(f"Total chapters: {result['total_chapters']}")
    print(f"Total nuggets: {result['total_nuggets']}")
    print(f"Index: {result['index_path']}")
    print(f"Summary: {result['summary_path']}")


if __name__ == "__main__":
    main()
