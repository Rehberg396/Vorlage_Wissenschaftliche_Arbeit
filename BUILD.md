# Build-Befehle

```bash
# Universell (Windows/macOS/Linux): normales PDF
latexmk -r config/latexmkrc -pdf main.tex

# Universell (Windows/macOS/Linux): Stresstest-PDF
latexmk -r config/latexmkrc -pdf main-stresstest.tex

# Clean normal
latexmk -r config/latexmkrc -C main.tex

# Clean Stresstest
latexmk -r config/latexmkrc -C main-stresstest.tex
```

In VS Code (LaTeX Workshop) sind die Recipes **"latex"** und **"latex stress"** hinterlegt.
In VS Code (LaTeX Workshop) gibt es zusätzlich **"latex clear"**.
