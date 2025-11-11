# Sprach Assistent
Deine Aufgabe ist es, eine aufbauende Lernplattform zu erstellen, um mir zu helfen, ein C1-Zertifikat in der deutschen Sprache zu erhalten.

## Projekt Übersicht

Dieses Projekt ist eine **Jekyll-basierte GitHub Pages Website** mit:
- Thematisch organisierte Vokabellisten (Deutsch-Englisch)
- Grammatikerklärungen mit Übungen
- Anki-Deck Export aller Inhalte
- Custom Styling mit Tabs und Blog-Layout

## Vokabular

### Ordnerstruktur
Vokabeln sind in **nummerierten Themenordnern** organisiert:
```
vokabular/
├── index.md                    # Übersichtsseite aller Themen
├── 01_essen/
│   ├── index.md               # Themen-Landingpage (Vokabelliste)
│   ├── vokabeln_de.csv        # Nur deutsche Wörter (Input)
│   └── vokabeln.csv           # Deutsch-Englisch (Output, für Anki)
├── 02_reisen/
│   ├── index.md
│   ├── vokabeln_de.csv
│   └── vokabeln.csv
└── 03_arbeit/
    └── ...
```

### Workflow: Neues Vokabel-Thema erstellen

1. **Ordner erstellen** (mit Nummer!):
   ```bash
   mkdir -p vokabular/02_thema
   ```

2. **Deutsche Vokabeln schreiben** (`vokabeln_de.csv`):
   - Eine Kolonne, nur deutsche Wörter
   - Keine Header-Zeile nötig
   - Ein Wort pro Zeile
   ```csv
   die Gabel
   das Messer
   der Löffel
   ```

3. **Übersetzen mit MCP Tool**:
   ```
   mcp__translate__translate_csv
   input: vokabular/02_thema/vokabeln_de.csv
   output: vokabular/02_thema/vokabeln.csv
   source_language: de
   target_language: en
   ```

4. **Index-Seite erstellen** (`index.md`):
   - Vokabeltabelle mit deutscher und englischer Spalte
   - YAML Front Matter für Jekyll
   - Kategorisierung der Wörter (z.B. nach Wortart, Unterthema)
   - Download-Link zur CSV-Datei
   - Link zurück zur Vokabular-Übersicht

5. **Vokabular-Index aktualisieren** (`vokabular/index.md`):
   - Neues Thema zur Liste hinzufügen
   - Beschreibung und Anzahl Vokabeln angeben
   - Download-Link zur CSV-Datei

6. **Haupt-Index aktualisieren** (`index.md`):
   - Neues Thema in der Tab-Ansicht "Vokabular" hinzufügen

### CSV-Format für Vokabeln

**Input** (`vokabeln_de.csv`):
```csv
deutsch
die Gabel
das Messer
der Löffel
```

**Output nach Translation** (`vokabeln.csv`):
Verwende das MCP tool `translate` für diese Arbeit.
```csv
deutsch_translated,deutsch
fork,die Gabel
knife,das Messer
spoon,der Löffel
```

## Grammatik

### Ordnerstruktur
Grammatikthemen sind in **nummerierten Unterordnern** organisiert:
```
grammatik/
├── index.md                              # Übersichtsseite aller Themen
├── 01_vergangenheitsformen/
│   ├── erklaerung.md                     # Grammatikerklärung (Website-Content)
│   └── aufgaben.csv                      # Übungen (für Anki)
├── 02_konjunktiv/
│   ├── erklaerung.md
│   └── aufgaben.csv
└── 03_passiv/
    └── ...
```

### Workflow: Neues Grammatik-Thema erstellen

1. **Ordner erstellen** (mit Nummer!):
   ```bash
   mkdir -p grammatik/02_thema
   ```

2. **Recherche durchführen**:
   - WebSearch oder WebFetch verwenden
   - Seriöse deutsche Grammatik-Quellen nutzen
   - Informationen für C1-Niveau sammeln

3. **Erklärung schreiben** (`erklaerung.md`):
   - YAML Front Matter für Jekyll hinzufügen
   - Klare Regelerklärungen
   - Viele Beispielsätze
   - Ausnahmen und Besonderheiten dokumentieren
   - Strukturierung mit Markdown Headers
   - Link zurück zur Grammatik-Übersicht

4. **Übungen erstellen** (`aufgaben.csv`):
   - Kolonne 1: Frage/Aufgabenstellung
   - Kolonne 2: Korrekte Antwort
   - Mindestens 10-15 Übungen pro Thema
   - Verschiedene Schwierigkeitsgrade

5. **Grammatik-Index aktualisieren** (`grammatik/index.md`):
   - Neues Thema zur Liste hinzufügen
   - Kurzbeschreibung und Niveau angeben
   - Links zu Erklärung und Übungs-CSV

6. **Haupt-Index aktualisieren** (`index.md`):
   - Neues Thema in der Tab-Ansicht "Grammatik" hinzufügen

### CSV-Format für Aufgaben

**Format** (`aufgaben.csv`):
```csv
Frage,Antwort
"Bilde das Perfekt: ich (gehen)","ich bin gegangen"
"Bilde das Perfekt: du (essen)","du hast gegessen"
"Welches Hilfsverb? Er ___ gekommen (sein/haben)","ist"
```

**Wichtig**:
- Header-Zeile: `Frage,Antwort`
- Anführungszeichen verwenden, wenn Kommas im Text vorkommen
- Klare, eindeutige Aufgabenstellungen
- Präzise, korrekte Antworten

## Anki Deck Generierung

### Automatische Deck-Erstellung
Es gibt ein Python-Script, das alle CSV-Dateien scannt und ein hierarchisches Anki-Deck erstellt:

```bash
cd scripts
uv run --with genanki create_anki_deck.py
```

**Output**: `static/downloads/Deutsch_C1.apkg`

### Deck-Struktur
```
Deutsch C1
├── Vokabular
│   ├── 01. Essen
│   ├── 02. Reisen
│   └── ...
└── Grammatik
    ├── 01. Vergangenheitsformen
    ├── 02. Konjunktiv
    └── ...
```

### Wann Deck neu generieren?
- Nach Hinzufügen neuer Vokabel-Themen
- Nach Erstellen neuer Grammatik-Übungen
- Nach Updates an bestehenden CSV-Dateien
- Vor größeren Commits/Releases

## Jekyll Website

### Lokales Testen
```bash
bundle install
bundle exec jekyll serve
```
Dann öffnen: `http://localhost:4000`

### Wichtige Dateien
- `index.md` - Hauptseite mit Tabs (Grammatik, Vokabular, Info)
- `_config.yml` - Jekyll-Konfiguration (Minima Theme)
- `vokabular/index.md` - Vokabular-Übersichtsseite
- `grammatik/index.md` - Grammatik-Übersichtsseite

### Styling
Custom CSS ist direkt in `index.md` eingebettet (in `<style>`-Tags am Anfang). Bei Änderungen am Design dort anpassen.

## Nummerierung von Themen

**Wichtig**: Alle Themen werden mit Nummern-Präfix erstellt:
- `01_essen`, `02_reisen`, `03_arbeit` usw.
- `01_vergangenheitsformen`, `02_konjunktiv`, `03_passiv` usw.

Dies stellt sicher:
- Konsistente Sortierung
- Klare Reihenfolge beim Lernen
- Einfache Navigation auf der Website

## Zusammenfassung

### Bei neuen Vokabel-Themen
1. Nummerierten Ordner erstellen
2. `vokabeln_de.csv` mit deutschen Wörtern schreiben
3. Mit MCP-Tool übersetzen → `vokabeln.csv`
4. `index.md` für das Thema erstellen
5. `vokabular/index.md` und Haupt-`index.md` aktualisieren
6. Anki-Deck neu generieren

### Bei neuen Grammatik-Themen
1. Nummerierten Ordner erstellen
2. Recherche durchführen (WebSearch/WebFetch)
3. `erklaerung.md` schreiben
4. `aufgaben.csv` mit Übungen erstellen
5. `grammatik/index.md` und Haupt-`index.md` aktualisieren
6. Anki-Deck neu generieren