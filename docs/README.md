# Squardle Solver Web App

A Single Page Application (SPA) that solves Squaredle puzzles by finding all valid English words in a 4x4 letter grid.

## 🌐 Live Demo

Once deployed, your app will be available at: `https://[your-username].github.io/squardle`

## ✨ Features

- **Interactive 4x4 grid input** - Easy letter entry with auto-focus
- **Input validation** - Only accepts letters (a-z)
- **Smart word finding** - Uses Trie + DFS algorithm
- **Collapsible results** - Word groups organized by length
- **Share functionality** - Generate shareable URLs for family/friends
- **Mobile-friendly** - Responsive design that works on all devices
- **No backend required** - Runs entirely in the browser

## 🚀 Deployment to GitHub Pages

### Quick Setup

1. **Push to GitHub** (if not already done):

   ```bash
   git add .
   git commit -m "Add Squardle solver web app"
   git push origin main
   ```

2. **Enable GitHub Pages**:
   - Go to your repository on GitHub
   - Navigate to **Settings** → **Pages**
   - Under "Source", select **Deploy from a branch**
   - Choose branch: `main`
   - Choose folder: `/docs`
   - Click **Save**

3. **Access your app**:
   - Your site will be live at `https://[username].github.io/squardle`
   - May take a few minutes for first deployment

### Alternative: Direct Deployment

If you want to use the root or a different branch:

- Select `/` (root) instead of `/docs`
- Or create a `gh-pages` branch and deploy from there

## 📖 How to Use

1. **Visit** [Squaredle.app](https://squaredle.app/) and play today's puzzle
2. **Come back** only if you need help!
3. **Enter** the letters from your puzzle into the grid
4. **Click** "Find Words" to see all solutions
5. **Share** the grid with family using the Share button

## 🔗 Sharing Grids

The app supports URL parameters for easy sharing:

```
https://your-site.github.io/squardle?grid=essimakcgbrgelyo
```

Just click the "📤 Share This Grid" button to automatically copy the shareable link!

## 🛠️ Technical Details

- **Single HTML file** - No build process needed
- **Pure JavaScript** - No frameworks or dependencies
- **External word list** - Fetched from dwyl/english-words (370k+ words)
- **Client-side processing** - All solving happens in the browser
- **URL-based sharing** - Grid state encoded in URL parameters

## 📱 Browser Compatibility

Works on all modern browsers:

- ✅ Chrome/Edge (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Mobile browsers (iOS/Android)

## 🎨 Customization

To customize colors, fonts, or layout, edit the `<style>` section in `index.html`. The CSS uses:

- Purple gradient theme (`#667eea` to `#764ba2`)
- System fonts for best performance
- CSS Grid for responsive layouts

## 📝 Algorithm

The solver uses:

1. **Trie data structure** - Efficient prefix matching for word validation
2. **Depth-First Search** - Explores all valid paths through the grid
3. **8-directional movement** - Checks all adjacent cells (including diagonals)
4. **Visited tracking** - Prevents reusing cells in the same word

## 🐛 Troubleshooting

**Grid doesn't auto-load from URL?**

- Check that the URL has exactly 16 characters in the `grid` parameter
- Spaces are supported for empty cells

**Word list fails to load?**

- Requires internet connection on first use
- Check browser console for CORS or network errors

**Share button doesn't work?**

- Requires HTTPS or localhost for clipboard access
- Falls back to alert dialog if clipboard unavailable

## 📄 License

MIT License - Free to use and modify

---

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-☕%20support-yellow?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/nabeelvandayar)
