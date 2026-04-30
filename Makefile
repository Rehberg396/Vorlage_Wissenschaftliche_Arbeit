MAIN := main.tex
MAIN_BASENAME := $(basename $(MAIN))
STRESS_MAIN := main-stresstest.tex
STRESS_BASENAME := $(basename $(STRESS_MAIN))

.DEFAULT_GOAL := all
.PHONY: all stress clean

all:
	latexmk -r config/latexmkrc -pdf $(MAIN) && cp build/$(MAIN_BASENAME).pdf $(MAIN_BASENAME).pdf

stress:
	latexmk -r config/latexmkrc -pdf $(STRESS_MAIN) && cp build/$(STRESS_BASENAME).pdf $(STRESS_BASENAME).pdf

clean:
	latexmk -r config/latexmkrc -C $(MAIN)
	latexmk -r config/latexmkrc -C $(STRESS_MAIN)
	rm -rf build $(MAIN_BASENAME).pdf
	rm -f $(STRESS_BASENAME).pdf
	rm -f $(MAIN_BASENAME).aux $(MAIN_BASENAME).bbl $(MAIN_BASENAME).bcf $(MAIN_BASENAME).blg \
		$(MAIN_BASENAME).fdb_latexmk $(MAIN_BASENAME).fls $(MAIN_BASENAME).lof $(MAIN_BASENAME).log \
		$(MAIN_BASENAME).lol $(MAIN_BASENAME).lot $(MAIN_BASENAME).out $(MAIN_BASENAME).run.xml \
		$(MAIN_BASENAME).toc $(MAIN_BASENAME).synctex.gz
	rm -f $(STRESS_BASENAME).aux $(STRESS_BASENAME).bbl $(STRESS_BASENAME).bcf $(STRESS_BASENAME).blg \
		$(STRESS_BASENAME).fdb_latexmk $(STRESS_BASENAME).fls $(STRESS_BASENAME).lof $(STRESS_BASENAME).log \
		$(STRESS_BASENAME).lol $(STRESS_BASENAME).lot $(STRESS_BASENAME).out $(STRESS_BASENAME).run.xml \
		$(STRESS_BASENAME).toc $(STRESS_BASENAME).synctex.gz
