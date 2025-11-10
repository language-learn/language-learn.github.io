# Anki Deck Generator

This script recursively scans the `vokabular/` and `grammatik/` directories for CSV files and generates a hierarchical Anki deck that can be imported into Anki.

## Requirements

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

## Installation

### Using uv (recommended)

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh
```

No additional installation needed! uv will automatically install dependencies when you run the script.

### Using pip (alternative)

```bash
cd scripts
pip install -r requirements.txt
```

## Usage

### Using uv (recommended)

```bash
# From the scripts directory
cd scripts
uv run --with genanki create_anki_deck.py

# Or from the repo root
uv run --with genanki scripts/create_anki_deck.py
```

### Using python directly (after pip install)

```bash
python scripts/create_anki_deck.py
```

## Output

The script will generate a file called `Deutsch_C1.apkg` in the `static/downloads/` directory. This file can be imported into Anki via **File → Import** or downloaded from the website.

## Deck Structure

The generated deck follows this hierarchical structure:

```
Deutsch C1
├── Vokabular
│   ├── Essen
│   ├── Reisen
│   └── ...
└── Grammatik
    ├── Vergangenheitsformen
    ├── Konjunktiv
    └── ...
```

## CSV Format

### Vocabulary Files (`vokabular/*/vokabeln.csv`)

```csv
deutsch_translated,deutsch
the fork,die Gabel
the knife,das Messer
```

### Grammar Files (`grammatik/*/aufgaben.csv`)

```csv
Frage,Antwort
"Bilde das Perfekt: ich (gehen)","ich bin gegangen"
"Bilde das Perfekt: du (essen)","du hast gegessen"
```
