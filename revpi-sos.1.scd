revpi-sos(1)

# NAME

revpi-sos  - collect the information for RevPi related problems debugging

# SYNOPSIS

*revpi-sos* [_options_]

# DESCRIPTION

*revpi-sos* base on sosreport(1) to collect the needed information for
debugging.

The information includes the following files:
- /var/log/syslog
- /var/log/kern.log
- /var/log/apache2/error.log
- /var/log/apache2/revpi-\*-error.log
- /var/www/pictory/projects/\_config.rsc
- /boot/firmware/cmdline.txt
- /boot/firmware/config.txt
- /etc/default/rpi-eeprom-update
- /etc/dhcpcd.conf
- /etc/resolv.conf
- /etc/revpi/image-release
- /etc/network/interfaces
- /etc/network/interfaces.d/\*

and output of following commands:
- df -h
- dmesg
- uname -a
- piTest -d
- ps -ax
- lsusb -v
- free
- apt-cache show picontrol
- apt-cache show pictory
- apt-cache show rpi-eeprom
- apt-cache show linux-image-revpi-v8
- netstat -ln
- rpi-eeprom-update
- vclog -a, vclog -m
- ls /dev/ttyUSB\*
- ls /dev/ttyRS485
- ls -l /etc/revpi/config.rsc
- vcgencmd version
- journalctl --no-pager -u cockpit
- vcgencmd measure_temp
- vcgencmd measure_clock arm
- revpi-device-info

# OPTIONS

*-f*
	Execute without confirmation(generating the report and change the ownership
	to current user).

*-h* Show the help list.

# SEE ALSO

For more information on Revolution Pi visit https://revolutionpi.com
