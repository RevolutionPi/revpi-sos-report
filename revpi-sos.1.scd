revpi-sos(1)

# NAME

revpi-sos - collect information for RevPi related problems debugging

# SYNOPSIS

*revpi-sos* [*-f*]

# DESCRIPTION

*revpi-sos* is based on *sosreport*(1) to collect necessary information for
debugging problems on a Revolution Pi system.++
Please take care to check that the SOS report doesn't contain sensitive
information like passwords before sharing it with others.

Upon contacting Revolution Pi support they might request an SOS report. It is
generated with *revpi-sos*.++
The SOS report should be sent to support@kunbus.com, either along a new support
request or after support requested it.

The SOS report is saved to /var/tmp/ in .tar.gz format.

What information *revpi-sos* collects is noted in the *COLLECTED DATA* section.

# OPTIONS

*-f*
	Execute without confirmation (generating the report and change the ownership
	to current user).

*-h* Show the help list.

# COLLECTED DATA

This section lists all the files and commands that are used to collect the
information about the system that is included in an SOS report.

## Files

The following is a list of files that *revpi-sos* collects and packs into a SOS
report. If a file is not present it's inclusion into the report is skipped.

- /var/log/syslog
- /var/log/apache2/error.log
- /var/log/apache2/revpi-\*-error.log
- /var/log/kern.log
- /etc/revpi/config.rsc
- /boot/firmare/cmdline.txt
- /boot/firmware/config.txt
- /etc/default/rpi-eeprom-update
- /etc/revpi/image-release
- /etc/dhcpcd.conf
- /etc/network/interfaces
- /etc/network/interfaces.d/\*
- /etc/resolv.conf
- /etc/CODESYSControl.cfg
- /etc/CODESYSControl_user.cfg
- /tmp/codesyscontrol.log
- /var/opt/codesys/codesyscontrol.log

## Output of commands

- df -h
- dmesg
- uname -a
- piTest -d
- ps -ax
- ls -l /dev/ttyUSB\*
- ls -l /dev/ttyRS485\*
- ls -l /etc/revpi/config.rsc
- vcgencmd measure_temp
- vcgencmd measure_clock arm
- journalctl --no-pager -u cockpit
- lsusb -v
- free
- apt-cache show picontrol
- apt-cache show pictory
- apt-cache show rpi-eeprom
- apt-cache show cockpit-revpi
- apt-cache show linux-image-revpi-v8
- netstat -ln
- rpi-eeprom-update
- vclog -a
- vclog -m
- vcgencmd version
- modinfo piControl
- cat /sys/devices/system/cpu/cpu?/cpufreq/scaling_governor
- revpi-device-info

# EXAMPLES

To create an SOS report simply call *revpi-sos*

```
revpi-sos
```

The contents of the SOS report can be viewed with

```
tar -tzf /path/to/sos-report.tar.gz
```

Unpacking the SOS report is possible with

```
tar -xzf /path/to/sos-report.tar.gz
```

# SEE ALSO

*sosreport*(1)

For more information on Revolution Pi visit https://revolutionpi.com
