# Build-Befehle

```bash
# Universell (Windows/macOS/Linux): normales PDF
latexmk -r config/latexmkrc -pdf main.tex

# Universell (Windows/macOS/Linux): Stresstest-PDF
latexmk -r config/latexmkrc -pdf main-stresstest.tex
```

In VS Code (LaTeX Workshop) sind die Recipes **"latex"** und **"latex stress"** hinterlegt.
In VS Code (LaTeX Workshop) gibt es zusätzlich **"latex clear"**.
