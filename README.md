# Deutsch C1 Lernplattform

A personal learning platform for German language C1 certification preparation, built with GitHub Pages.

## Structure

- **vokabular/** - Thematic vocabulary lists with German-English translations
- **grammatik/** - Grammar explanations and exercises
- **assets/** - Custom styling for the blog-like layout

## About This Project

**⚠️ Important Notice:**
- This repository is primarily built using LLMs (Claude from Anthropic) and subsequently reviewed by the author
- The content is provided as-is for personal learning purposes
- **The author takes no liability for the accuracy or completeness of this learning platform**
- Always verify information with official language resources and qualified instructors

## Features

- 📚 Comprehensive grammar explanations
- 📝 Thematic vocabulary lists
- ✏️ Interactive exercises
- 📥 **Downloadable CSV files** - All vocabulary and exercise CSV files can be imported into [Anki](https://apps.ankiweb.net/), [Quizlet](https://quizlet.com/), or any other flashcard application for personalized study
- 🎨 Blog-like layout with custom styling

## Local Development

This site uses Jekyll with GitHub Pages. To run locally:

```bash
bundle install
bundle exec jekyll serve
```

Visit `http://localhost:4000`

## Adding Content

### New Vocabulary Topic

1. Create directory: `mkdir -p vokabular/<topic>`
2. Create German CSV with one column
3. Use MCP translate tool to create bilingual version
4. Create index.md with vocabulary tables

### New Grammar Topic

1. Create directory: `mkdir -p grammatik/<topic>`
2. Create `erklaerung.md` with explanations
3. Create `aufgaben.md` with exercises
4. Update `grammatik/index.md`

## Technologies

- GitHub Pages
- Jekyll (Minima theme)
- Markdown + YAML front matter
- MCP translation tools

## License

Personal educational project - all content for learning purposes.
