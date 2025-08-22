#
# SPDX-FileCopyrightText: 2020-2025 KUNBUS GmbH
#
# SPDX-License-Identifier: GPL-2.0-or-later
#


from sos.report.plugins import Plugin, DebianPlugin


class RevPi(Plugin, DebianPlugin):
    """
    This plugin gathers Revolution Pi specific information from the system

    The output of this plugin is used in the revpi-sos-report archive, which
    often is requested by the support team.
    """

    short_desc = "Revolution Pi information"

    requires_root = True
    profiles = ("system",)
    plugin_name = "revpi"

    def setup(self):
        self.add_copy_spec(
            [
                "/var/log/syslog*",
                "/var/log/apache2/error.log",
                "/var/log/apache2/revpi-*-error.log",
                "/var/log/kern.log*",
                "/etc/revpi/config.rsc",
                "/boot/firmware/cmdline.txt",
                "/boot/firmware/config.txt",
                "/etc/default/rpi-eeprom-update",
                "/etc/revpi/image-release",
                "/etc/revpi/factory-reset",
                "/etc/dhcpcd.conf",
                "/etc/network/interfaces",
                "/etc/network/interfaces.d/*",
                "/etc/resolv.conf",
                "/sys/bus/serial/drivers/pi-bridge/stats/*",
                "/sys/class/net/*/carrier",
                "/sys/class/net/*/speed",
                "/sys/class/net/*/duplex",
                "/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor",
                "/sys/block/mmcblk0/device/life_time",
                "/sys/block/mmcblk0/device/pre_eol_info",
                "/proc/tty/driver/ttyAMA",
                "/home/pi/.revpi-factory-reset",
            ]
        )

        self.add_cmd_output(
            [
                "df -h",
                "dmesg",
                "uname -a",
                "piTest -d",
                "ps -ax",
                "ls -l /dev/ttyUSB*",
                "ls -l /dev/ttyRS485*",
                "ls -l /etc/revpi/config.rsc",
                "vcgencmd measure_temp",
                "vcgencmd measure_clock arm",
                "journalctl --no-pager -u cockpit",
                "lsusb -v",
                "free",
                "apt-cache show picontrol",
                "apt-cache show pictory",
                "apt-cache show rpi-eeprom",
                "apt-cache show cockpit-revpi",
                "apt-cache show linux-image-revpi-v8",
                "netstat -ln",
                "rpi-eeprom-update",
                "vclog -a",
                "vclog -m",
                "vcgencmd version",
                "modinfo piControl",
                "dpkg -l",
            ]
        )


# vim: set et ts=4 sw=4 :
