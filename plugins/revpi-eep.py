#
# SPDX-License-Identifier: GPL-2.0
#
# Copyright 2023 KUNBUS GmbH
#


from sos.report.plugins import Plugin, DebianPlugin


class RevPiEEP(Plugin, DebianPlugin):
    """
    This plugin gathers Revolution Pi specific information from the HAT eeprom.

    The output of this plugin is used in the revpi-sos-report archive, which
    often is requested by the support team.
    """

    short_desc = "Revolution Pi EEP information"

    requires_root = False
    profiles = ("system",)
    plugin_name = "revpi-eep"

    packages = ("python3-revpi-device-info",)

    def setup(self):
        self.add_cmd_output(
            [
                "revpi-device-info",
            ]
        )


# vim: set et ts=4 sw=4 :
