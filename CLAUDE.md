# Sprach Assistent
Deine Aufgabe ist es eine aufbauende lernplatform zu erstellen, um mir zu helfen ein C1 Zeugniss in der Deutschen Sprache zu erhalten.

## Vokabeln
Das Repo ist aufgebaut in einen `./vokabular` Ordner, in welchem du thematisch bezogene Wörter erstellen wirst und diese ins Englische übersetzt. Für die Übersetzungen verwende das MCP Tool `translate-mcp`, welches von Deutsch auf Englisch übersetzt.

### Struktur
```
vokabular/
├── essen/
│   └── vokabeln.csv
├── reisen/
│   └── vokabeln.csv
└── arbeit/
    └── vokabeln.csv
```

### Workflow
1. **Unterordner erstellen**: `mkdir -p vokabular/<thema>`
2. **Deutsche Vokabeln schreiben**: CSV Datei mit einer Kolonne erstellen (nur deutsche Wörter)
3. **Übersetzen**: MCP translate-Tool verwenden, um das CSV zu übersetzen
4. **Resultat**: Output CSV hat zwei Kolonnen (Deutsch | Englisch)

### Beispiel
Wenn ich frage: "Erstelle Vokabeln zum Thema Essen"

**Input CSV** (`vokabular/essen/vokabeln_de.csv`):
```csv
die Gabel
das Messer
der Löffel
```

**Output CSV** (`vokabular/essen/vokabeln.csv`):
```csv
Translation,Original
fork,die Gabel
knife,das Messer
spoon,der Löffel
```

## Grammatik
Im `./grammatik` Ordner werden Grammatikregeln und Übungen gespeichert. Die Themen werden in thematisch sortierten Unterordnern organisiert.

### Struktur
```
grammatik/
├── vergangenheitsformen/
│   ├── erklaerung.md
│   └── aufgaben.csv
├── konjunktiv/
│   ├── erklaerung.md
│   └── aufgaben.csv
└── passiv/
    ├── erklaerung.md
    └── aufgaben.csv
```

### Workflow
1. **Recherche**: Online-Ressourcen zu dem Grammatikthema finden
2. **Zusammenfassung erstellen**: `erklaerung.md` Datei mit Regeln, Beispielen und Erklärungen schreiben
3. **Aufgaben erstellen**: `aufgaben.csv` mit Übungen (Kolonne 1: Frage, Kolonne 2: Antwort)

### Beispiel
**Erklärung** (`grammatik/vergangenheitsformen/erklaerung.md`):
```markdown
# Perfekt

Das Perfekt wird verwendet für abgeschlossene Handlungen in der Vergangenheit.

**Bildung**: haben/sein + Partizip II
- Ich habe gegessen
- Er ist gegangen
```

**Aufgaben** (`grammatik/vergangenheitsformen/aufgaben.csv`):
```csv
Frage,Antwort
"Bilde das Perfekt: ich (gehen)","ich bin gegangen"
"Bilde das Perfekt: du (essen)","du hast gegessen"
"Welches Hilfsverb? Er ___ gekommen (sein/haben)","ist"
```

### CSV Format für Aufgaben
- **Kolonne 1** (Frage): Die Aufgabenstellung oder Frage
- **Kolonne 2** (Antwort): Die korrekte Lösung
- Beide Kolonnen mit Anführungszeichen, wenn Kommas oder Sonderzeichen enthalten sind