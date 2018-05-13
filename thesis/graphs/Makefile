M4_SRCS = $(shell find -name '*.dot.m4')
SRCS = $(patsubst %.dot.m4,%.dot,$(M4_SRCS))
TGTS = $(patsubst %.dot,%.pdf,$(SRCS))

.PHONY: all clean

all: $(TGTS)

%.pdf: %.dot
	dot -Tpdf $? -o $@ -Gsize

%.dot: %.dot.m4
	m4 $? > $@

clean:
	find -name '*.pdf' -delete
	find -name '*.dot' -delete
