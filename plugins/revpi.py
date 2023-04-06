#
# SPDX-License-Identifier: GPL-2.0
#
# Copyright 2020-2023 KUNBUS GmbH
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
                "/var/log/messages",
                "/var/log/apache2/error.log",
                "/var/log/kern.log",
                "/var/log/daemon.log",
                "/etc/revpi/config.rsc",
                "/boot/cmdline.txt",
                "/boot/config.txt",
                "/etc/revpi/image-release",
                "/etc/dhcpcd.conf",
                "/etc/network/interfaces",
                "/etc/resolv.conf",
            ]
        )

        self.add_cmd_output(
            [
                "df -h",
                "dmesg",
                "uname -a",
                "piTest -d",
                "ps -ax",
                "ls /dev/ttyUSB*",
                "ls /dev/ttyRS485",
                "ls -l /etc/revpi/config.rsc",
                "vcgencmd measure_temp",
                "vcgencmd measure_clock arm",
                "lsusb -v",
                "free",
                "apt-cache show pictory",
                "apt-cache show revpi-webstatus",
                "apt-cache show raspberrypi-kernel",
                "netstat -ln",
                "vcgencmd version",
            ]
        )


# vim: set et ts=4 sw=4 :
