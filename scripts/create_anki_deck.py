#!/usr/bin/env python3
"""
Anki Deck Generator for German C1 Learning Platform

This script recursively searches for CSV files in the vokabular/ and grammatik/
directories and creates a hierarchical Anki deck (.apkg file) that can be
imported into Anki.

Requirements:
    pip install genanki

Usage:
    python create_anki_deck.py
"""

import csv
import os
import random
import genanki # type: ignore
from pathlib import Path


# Generate unique model IDs using random.randrange(1 << 30, 1 << 31)
VOCABULARY_MODEL_ID = random.randrange(1 << 30, 1 << 31)
GRAMMAR_MODEL_ID = random.randrange(1 << 30, 1 << 31)


# Create a model for vocabulary cards (German → English)
vocabulary_model = genanki.Model(
    VOCABULARY_MODEL_ID,
    'Deutsch C1 Vokabular',
    fields=[
        {'name': 'Deutsch'},
        {'name': 'English'},
    ],
    templates=[
        {
            'name': 'Deutsch → English',
            'qfmt': '<div style="font-size: 24px; text-align: center;">{{Deutsch}}</div>',
            'afmt': '''
                <div style="font-size: 24px; text-align: center;">{{Deutsch}}</div>
                <hr id="answer">
                <div style="font-size: 20px; text-align: center; color: #0066cc;">{{English}}</div>
            ''',
        },
    ],
    css='''
        .card {
            font-family: arial;
            font-size: 20px;
            text-align: center;
            color: black;
            background-color: white;
        }
    '''
)


# Create a model for grammar exercise cards (Question → Answer)
grammar_model = genanki.Model(
    GRAMMAR_MODEL_ID,
    'Deutsch C1 Grammatik',
    fields=[
        {'name': 'Frage'},
        {'name': 'Antwort'},
    ],
    templates=[
        {
            'name': 'Grammatik Übung',
            'qfmt': '<div style="font-size: 18px;">{{Frage}}</div>',
            'afmt': '''
                <div style="font-size: 18px;">{{Frage}}</div>
                <hr id="answer">
                <div style="font-size: 18px; color: #006600;"><strong>{{Antwort}}</strong></div>
            ''',
        },
    ],
    css='''
        .card {
            font-family: arial;
            font-size: 18px;
            color: black;
            background-color: white;
            padding: 20px;
        }
    '''
)


def get_deck_name_from_path(base_dir, csv_path):
    """
    Generate a hierarchical deck name from the file path.

    Example:
        vokabular/01_essen/vokabeln.csv → "Deutsch C1::Vokabular::Essen"
        grammatik/01_vergangenheitsformen/aufgaben.csv → "Deutsch C1::Grammatik::Vergangenheitsformen"
    """
    rel_path = os.path.relpath(csv_path, base_dir)
    parts = Path(rel_path).parts

    # Build deck name
    deck_parts = ["Deutsch C1"]

    # Add category (Vokabular or Grammatik)
    if parts[0] == "vokabular":
        deck_parts.append("Vokabular")
    elif parts[0] == "grammatik":
        deck_parts.append("Grammatik")

    # Add topic name (remove number prefix like "01_")
    if len(parts) > 1:
        topic = parts[1]
        # Remove number prefix if present (e.g., "01_essen" → "Essen")
        if "_" in topic:
            topic = topic.split("_", 1)[1]
        # Capitalize first letter
        topic = topic.capitalize()
        deck_parts.append(topic)

    return "::".join(deck_parts)


def generate_deck_id(deck_name):
    """Generate a stable deck ID from the deck name"""
    import hashlib
    hash_value = int(hashlib.md5(deck_name.encode('utf-8')).hexdigest()[:8], 16)
    # Ensure it's in the valid range
    return (hash_value % (1 << 31 - 1 << 30)) + (1 << 30)


def read_csv_file(csv_path):
    """Read CSV file and return rows"""
    rows = []
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
    except Exception as e:
        print(f"Error reading {csv_path}: {e}")
    return rows


def create_vocabulary_notes(csv_path):
    """Create Anki notes from vocabulary CSV"""
    notes = []
    rows = read_csv_file(csv_path)

    if not rows:
        return notes

    # Skip header row
    for row in rows[1:]:
        if len(row) >= 2 and row[0].strip() and row[1].strip():
            english = row[0].strip()
            deutsch = row[1].strip()

            # Create note with German on front, English on back
            note = genanki.Note(
                model=vocabulary_model,
                fields=[deutsch, english]
            )
            notes.append(note)

    return notes


def create_grammar_notes(csv_path):
    """Create Anki notes from grammar exercise CSV"""
    notes = []
    rows = read_csv_file(csv_path)

    if not rows:
        return notes

    # Skip header row
    for row in rows[1:]:
        if len(row) >= 2 and row[0].strip() and row[1].strip():
            frage = row[0].strip()
            antwort = row[1].strip()

            note = genanki.Note(
                model=grammar_model,
                fields=[frage, antwort]
            )
            notes.append(note)

    return notes


def find_csv_files(base_dir, subdirs):
    """Find all CSV files in specified subdirectories, excluding _site directory"""
    csv_files = []

    for subdir in subdirs:
        subdir_path = os.path.join(base_dir, subdir)
        if not os.path.exists(subdir_path):
            continue

        for root, dirs, files in os.walk(subdir_path):
            # Skip _site directory
            if '_site' in root:
                continue

            for file in files:
                if file.endswith('.csv'):
                    csv_path = os.path.join(root, file)
                    csv_files.append((subdir, csv_path))

    return csv_files


def main():
    """Main function to create Anki deck"""
    # Get the parent directory (repo root) since script is in scripts/ folder
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)

    print("🎴 Anki Deck Generator für Deutsch C1")
    print("=" * 50)

    # Dictionary to store decks by name
    decks = {}

    # Find all CSV files
    csv_files = find_csv_files(base_dir, ['vokabular', 'grammatik'])

    if not csv_files:
        print("❌ Keine CSV-Dateien gefunden!")
        return

    print(f"\n📁 {len(csv_files)} CSV-Datei(en) gefunden\n")

    # Process each CSV file
    for category, csv_path in csv_files:
        # Generate deck name
        deck_name = get_deck_name_from_path(base_dir, csv_path)

        # Skip intermediate files (like vokabeln_de.csv)
        if '_de.csv' in csv_path:
            continue

        # Create or get deck
        if deck_name not in decks:
            deck_id = generate_deck_id(deck_name)
            decks[deck_name] = genanki.Deck(deck_id, deck_name)
            print(f"📚 Erstelle Deck: {deck_name}")

        deck = decks[deck_name]

        # Create notes based on category
        if category == 'vokabular' and 'vokabeln.csv' in csv_path:
            notes = create_vocabulary_notes(csv_path)
            note_type = "Vokabeln"
        elif category == 'grammatik' and 'aufgaben.csv' in csv_path:
            notes = create_grammar_notes(csv_path)
            note_type = "Aufgaben"
        else:
            continue

        # Add notes to deck
        for note in notes:
            deck.add_note(note)

        print(f"   ✅ {len(notes)} {note_type} hinzugefügt aus {os.path.basename(csv_path)}")

    if not decks:
        print("❌ Keine Karten erstellt!")
        return

    # Create package with all decks
    print("\n📦 Erstelle Anki-Paket...")
    package = genanki.Package(list(decks.values()))

    # Write to file in static/downloads directory
    output_dir = os.path.join(base_dir, 'static', 'downloads')
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'Deutsch_C1.apkg')
    package.write_to_file(output_file)

    # Count total cards
    total_cards = sum(len(deck.notes) for deck in decks.values())

    print(f"\n✅ Erfolgreich erstellt!")
    print(f"📊 Statistiken:")
    print(f"   - Decks: {len(decks)}")
    print(f"   - Karten: {total_cards}")
    print(f"   - Datei: {output_file}")
    print(f"\n💡 Importiere die Datei in Anki: File → Import → {output_file}")


if __name__ == '__main__':
    main()
