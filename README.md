# Gold Nugget Extractor

A Python-based tool that leverages OpenAI Agents SDK and OpenRouter to extract "Gold Nuggets" of knowledge from books and save them as structured Markdown files.

## Features

- **Chapter-by-Chapter Processing**: Systematically reads through books and extracts insights
- **State Management**: Tracks progress with JSON state file for resume capability
- **Deduplication**: Prevents duplicate nuggets from being saved
- **Retry Logic**: Handles file operation failures with automatic retries
- **Index Generation**: Creates table of contents for each book
- **Summary Reports**: Generates consolidated summaries and statistics
- **OpenRouter Integration**: Supports 100+ LLMs through OpenRouter's OpenAI-compatible API

## Architecture

| Layer | Component | Description |
| :--- | :--- | :--- |
| **Orchestration** | OpenAI Agents SDK | Manages the agent loop and response handling |
| **Knowledge Base** | ChromaDB Vector DB | Provides `keyword_search` and `semantic_search` to retrieve text |
| **File System** | Custom Python Tool | Handles local I/O for saving `.md` nuggets |
| **LLM Engine** | OpenRouter | Provides access to 100+ LLMs (Gemini, Claude, GPT, etc.) |
| **State Management** | JSON State File | Tracks processed chapters and nuggets |

## Installation

1. Clone the repository:
```bash
cd gold-nugget-extractor
```

2. Install dependencies:
```bash
uv sync
```

3. Create a `.env` file from the example:
```bash
cp .env.example .env
```

4. Update the `.env` file with your OpenRouter API key:
```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
LLM_MODEL=google/gemini-3-flash:free
```

## Configuration

### OpenRouter API Key

Get your API key from [https://openrouter.ai/](https://openrouter.ai/)

### Model Selection

The `LLM_MODEL` environment variable accepts OpenRouter model IDs in the format `provider/model:variant`. Examples:

- `google/gemini-3-flash:free`
- `google/gemini-2.0-flash-exp`
- `anthropic/claude-3.5-sonnet`
- `openai/gpt-4o`
- `meta-llama/llama-3.1-8b-instruct`

## Usage

### Command Line

```bash
# Activate the virtual environment
source .venv/bin/activate

# Run extraction for a book
python -m gold_nugget_extractor.main "Book Title"

# Specify a different model
python -m gold_nugget_extractor.main "Book Title" --model google/gemini-3-flash:free

# Specify a different output directory
python -m gold_nugget_extractor.main "Book Title" --output-dir my-output
```

### Python API

```python
from gold_nugget_extractor import GoldNuggetExtractor

# Create extractor instance
extractor = GoldNuggetExtractor("Book Title")

# Run extraction
result = extractor.run()

print(f"Processed {result['total_chapters']} chapters")
print(f"Extracted {result['total_nuggets']} nuggets")
```

## Output Structure

```
output-folder/
├── processing-state.json
└── nuggets-of-knowledge/
    └── [book-name]/
        ├── index.md
        ├── chapter_1_a1b2c3d4.md
        ├── chapter_1_e5f6g7h8.md
        └── chapter_2_i9j0k1l2.md
```

### State File Structure

```json
{
  "books": {
    "book-title": {
      "processed_chapters": ["Chapter 1", "Chapter 2"],
      "nuggets": {
        "Chapter 1": 2,
        "Chapter 2": 1
      }
    }
  }
}
```

## Nugget Format

Each extracted nugget follows this format:

```markdown
# [Insight Title]

> "[Quote/Concept]"

*Reference: Book Name, Chapter, Paragraph*

## Explanation

[3-4 sentences explaining the importance]

## Final Thoughts

[2-3 sentences with final thoughts]

---
```

## Project Structure

```
gold-nugget-extractor/
├── src/
│   └── gold_nugget_extractor/
│       ├── __init__.py
│       ├── agent.py      # Main OpenAI Agents SDK agent
│       ├── state.py      # State management
│       ├── nuggets.py    # Nugget saving with deduplication
│       └── index.py      # Index and summary generation
├── .env.example
├── pyproject.toml
└── README.md
```

## Development

```bash
# Install in development mode
uv sync

# Run tests
pytest

# Format code
ruff format .

# Lint code
ruff check .
```

## License

MIT License
