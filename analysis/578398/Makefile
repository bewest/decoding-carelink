

JSONS=\
ReadGlucoseHistory-page-6.json \
ReadHistoryData-page-0.json \
ReadHistoryData-page-10.json \
ReadHistoryData-page-1.json \
ReadHistoryData-page-2.json \
ReadHistoryData-page-3.json \
ReadHistoryData-page-4.json \
ReadHistoryData-page-5.json \
ReadHistoryData-page-6.json \
ReadHistoryData-page-7.json \
ReadHistoryData-page-8.json \
ReadHistoryData-page-9.json \


MARKDOWNS=\
ReadGlucoseHistory-page-6.markdown \
ReadHistoryData-page-0.markdown \
ReadHistoryData-page-10.markdown \
ReadHistoryData-page-1.markdown \
ReadHistoryData-page-2.markdown \
ReadHistoryData-page-3.markdown \
ReadHistoryData-page-4.markdown \
ReadHistoryData-page-5.markdown \
ReadHistoryData-page-6.markdown \
ReadHistoryData-page-7.markdown \
ReadHistoryData-page-8.markdown \
ReadHistoryData-page-9.markdown \

all: ${JSONS} ${MARKDOWNS}

clean:
	echo ${JSONS} ${MARKDOWNS} | xargs rm -f

ReadGlucose%.markdown: ReadGlucose%.data \
	mm-decode-history-page.py --out $@ --data glucose --model 522 $<

ReadGlucose%.json: ReadGlucose%.data
	echo $@ $<
	mm-decode-history-page.py --collate --out $@ --data glucose --model 522 $<

ReadHistoryData%.markdown: ReadHistoryData%.data
	echo $@ $<
	mm-decode-history-page.py --collate --out $@  --model 522 $<

ReadHistoryData%.json: ReadHistoryData%.data
	echo $@ $<
	mm-decode-history-page.py --collate --out $@  --model 522 $<
