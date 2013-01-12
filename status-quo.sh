#!/bin/bash
# make an example of an interesting log worth sharing

export TIME="%C\n\telapsed %E\n\tuser %U\n\tsystem %S\n\tCPU %P (%Xtext+%Ddata %Mmax)k"

CMD="$*"
NAME=$0
PORT=${1-'/dev/ttyUSB0'}
SERIAL=${2-'208850'}

function run_stick ( ) {
  TIME="$TIME" time python pump/stick.py ${PORT} | tee logs/stick.log
}
function run_baseline ( ) {
  TIME="$TIME" time python pump/stick.py ${PORT} | tee logs/baseline.stick.log
}
function run_postmortem ( ) {
  TIME="$TIME" time python pump/stick.py ${PORT} | tee logs/postmortem.stick.log
}
function run_session ( ) {
  TIME="$TIME" time python pump/session.py ${PORT} ${SERIAL} | tee logs/session.log
}
function run_commands ( ) {
  TIME="$TIME" time python pump/commands.py ${PORT} ${SERIAL} | tee logs/commands.log
}

function dump_repro ( ) {
  if [[ "$NAME" = "/bin/bash" ]] ; then
    NAME='status-quo.sh'
  fi
  cat $NAME
}

function contrast_baseline_postmortem_stats ( ) {
  tail -n 13 logs/baseline.stick.log  logs/postmortem.stick.log

}

function summarize_commands ( ) {
  log=${1-'logs/commands.log'}
  echo ""
  echo -n '## commands session:finished: '
  grep -E "session:finished executing" $log | sort | uniq | wc -l
  echo ""
  echo '```'
  grep -E "session:finished executing" $log | sort | uniq
  echo '```'
  echo ""

}

function summarize_pages ( ) {
  log=${1-'logs/commands.log'}
  echo ""
  echo -n '## downloaded: '
  grep -E "session:finished.*ReadHistory" $LOG | grep "data\[1024\]" | sort | uniq | wc -l
  echo ""
  echo '```'
  grep -E "session:finished executing.*ReadHistory" $LOG | sort | uniq
  echo '```'
  echo ""

}

function explain_markdown ( ) {

  echo "# ${NAME} ${CMD}" > explain.markdown

  echo "## cat ${NAME}" >> explain.markdown
  echo '```bash'        >> explain.markdown
  cat $NAME             >> explain.markdown
  echo '```'            >> explain.markdown

  echo "## cat logs/explain.log" >> explain.markdown
  cat logs/explain.log           >> explain.markdown
}

function run_all ( ) {

  echo "## run all ${NAME} ${CMD}"
  echo $NAME
  dump_repro
  date
  run_baseline
  run_session
  run_commands
  echo "Was there an ACK ERROR?"
  echo "### DIAGNOSE CRC"
  run_postmortem
  # run_stick
}

run_all 2>&1 | tee status-quo.log

echo "OUT" | tee logs/explain.log
. ./explain-brief.sh | tee -a logs/explain.log
explain_markdown


#####
# EOF
