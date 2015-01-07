
# Decoding carelink

For an intro, see
[insulaudit](https://github.com/bewest/insulaudit/tree/master/questions).
We are hoping to help diabetics independently reproduce therapeutic
audits of their Medtronic insulin pumps.  This experimental software
will download pump settings, and the entire log of historical data.

## [Docs](http://bewest.github.io/decoding-carelink/)

Spot something incorrect or not working?  Want a feature/tool to do
something?
[Please file an issue!](https://github.com/bewest/decoding-carelink/issues)

* http://bewest.github.io/decoding-carelink/ Sphinx docs.
* https://gist.github.com/bewest/6330546 some diagrams

![overview](https://gist.github.com/bewest/6330546/raw/dffdb1e95ef9882e3929579784f95db8c5c6705d/overview.seq.png)

## Status

We can decode many of the opcodes that store configuration settings.
We can also download all pages of history from the ReadHistoryData
command, which contains the log of all actions the pump has taken on
your behalf:

* glucose readings
* all bolus dosings, all usage of bolus wizard
* unabsorbed insulin
* alarms, etc...
* current settings
* query pump status: normal, suspended, bolusing
  `./bin/mm-set-suspend.py`
* set/edit/query temporary basal rates
  `./bin/mm-temp-basals.py`
* press any button on the keypad, using
  `./bin/mm-press-key.py`
* Investigate how any command works, make new commands, download any command
  `./bin/mm-send-comm.py`
* Bolus
  `./bin/mm-bolus.py`

## Install first run

This only needs to be done once:

### From pypi

```bash
$ easy_install decocare
# or
$ pip install decocare
```

### From source
```bash
git clone https://github.com/bewest/decoding-carelink.git
cd decoding-carelink
sudo python ez_setup.py # only if you rarely use python
sudo python setup.py develop
```

### Contribute your logs

Fork the repo, create a new branch, send the results back to your branch.
There will be a green "create pull request button."  Putting your logs back on
github will allow more people to assist in decoding results.

```bash
git checkout -b myname/init # replace <myname> with your name
# all done
```
#### Find/Create serial device in the OS

Congratulations, now you are ready for the demo:
Plug in the carelink usb stick, and run this:
```bash
dmesg | grep ttyUSB # notice the new ttyUSB$x
sudo ./insert.sh
```

You are all done with setup.
Here's how to test just the usb stick, then we'll run the full suite of
experiments.

* on **MAC** the `PORT` is called `/dev/tty.serial` or something.
* on **windows** the `PORT` is called `COM1` or something
* on **Linux** the `PORT` is called `/dev/ttyUSBx` or something

### Get your logs
```bash
python decocare/stick.py /dev/ttyUSB0 # on windows this is called COM1
# should get a bunch of output, notably some counters called INTERFACE STATS

export SERIAL=208850
# Turn RF POWER ON for 10 minutes
# You have ten minutes to talk with the pump.
# should say hello, and print serial number
mm-send-comm.py --init sleep 0
# print serial number
mm-send-comm.py sleep 0
# get logs
mm-latest.py 

```

Fantastic.
Send me your results!  The following process uses git to store your
recent results.  You can email me a bundle, or simply push your branch
back to your fork on github.

Do this every time, after you run some experiments:
```bash
git commit -avm 'for @bewest, these are @<my-name> results'
```

Set up for sending me results.
```bash
# email me your results like this:
git bundle create myname-expr.bundle master..myname/init
# you can send me myname-expr.bundle in an email
```

Even better, [fork the repo](https://github.com/bewest/decoding-carelink/fork)
and setup to for easy.
```bash
# add your fork like this:
git remote rename origin author
git remote add origin git@github.com:<my-user-name>/decoding-carelink.git
git push -u origin myname/init
```


Now you can do this easily:
```bash
./status-quo.sh /dev/ttyUSB0 <pump-serial> # use your pump's serial number
git commit -avm 'for @bewest, these are @<my-name> results'
git push -u origin myname/init
```

Repeat.  The easiest way to see what happened is to look at
explain.log, and use `git diff` and `git show`.  Pushing to github as
shown above will allow everyone to discuss our analysis together.

There are several log files created for each experiment.


## Demo

> If you don't want to use your own equipment, I've made some of my
> test equipment available.
Talk to my test insulin pump over the internet.

Requires `socat` and `python 2.7`.  The script [`./bin/socat_run_app.sh`](https://github.com/bewest/decoding-carelink/blob/master/bin/socat_run_app.sh)
will connect to my server, `bewest.io:8080` where my test insulin
pump, serial `208850` is waiting to talk to you.

Here's an example using my scripts:

```bash
$ git checkout -b tester # create a new branch with just your stuff, please
$ . ./bin/common # import some handy run_* functions
$ ./bin/socat_run_app.sh & # get my test insulin pump from bewest.io:8080
$ ls carelink.ttyUSB0  # creates this thing
carelink.ttyUSB0
$ ./status-quo.sh ./carelink.ttyUSB0
[...]
$ PORT=./carelink.ttyUSB0 SERIAL=208850 run_download 
[...]

```
* [download](https://raw.github.com/bewest/decoding-carelink/tester/logs/download.log)
* [commands](https://github.com/bewest/decoding-carelink/blob/tester/logs/commands.log)

Try figuring out the dosing commands.  Is it possible to rewind
the pump?  Is it possible to enter new profiles and schedules?

## Future work

* collect more data
* finish [analyzing pages of insulin pump history](https://github.com/bewest/decoding-carelink/blob/rewriting/analysis/pages.markdown)
* https://github.com/bewest/decoding-carelink/tree/rewriting/analysis/pages
** [analyze insulin pump bolus records](https://github.com/bewest/decoding-carelink/blob/rewriting/analysis/bolus.markdown)
** [help analyze prime events](https://github.com/bewest/decoding-carelink/blob/rewriting/ground-start-0/decoding-prime-events.markdown)
** [help analyze pump midnight events](https://github.com/bewest/decoding-carelink/tree/rewriting/basal-hist-2006)

Once we can decode historical logs, we'll clean up and merge back into
[insulaudit](https://github.com/bewest/insulaudit/tree/master/hacking)

### Help needed

Documentation of protocol, decoders, etc...

```bash
# fork the repo on github
# clone the repo
$ git clone git@github.com/<yourname>/decoding-carelink.git
$ cd decoding-carelink
$ git checkout -b <yourname>
$ ./insert.sh # will ask for sudo to configure usbserial for the stick
# ./status-quo.sh [[<path>|/dev/ttyUSB0>] [<serial>|208850]] eg:
$ ./status-quo.sh /dev/ttyUSB0 208850
$ git commit -avm "here is my data <yourname>"
$ git push -u origin <yourname>
```
Thanks!
If you can include CSV export from carelink, it would be helpful.

### Decoding

We know how to
[decode time](https://github.com/bewest/decoding-carelink/blob/master/new-years-day/rollover-month/stage-5.markdown)
and as a result we can find and parse most records now.

And lining this up with the Carelink CSV exports reveals the nature of
the contents for further analysis.

Once we can decode all records, it should be useful for
diabetics, to get basic reports, more or less on par with the
vendor's solution.
We'll use it to 
[collect diabetes data](https://github.com/bewest/insulaudit/tree/master/hacking)
(https://github.com/bewest/decoding-carelink/tree/rewriting/analysis/pages)
over the internet, allowing anyone to independently audit their
therapy, and then send the data to their preferred auditing software.

## Tools
### `./bin/mm-bolus.py`
```
+ ./bin/mm-bolus.py --help
usage: mm-bolus.py [-h] [--serial SERIAL] [--port PORT] [--no-op]
                   [--skip-prelude] [--no-rf-prelude] [--skip-postlude] [-v]
                   [--init] (--515 | --strokes STROKES_PER_UNIT)
                   units

mm-bolus.py - Send bolus command to a pump.

positional arguments:
  units                 Amount of insulin to bolus.

optional arguments:
  -h, --help            show this help message and exit
  --serial SERIAL       serial number of pump [default: ]
  --port PORT           Path to device [default: ]
  --no-op               Dry run, don't do main function
  --skip-prelude        Don't do the normal prelude.
  --no-rf-prelude       Do the prelude, but don't query the pump.
  --skip-postlude       Don't do the normal postlude.
  -v, --verbose         Verbosity
  --init                Send power ctrl to initialize RF session.
  --515
  --strokes STROKES_PER_UNIT

XXX: Be careful please! Units might be wrong. Keep disconnected from pump
until you trust it by observing the right amount first.
+ ./bin/mm-bolus.py
usage: mm-bolus.py [-h] [--serial SERIAL] [--port PORT] [--no-op]
                   [--skip-prelude] [--no-rf-prelude] [--skip-postlude] [-v]
                   [--init] (--515 | --strokes STROKES_PER_UNIT)
                   units
mm-bolus.py: error: too few arguments


+ ./bin/mm-bolus.py --515
usage: mm-bolus.py [-h] [--serial SERIAL] [--port PORT] [--no-op]
                   [--skip-prelude] [--no-rf-prelude] [--skip-postlude] [-v]
                   [--init] (--515 | --strokes STROKES_PER_UNIT)
                   units
mm-bolus.py: error: too few arguments


+ ./bin/mm-bolus.py --strokes 10
usage: mm-bolus.py [-h] [--serial SERIAL] [--port PORT] [--no-op]
                   [--skip-prelude] [--no-rf-prelude] [--skip-postlude] [-v]
                   [--init] (--515 | --strokes STROKES_PER_UNIT)
                   units
mm-bolus.py: error: too few arguments
```

### `./bin/mm-send-comm.py`

##### `mm-send-comm.py -h`
```
+ mm-send-comm.py -h
usage: mm-send-comm.py [-h] [--serial SERIAL] [--port PORT] [--no-op]
                       [--skip-prelude] [--no-rf-prelude] [--skip-postlude]
                       [-v] [--init] [--prefix-path PREFIX_PATH] [--saveall]
                       [--prefix
                       {BaseCommand, KeypadPush, PowerControl, PowerControlOff,
                       PumpCommand, PumpResume, PumpSuspend, ReadBasalTemp,
                       ReadBatteryStatus, ReadContrast, ReadCurPageNumber,
                       ReadErrorStatus, ReadFirmwareVersion,
                       ReadGlucoseHistory, ReadHistoryData, ReadPumpID,
                       ReadPumpModel, ReadPumpState, ReadPumpStatus, ReadRTC,
                       ReadRadioCtrlACL, ReadRemainingInsulin, ReadSettings,
                       ReadTotalsToday, SetSuspend, PushEASY, PushUP, PushDOWN,
                       PushACT, PushESC, TempBasal, ManualCommand,
                       ReadCurGlucosePageNumber, ReadErrorStatus508,
                       ReadBolusHistory, ReadDailyTotals, ReadPrimeBoluses,
                       ReadAlarms, ReadProfileSets, ReadUserEvents,
                       ReadRemoteControlID, Read128KMem, Read256KMem,
                       ReadBasalTemp508, ReadTodayTotals508,
                       ReadSensorSettings, ReadSensorHistoryData,
                       ReadISIGHistory, FilterHistory, FilterGlucoseHistory,
                       FilterISIGHistory, ReadProfiles511_STD,
                       ReadProfiles511_A, ReadProfiles511_B,
                       Model511_ExperimentOP125, Model511_ExperimentOP126,
                       ReadSettings511, ReadPumpTrace, ReadDetailTrace,
                       Model511_Experiment_OP165, ReadNewTraceAlarm,
                       ReadOldTraceAlarm, WriteGlucoseHistoryTimestamp,
                       ReadLanguage, ReadBolusWizardSetupStatus, ReadCarbUnits,
                       ReadBGUnits, ReadCarbRatios, ReadInsulinSensitivities,
                       ReadBGTargets, ReadBGAlarmCLocks, ReadReservoirWarning,
                       ReadBGReminderEnable, ReadSettings512,
                       ReadProfile_STD512, ReadProfile_A512, ReadProfile_B512,
                       ReadLogicLinkIDS, Model512Experiment_OP150,
                       ReadBGAlarmEnable, GuardianSensorSettings,
                       GuardianSensorSettings, GuardianSensorDemoGraphTimeout,
                       GuardianSensorAlarmSilence,
                       GuardianSensorRateChangeAlerts, ReadSavedSettingsDate,
                       ReadBolusReminderEnable, ReadBolusReminders,
                       ReadFactoryParameters, ReadCalibrationFactor,
                       ReadVCNTRHistory, ReadOtherDevicesIDS, PumpTraceSelect,
                       PumpEnableDetailTrace, PumpDisableDetailTrace,
                       Experiment_OP161, Experiment_OP162,
                       Model511_Experiment_OP119, Model511_Experiment_OP120,
                       Model511_Experiment_OP121, Model511_Experiment_OP122,
                       Model511_Experiment_OP123, Model511_Experiment_OP124,
                       Model511_Experiment_OP125, Model511_Experiment_OP126,
                       Model511_Experiment_OP127, Model511_Experiment_OP128,
                       Model511_Experiment_OP129, Model511_Experiment_OP130,
                       SelectBasalProfile, SelectBasalProfileSTD,
                       SelectBasalProfileA, SelectBasalProfileB,
                       PumpExperiment_OP69, PumpExperiment_OP70,
                       PumpExperiment_OP71, PumpExperiment_OP72,
                       PumpExperiment_OP73, PumpExperiment_OP75}]
                       [--postfix {BaseCommand, KeypadPush, PowerControl,
                       PowerControlOff, PumpCommand, PumpResume, PumpSuspend,
                       ReadBasalTemp, ReadBatteryStatus, ReadContrast,
                       ReadCurPageNumber, ReadErrorStatus, ReadFirmwareVersion,
                       ReadGlucoseHistory, ReadHistoryData, ReadPumpID,
                       ReadPumpModel, ReadPumpState, ReadPumpStatus, ReadRTC,
                       ReadRadioCtrlACL, ReadRemainingInsulin, ReadSettings,
                       ReadTotalsToday, SetSuspend, PushEASY, PushUP, PushDOWN,
                       PushACT, PushESC, TempBasal, ManualCommand,
                       ReadCurGlucosePageNumber, ReadErrorStatus508,
                       ReadBolusHistory, ReadDailyTotals, ReadPrimeBoluses,
                       ReadAlarms, ReadProfileSets, ReadUserEvents,
                       ReadRemoteControlID, Read128KMem, Read256KMem,
                       ReadBasalTemp508, ReadTodayTotals508,
                       ReadSensorSettings, ReadSensorHistoryData,
                       ReadISIGHistory, FilterHistory, FilterGlucoseHistory,
                       FilterISIGHistory, ReadProfiles511_STD,
                       ReadProfiles511_A, ReadProfiles511_B,
                       Model511_ExperimentOP125, Model511_ExperimentOP126,
                       ReadSettings511, ReadPumpTrace, ReadDetailTrace,
                       Model511_Experiment_OP165, ReadNewTraceAlarm,
                       ReadOldTraceAlarm, WriteGlucoseHistoryTimestamp,
                       ReadLanguage, ReadBolusWizardSetupStatus, ReadCarbUnits,
                       ReadBGUnits, ReadCarbRatios, ReadInsulinSensitivities,
                       ReadBGTargets, ReadBGAlarmCLocks, ReadReservoirWarning,
                       ReadBGReminderEnable, ReadSettings512,
                       ReadProfile_STD512, ReadProfile_A512, ReadProfile_B512,
                       ReadLogicLinkIDS, Model512Experiment_OP150,
                       ReadBGAlarmEnable, GuardianSensorSettings,
                       GuardianSensorSettings, GuardianSensorDemoGraphTimeout,
                       GuardianSensorAlarmSilence,
                       GuardianSensorRateChangeAlerts, ReadSavedSettingsDate,
                       ReadBolusReminderEnable, ReadBolusReminders,
                       ReadFactoryParameters, ReadCalibrationFactor,
                       ReadVCNTRHistory, ReadOtherDevicesIDS, PumpTraceSelect,
                       PumpEnableDetailTrace, PumpDisableDetailTrace,
                       Experiment_OP161, Experiment_OP162,
                       Model511_Experiment_OP119, Model511_Experiment_OP120,
                       Model511_Experiment_OP121, Model511_Experiment_OP122,
                       Model511_Experiment_OP123, Model511_Experiment_OP124,
                       Model511_Experiment_OP125, Model511_Experiment_OP126,
                       Model511_Experiment_OP127, Model511_Experiment_OP128,
                       Model511_Experiment_OP129, Model511_Experiment_OP130,
                       SelectBasalProfile, SelectBasalProfileSTD,
                       SelectBasalProfileA, SelectBasalProfileB,
                       PumpExperiment_OP69, PumpExperiment_OP70,
                       PumpExperiment_OP71, PumpExperiment_OP72,
                       PumpExperiment_OP73, PumpExperiment_OP75}]
                       {sleep,tweak,ManualCommand} ...

mm-send-comm.py - send messages to a compatible MM insulin pump

positional arguments:
  {sleep,tweak,ManualCommand}
                        Main thing to do between --prefix and--postfix
    sleep               Just sleep between command sets
    tweak               Tweak a builtin command
    ManualCommand       Customize a command

optional arguments:
  -h, --help            show this help message and exit
  --serial SERIAL       serial number of pump [default: ]
  --port PORT           Path to device [default: ]
  --no-op               Dry run, don't do main function
  --skip-prelude        Don't do the normal prelude.
  --no-rf-prelude       Do the prelude, but don't query the pump.
  --skip-postlude       Don't do the normal postlude.
  -v, --verbose         Verbosity
  --init                Send power ctrl to initialize RF session.
  --prefix-path PREFIX_PATH
                        Prefix to store saved files when using --save or
                        --saveall.
  --saveall             Whether or not to save all responses.
  --prefix {BaseCommand, KeypadPush, PowerControl, PowerControlOff,
  PumpCommand, PumpResume, PumpSuspend, ReadBasalTemp, ReadBatteryStatus,
  ReadContrast, ReadCurPageNumber, ReadErrorStatus, ReadFirmwareVersion,
  ReadGlucoseHistory, ReadHistoryData, ReadPumpID, ReadPumpModel,
  ReadPumpState, ReadPumpStatus, ReadRTC, ReadRadioCtrlACL,
  ReadRemainingInsulin, ReadSettings, ReadTotalsToday, SetSuspend, PushEASY,
  PushUP, PushDOWN, PushACT, PushESC, TempBasal, ManualCommand,
  ReadCurGlucosePageNumber, ReadErrorStatus508, ReadBolusHistory,
  ReadDailyTotals, ReadPrimeBoluses, ReadAlarms, ReadProfileSets,
  ReadUserEvents, ReadRemoteControlID, Read128KMem, Read256KMem,
  ReadBasalTemp508, ReadTodayTotals508, ReadSensorSettings,
  ReadSensorHistoryData, ReadISIGHistory, FilterHistory, FilterGlucoseHistory,
  FilterISIGHistory, ReadProfiles511_STD, ReadProfiles511_A, ReadProfiles511_B,
  Model511_ExperimentOP125, Model511_ExperimentOP126, ReadSettings511,
  ReadPumpTrace, ReadDetailTrace, Model511_Experiment_OP165, ReadNewTraceAlarm,
  ReadOldTraceAlarm, WriteGlucoseHistoryTimestamp, ReadLanguage,
  ReadBolusWizardSetupStatus, ReadCarbUnits, ReadBGUnits, ReadCarbRatios,
  ReadInsulinSensitivities, ReadBGTargets, ReadBGAlarmCLocks,
  ReadReservoirWarning, ReadBGReminderEnable, ReadSettings512,
  ReadProfile_STD512, ReadProfile_A512, ReadProfile_B512, ReadLogicLinkIDS,
  Model512Experiment_OP150, ReadBGAlarmEnable, GuardianSensorSettings,
  GuardianSensorSettings, GuardianSensorDemoGraphTimeout,
  GuardianSensorAlarmSilence, GuardianSensorRateChangeAlerts,
  ReadSavedSettingsDate, ReadBolusReminderEnable, ReadBolusReminders,
  ReadFactoryParameters, ReadCalibrationFactor, ReadVCNTRHistory,
  ReadOtherDevicesIDS, PumpTraceSelect, PumpEnableDetailTrace,
  PumpDisableDetailTrace, Experiment_OP161, Experiment_OP162,
  Model511_Experiment_OP119, Model511_Experiment_OP120,
  Model511_Experiment_OP121, Model511_Experiment_OP122,
  Model511_Experiment_OP123, Model511_Experiment_OP124,
  Model511_Experiment_OP125, Model511_Experiment_OP126,
  Model511_Experiment_OP127, Model511_Experiment_OP128,
  Model511_Experiment_OP129, Model511_Experiment_OP130, SelectBasalProfile,
  SelectBasalProfileSTD, SelectBasalProfileA, SelectBasalProfileB,
  PumpExperiment_OP69, PumpExperiment_OP70, PumpExperiment_OP71,
  PumpExperiment_OP72, PumpExperiment_OP73, PumpExperiment_OP75}
                        Built-in commands to run before the main one.
  --postfix {BaseCommand, KeypadPush, PowerControl, PowerControlOff,
  PumpCommand, PumpResume, PumpSuspend, ReadBasalTemp, ReadBatteryStatus,
  ReadContrast, ReadCurPageNumber, ReadErrorStatus, ReadFirmwareVersion,
  ReadGlucoseHistory, ReadHistoryData, ReadPumpID, ReadPumpModel,
  ReadPumpState, ReadPumpStatus, ReadRTC, ReadRadioCtrlACL,
  ReadRemainingInsulin, ReadSettings, ReadTotalsToday, SetSuspend, PushEASY,
  PushUP, PushDOWN, PushACT, PushESC, TempBasal, ManualCommand,
  ReadCurGlucosePageNumber, ReadErrorStatus508, ReadBolusHistory,
  ReadDailyTotals, ReadPrimeBoluses, ReadAlarms, ReadProfileSets,
  ReadUserEvents, ReadRemoteControlID, Read128KMem, Read256KMem,
  ReadBasalTemp508, ReadTodayTotals508, ReadSensorSettings,
  ReadSensorHistoryData, ReadISIGHistory, FilterHistory, FilterGlucoseHistory,
  FilterISIGHistory, ReadProfiles511_STD, ReadProfiles511_A, ReadProfiles511_B,
  Model511_ExperimentOP125, Model511_ExperimentOP126, ReadSettings511,
  ReadPumpTrace, ReadDetailTrace, Model511_Experiment_OP165, ReadNewTraceAlarm,
  ReadOldTraceAlarm, WriteGlucoseHistoryTimestamp, ReadLanguage,
  ReadBolusWizardSetupStatus, ReadCarbUnits, ReadBGUnits, ReadCarbRatios,
  ReadInsulinSensitivities, ReadBGTargets, ReadBGAlarmCLocks,
  ReadReservoirWarning, ReadBGReminderEnable, ReadSettings512,
  ReadProfile_STD512, ReadProfile_A512, ReadProfile_B512, ReadLogicLinkIDS,
  Model512Experiment_OP150, ReadBGAlarmEnable, GuardianSensorSettings,
  GuardianSensorSettings, GuardianSensorDemoGraphTimeout,
  GuardianSensorAlarmSilence, GuardianSensorRateChangeAlerts,
  ReadSavedSettingsDate, ReadBolusReminderEnable, ReadBolusReminders,
  ReadFactoryParameters, ReadCalibrationFactor, ReadVCNTRHistory,
  ReadOtherDevicesIDS, PumpTraceSelect, PumpEnableDetailTrace,
  PumpDisableDetailTrace, Experiment_OP161, Experiment_OP162,
  Model511_Experiment_OP119, Model511_Experiment_OP120,
  Model511_Experiment_OP121, Model511_Experiment_OP122,
  Model511_Experiment_OP123, Model511_Experiment_OP124,
  Model511_Experiment_OP125, Model511_Experiment_OP126,
  Model511_Experiment_OP127, Model511_Experiment_OP128,
  Model511_Experiment_OP129, Model511_Experiment_OP130, SelectBasalProfile,
  SelectBasalProfileSTD, SelectBasalProfileA, SelectBasalProfileB,
  PumpExperiment_OP69, PumpExperiment_OP70, PumpExperiment_OP71,
  PumpExperiment_OP72, PumpExperiment_OP73, PumpExperiment_OP75}
                        Built-in commands to run after the main one.

This tool is intended to help discover protocol behavior. Under no
circumstance is it intended to deliver therapy.
```

##### `mm-send-comm.py ManualCommand -h`

```
+ mm-send-comm.py ManualCommand -h
usage: mm-send-comm.py ManualCommand [-h] [--params PARAMS] [--descr DESCR]
                                     [--name NAME] [--save]
                                     [--effectTime EFFECTTIME]
                                     [--maxRecords MAXRECORDS]
                                     [--bytesPerRecord BYTESPERRECORD]
                                     code

positional arguments:
  code                  The opcode to send to the pump.

optional arguments:
  -h, --help            show this help message and exit
  --params PARAMS       parameters to format into sent message
  --descr DESCR         Description of command
  --name NAME           Proposed name of command
  --save                Save response in a file.
  --effectTime EFFECTTIME
                        time to sleep before responding to message, float in
                        seconds
  --maxRecords MAXRECORDS
                        number of frames in a packet composing payload
                        response
  --bytesPerRecord BYTESPERRECORD
                        bytes per frame
```

#### `mm-send-comm.py sleep -h`
```

+ mm-send-comm.py sleep -h
usage: mm-send-comm.py sleep [-h] timeout

positional arguments:
  timeout     Sleep in between running --prefix and --postfix

optional arguments:
  -h, --help  show this help message and exit
```

#### `mm-send-comm.py tweak -h`

```
+ mm-send-comm.py tweak -h
usage: mm-send-comm.py tweak [-h] [--params PARAMS] [--descr DESCR]
                             [--name NAME] [--save] [--effectTime EFFECTTIME]
                             [--maxRecords MAXRECORDS]
                             [--bytesPerRecord BYTESPERRECORD] [--page PAGE]
                             [--begin BEGIN] [--end END]
                             
                             {BaseCommand, KeypadPush, PowerControl,
                             PowerControlOff, PumpCommand, PumpResume,
                             PumpSuspend, ReadBasalTemp, ReadBatteryStatus,
                             ReadContrast, ReadCurPageNumber, ReadErrorStatus,
                             ReadFirmwareVersion, ReadGlucoseHistory,
                             ReadHistoryData, ReadPumpID, ReadPumpModel,
                             ReadPumpState, ReadPumpStatus, ReadRTC,
                             ReadRadioCtrlACL, ReadRemainingInsulin,
                             ReadSettings, ReadTotalsToday, SetSuspend,
                             PushEASY, PushUP, PushDOWN, PushACT, PushESC,
                             TempBasal, ManualCommand,
                             ReadCurGlucosePageNumber, ReadErrorStatus508,
                             ReadBolusHistory, ReadDailyTotals,
                             ReadPrimeBoluses, ReadAlarms, ReadProfileSets,
                             ReadUserEvents, ReadRemoteControlID, Read128KMem,
                             Read256KMem, ReadBasalTemp508, ReadTodayTotals508,
                             ReadSensorSettings, ReadSensorHistoryData,
                             ReadISIGHistory, FilterHistory,
                             FilterGlucoseHistory, FilterISIGHistory,
                             ReadProfiles511_STD, ReadProfiles511_A,
                             ReadProfiles511_B, Model511_ExperimentOP125,
                             Model511_ExperimentOP126, ReadSettings511,
                             ReadPumpTrace, ReadDetailTrace,
                             Model511_Experiment_OP165, ReadNewTraceAlarm,
                             ReadOldTraceAlarm, WriteGlucoseHistoryTimestamp,
                             ReadLanguage, ReadBolusWizardSetupStatus,
                             ReadCarbUnits, ReadBGUnits, ReadCarbRatios,
                             ReadInsulinSensitivities, ReadBGTargets,
                             ReadBGAlarmCLocks, ReadReservoirWarning,
                             ReadBGReminderEnable, ReadSettings512,
                             ReadProfile_STD512, ReadProfile_A512,
                             ReadProfile_B512, ReadLogicLinkIDS,
                             Model512Experiment_OP150, ReadBGAlarmEnable,
                             GuardianSensorSettings, GuardianSensorSettings,
                             GuardianSensorDemoGraphTimeout,
                             GuardianSensorAlarmSilence,
                             GuardianSensorRateChangeAlerts,
                             ReadSavedSettingsDate, ReadBolusReminderEnable,
                             ReadBolusReminders, ReadFactoryParameters,
                             ReadCalibrationFactor, ReadVCNTRHistory,
                             ReadOtherDevicesIDS, PumpTraceSelect,
                             PumpEnableDetailTrace, PumpDisableDetailTrace,
                             Experiment_OP161, Experiment_OP162,
                             Model511_Experiment_OP119,
                             Model511_Experiment_OP120,
                             Model511_Experiment_OP121,
                             Model511_Experiment_OP122,
                             Model511_Experiment_OP123,
                             Model511_Experiment_OP124,
                             Model511_Experiment_OP125,
                             Model511_Experiment_OP126,
                             Model511_Experiment_OP127,
                             Model511_Experiment_OP128,
                             Model511_Experiment_OP129,
                             Model511_Experiment_OP130, SelectBasalProfile,
                             SelectBasalProfileSTD, SelectBasalProfileA,
                             SelectBasalProfileB, PumpExperiment_OP69,
                             PumpExperiment_OP70, PumpExperiment_OP71,
                             PumpExperiment_OP72, PumpExperiment_OP73,
                             PumpExperiment_OP75}

positional arguments:
  {BaseCommand, KeypadPush, PowerControl, PowerControlOff, PumpCommand,
  PumpResume, PumpSuspend, ReadBasalTemp, ReadBatteryStatus, ReadContrast,
  ReadCurPageNumber, ReadErrorStatus, ReadFirmwareVersion, ReadGlucoseHistory,
  ReadHistoryData, ReadPumpID, ReadPumpModel, ReadPumpState, ReadPumpStatus,
  ReadRTC, ReadRadioCtrlACL, ReadRemainingInsulin, ReadSettings,
  ReadTotalsToday, SetSuspend, PushEASY, PushUP, PushDOWN, PushACT, PushESC,
  TempBasal, ManualCommand, ReadCurGlucosePageNumber, ReadErrorStatus508,
  ReadBolusHistory, ReadDailyTotals, ReadPrimeBoluses, ReadAlarms,
  ReadProfileSets, ReadUserEvents, ReadRemoteControlID, Read128KMem,
  Read256KMem, ReadBasalTemp508, ReadTodayTotals508, ReadSensorSettings,
  ReadSensorHistoryData, ReadISIGHistory, FilterHistory, FilterGlucoseHistory,
  FilterISIGHistory, ReadProfiles511_STD, ReadProfiles511_A, ReadProfiles511_B,
  Model511_ExperimentOP125, Model511_ExperimentOP126, ReadSettings511,
  ReadPumpTrace, ReadDetailTrace, Model511_Experiment_OP165, ReadNewTraceAlarm,
  ReadOldTraceAlarm, WriteGlucoseHistoryTimestamp, ReadLanguage,
  ReadBolusWizardSetupStatus, ReadCarbUnits, ReadBGUnits, ReadCarbRatios,
  ReadInsulinSensitivities, ReadBGTargets, ReadBGAlarmCLocks,
  ReadReservoirWarning, ReadBGReminderEnable, ReadSettings512,
  ReadProfile_STD512, ReadProfile_A512, ReadProfile_B512, ReadLogicLinkIDS,
  Model512Experiment_OP150, ReadBGAlarmEnable, GuardianSensorSettings,
  GuardianSensorSettings, GuardianSensorDemoGraphTimeout,
  GuardianSensorAlarmSilence, GuardianSensorRateChangeAlerts,
  ReadSavedSettingsDate, ReadBolusReminderEnable, ReadBolusReminders,
  ReadFactoryParameters, ReadCalibrationFactor, ReadVCNTRHistory,
  ReadOtherDevicesIDS, PumpTraceSelect, PumpEnableDetailTrace,
  PumpDisableDetailTrace, Experiment_OP161, Experiment_OP162,
  Model511_Experiment_OP119, Model511_Experiment_OP120,
  Model511_Experiment_OP121, Model511_Experiment_OP122,
  Model511_Experiment_OP123, Model511_Experiment_OP124,
  Model511_Experiment_OP125, Model511_Experiment_OP126,
  Model511_Experiment_OP127, Model511_Experiment_OP128,
  Model511_Experiment_OP129, Model511_Experiment_OP130, SelectBasalProfile,
  SelectBasalProfileSTD, SelectBasalProfileA, SelectBasalProfileB,
  PumpExperiment_OP69, PumpExperiment_OP70, PumpExperiment_OP71,
  PumpExperiment_OP72, PumpExperiment_OP73, PumpExperiment_OP75}
                        Command to tweak.

optional arguments:
  -h, --help            show this help message and exit
  --params PARAMS       parameters to format into sent message
  --descr DESCR         Description of command
  --name NAME           Proposed name of command
  --save                Save response in a file.
  --effectTime EFFECTTIME
                        time to sleep before responding to message, float in
                        seconds
  --maxRecords MAXRECORDS
                        number of frames in a packet composing payload
                        response
  --bytesPerRecord BYTESPERRECORD
                        bytes per frame
  --page PAGE           Page to fetch (for ReadHistoryData)
  --begin BEGIN         begin date for FilterHistory
  --end END             end date for FilterHistory
```

##### `mm-latest.py -h`

```bash
usage: mm-latest.py [-h] [--serial SERIAL] [--port PORT] [--no-op]
                    [--skip-prelude] [--no-rf-prelude] [--skip-postlude] [-v]
                    [--init] [--no-clock] [--no-basal] [--no-temp]
                    [--no-reservoir] [--no-status]
                    [minutes]

mm-latest.py - Grab latest activity

positional arguments:
  minutes          [default: 30)]

optional arguments:
  -h, --help       show this help message and exit
  --serial SERIAL  serial number of pump [default: ]
  --port PORT      Path to device [default: ]
  --no-op          Dry run, don't do main function
  --skip-prelude   Don't do the normal prelude.
  --no-rf-prelude  Do the prelude, but don't query the pump.
  --skip-postlude  Don't do the normal postlude.
  -v, --verbose    Verbosity
  --init           Send power ctrl to initialize RF session.
  --no-clock       Also report current time on pump.
  --no-basal       Also report basal rates.
  --no-temp        Also report temp basal rates.
  --no-reservoir   Also report remaining insulin in reservoir.
  --no-status      Also report current suspend/bolus status.

Query pump for latest activity.
```


#### `./bin/mm-press-key.py`

```bash
usage: mm-press-key.py [-h] [--serial SERIAL] [--port PORT] [--no-op] [-v]
                       [--init]
                       {act,esc,up,down,easy} [{act,esc,up,down,easy} ...]

positional arguments:
  {act,esc,up,down,easy}
                        buttons to press [default: act)]

optional arguments:
  -h, --help            show this help message and exit
  --serial SERIAL       serial number of pump [default: ]
  --port PORT           Path to device [default: ]
  --no-op               Dry run, don't do main function
  -v, --verbose         Verbosity
  --init                Send power ctrl to initialize RF session.
```

#### `status-quo.sh`

`status-quo.sh </dev/ttyUSB0> <SERIAL>` runs several experiments, described below.
Each experiment is saved in the `./logs` directory, which is tracked by git.


##### `. bin/common`
Source a bunch of helper functions, notably:

##### `run_stick`_
Runs `python decocare/stick.py /dev/ttyUSB0`
and saves results in `logs/stick.log`.
When run by `status-quo.sh`, it creates
`./logs/baseline.stick.log` before continuing.
At end of experiments, it records `./logs/postmortem.stick.log`

##### `run_session`_
Runs `python decocare/session.py /dev/ttyUSB0 <SERIAL>`
and saves results in `logs/session.log`.

##### `run_commands`_
Runs `python decocare/commands.py /dev/ttyUSB0 <SERIAL>`
and saves results in `logs/commands.log`.

##### `run_download`_

Runs `python decocare/download.py /dev/ttyUSB0 <SERIAL>`
and saves results in `logs/download.log`.

The download script is configured to save each page of historical data as a raw
binary blob in the `./logs/` subdirectory like this:
`./logs/ReadHistoryData-page-$x.data`.

This script can take several minutes to run; it attempts to download
all pages of data available.

#### quick overview:

`status-quo.sh` also tries to summarize what happened, saving a quick
explanation of what happened in `logs/explain.log`.  The entire output
is saved in `./status-quo.log`.

#### `run_regress`
After `. bin/common`, `export SERIAL=511888` with your serial number.

Runs `python list_history.py` on each binary file found in `logs/`, saves
results in `./analysis/<SERIAL>/...`.

This is what I use to render the markdown files in analysis.
Often, the diffs between runs help test theories.

#### `list_history.py`
`list_history.py [--larger] ./logs/ReadHistory....page-0.data`
List/decode a page of history as markdown.

#### `list_opcodes.py`
`list_opcodes.py`
List records found in binary data by looking for opcodes, and a
regular data structure associated with that length.  Includes at least
one variable stop length strength.

#### `list_dates.py`
List records found in binary data by looking for dates.

#### usblyzer_filter.sh

```bash
# usblyzer_filter.sh was used to filter the raw usblyzer csv export into
# something a bit more manageable.
$ history
  553  ./usblyzer_filter.sh  first_run.csv  
  554  ls
  555  git mv first_run.csv pcaps/first_run/
  556  ./usblyzer_filter.sh  pcaps/first_run/first_run.csv  
  557  ./usblyzer_filter.sh  pcaps/first_run/first_run.csv   > pcaps/first_run/pcap.csv
  558  git mv second_run.csv pcaps/second_run/
  559  ./usblyzer_filter.sh pcaps/second_run/second_run.csv 
  560  ./usblyzer_filter.sh pcaps/second_run/second_run.csv  > pcaps/second_run/pcap.csv
  561  git mv third_run.csv pcaps/third_run/
  562  ./usblyzer_filter.sh  pcaps/third_run/third_run.csv 
  563  ./usblyzer_filter.sh  pcaps/third_run/third_run.csv  > pcaps/third_run/pcap.csv
bewest@paragon:~/src/decoding-carelink$ 
```

Thanks,
-[contributors](https://github.com/bewest/decoding-carelink/network/members)

