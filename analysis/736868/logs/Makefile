

DATA := $(wildcard *.data)

JSONS=$(patsubst %.data,%.json, ${DATA})

MARKDOWNS=$(patsubst %.data,%.markdown, ${DATA})

MODEL=523

all: ${JSONS} ${MARKDOWNS}

clean:
	rm -f ${JSONS} ${MARKDOWNS}

ReadGlucose%.markdown: ReadGlucose%.data
	mm-decode-history-page.py --data glucose --model ${MODEL} $< | tee $@

ReadGlucose%.json: ReadGlucose%.data
	echo $@ $<
	mm-decode-history-page.py --collate --out $@ --data glucose --model ${MODEL} $<

ReadHistoryData%.markdown: ReadHistoryData%.data
	echo $@ $<
	mm-decode-history-page.py  --model ${MODEL} $< | tee $@

ReadHistoryData%.json: ReadHistoryData%.data
	echo $@ $<
	mm-decode-history-page.py --collate --out $@  --model ${MODEL} $<
