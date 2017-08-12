mhucka-mjgraham-arxiv-2016-05-07.pdf: whitepaper.pdf
	java -cp pdfbox/PDFBox-0.7.3.jar:pax/scripts/pax/pax.jar pax.PDFAnnotExtractor whitepaper.pdf
	pdflatex mhucka-mjgraham-arxiv-2016-05-07
	pdflatex mhucka-mjgraham-arxiv-2016-05-07

whitepaper.pdf: whitepaper.tex mike-casics-library.bib casicswhitepaper.cls
	pdflatex whitepaper
	bibtex whitepaper
	pdflatex whitepaper
	pdflatex whitepaper
	pdflatex whitepaper
