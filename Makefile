PROJECT_NAME=upcgm
PDF_NAME=$(PROJECT_NAME).pdf

LATEXCMD = pdflatex -shell-escape -output-directory build/
export TEXINPUTS=.:content/tex/:
export max_print_line = 1048576

help:
	@echo "This makefile builds $(PROJECT_NAME)."
	@echo ""
	@echo "Available commands are:"
	@echo "	make fast		- to build $(PROJECT_NAME), quickly (only runs LaTeX once)"
	@echo "	make $(PROJECT_NAME)              - to build $(PROJECT_NAME)"
	@echo "	make clean		- to clean up the build process"
	@echo "	make veryclean		- to clean up and remove $(PDF_NAME)"
	@echo "	make test		- to run all the stress tests in stress-tests/"
	@echo "	make test-compiles	- to test compiling all headers"
	@echo "	make help		- to show this information"
	@echo "	make showexcluded	- to show files that are not included in the doc"
	@echo ""
	@echo "For more information see the file 'doc/README'"

fast: | build
	$(LATEXCMD) content/$(PROJECT_NAME).tex </dev/null
	cp build/$(PDF_NAME) $(PDF_NAME)



$(PROJECT_NAME): test-session.pdf | build
	$(LATEXCMD) content/$(PROJECT_NAME).tex && $(LATEXCMD) content/$(PROJECT_NAME).tex
	cp build/${PDF_NAME} ${PDF_NAME}

clean:
	cd build && rm -f $(PROJECT_NAME).aux $(PROJECT_NAME).log $(PROJECT_NAME).tmp $(PROJECT_NAME).toc $(PROJECT_NAME).pdf $(PROJECT_NAME).ptc

veryclean: clean
	rm -f $(PDF_NAME) test-session.pdf

.PHONY: help fast $(PROJECT_NAME) clean veryclean

build:
	mkdir -p build/

test:
	./doc/scripts/run-all.sh .

test-compiles:
	./doc/scripts/compile-all.sh .

test-session.pdf: content/test-session/test-session.tex content/test-session/chapter.tex | build
	$(LATEXCMD) content/test-session/test-session.tex
	cp build/test-session.pdf test-session.pdf

showexcluded: build
	grep -RoPh '^\s*\\kactlimport{\K.*' content/ | sed 's/.$$//' > build/headers_included
	find ./content -name "*.h" -o -name "*.py" -o -name "*.java" | grep -vFf build/headers_included
