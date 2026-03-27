# Squardle Solver

A complete Squaredle puzzle solver available in two versions:
1. **Web App** (SPA for GitHub Pages) - Use in your browser
2. **CLI Tool** (Python) - Run from command line with image generation

---

## 🌐 Web App (Recommended for Most Users)

An interactive Single Page Application that runs entirely in your browser.

### Quick Start

1. **Try it locally**: Open `docs/index.html` in your browser
2. **Deploy to GitHub Pages**: See [docs/README.md](docs/README.md) for deployment instructions

### Features

- ✅ Interactive 4x4 grid input with validation
- ✅ Finds all valid words (4+ letters)  
- ✅ Collapsible results grouped by word length
- ✅ Share grids via URL with family/friends
- ✅ Mobile-friendly responsive design
- ✅ No installation required

**[📖 View Web App Documentation →](docs/README.md)**

---

## 🖥️ CLI Tool (Python)

A command-line version that generates images showing word paths on the grid.

### Requirements

```bash
pip install wordfreq pillow
```

### Usage

1. Edit `input.txt` with your 4x4 grid:
   ```
   essi
   makc
   gbrg
   elyo
   ```

2. Run the solver:
   ```bash
   python main.py
   ```

3. Find results in `found_words/`:
   - Text files organized by word length
   - Images showing paths for each word

### Features

- 🔍 Finds all valid English words
- 🎨 Generates visual path images for each word
- 📁 Organizes output by word length
- ⚙️ Configurable via `config.py`

### Files

- `main.py` - Entry point
- `trie.py` - Trie data structure
- `trie_builder.py` - Build trie from word list
- `word_finder.py` - DFS algorithm to find words
- `grid_loader.py` - Parse input grid
- `image_generator.py` - Generate word path images
- `text_writer.py` - Write words to text files
- `directory_manager.py` - Manage output directory
- `config.py` - Configuration settings

### Configuration

Edit `config.py` to customize:
- `MIN_WORD_LENGTH` - Minimum word length (default: 3)
- `WORD_LIST_SIZE` - Number of words to load (default: 100,000)
- `CELL_SIZE` - Image cell size (default: 80px)
- `FONT_SIZE` - Image font size (default: 36)

---

## 🎯 Which Version Should I Use?

| Use Case | Recommended Version |
|----------|-------------------|
| Quick solve on any device | 🌐 Web App |
| Share puzzles with others | 🌐 Web App |
| No Python installed | 🌐 Web App |
| Want visual path images | 🖥️ CLI Tool |
| Batch processing | 🖥️ CLI Tool |
| Offline use | 🖥️ CLI Tool |

---

## 🧮 How It Works

Both versions use the same algorithm:

1. **Trie Data Structure** - Efficient word lookup with prefix matching
2. **DFS (Depth-First Search)** - Explore all paths through the grid
3. **8-Directional Movement** - Check all adjacent cells including diagonals
4. **Visited Tracking** - Prevent cell reuse within the same word

### Example Grid

```
e s s i
m a k c  
g b r g
e l y o
```

Finds words like: `mass`, `make`, `sake`, `gear`, `berg`, `able`, etc.

---

## 📁 Repository Structure

```
squardle/
├── docs/                      # Web app (GitHub Pages)
│   ├── index.html            # SPA - single file app
│   └── README.md             # Web deployment guide
├── *.py                      # CLI tool Python files
├── input.txt                 # Input grid for CLI
├── config.py                 # CLI configuration
├── found_words/              # CLI output directory
└── README.md                 # This file
```

---

## 📄 License

MIT License - Free to use and modify
