#!/bin/bash

mm-pretty-csv ../CareLink-Export-1427693806171.csv  |  grep Wizard |
  tr -d '"' | tr -s ' ' |
  while IFS=', ' read timestamp name details bg_units  bg_input carb_input carb_units carb_ratio sensitivity bg_target_low bg_target_high bolus_estimate correction_estimate food_estimate unabsorbed_total trash_1 trash_2 junk ; do
    if [[ -n $junk ]] ; then
      echo -n $timestamp $name ''
      # $details $bg_input $bg_units $carb_input
      export $details
      echo -n $BG_INPUT ''
      # BG_UNITS
      # export "$bg_units/$bg_input"
      export $carb_input
      export $carb_units
      export $carb_ratio
      export $sensitivity
      export $bg_target_low
      export $bg_target_high
      export $bolus_estimate
      export $correction_estimate
      export $food_estimate
      export $unabsorbed_total

      echo -n $CARB_INPUT $CARB_RATIO ''
      echo -n $INSULIN_SENSITIVITY ''
      echo -n $BG_TARGET_LOW $BG_TARGET_HIGH ''
      echo -n $BOLUS_ESTIMATE $CORRECTION_ESTIMATE $FOOD_ESTIMATE $UNABSORBED_INSULIN_TOTAL
      echo
      # echo 'xx' $carb_ratio
    fi
  done

#
# for x in ReadHistory*.json ; do cat $x |  json -a timestamp _type bg carb_input carb_ratio sensitivity bg_target_low bg_target_high bolus_estimate correction_estimate food_estimate unabsorbed_insulin_total _head _date _body ; done | grep Wiz | sort | tee wizards.tsv
#

