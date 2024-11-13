#
# SPDX-FileCopyrightText: 2020-2023 KUNBUS GmbH
#
# SPDX-License-Identifier: GPL-2.0-or-later
#


from sos.report.plugins import Plugin, DebianPlugin


class RevPiCodesys(Plugin, DebianPlugin):
    """
    This plugin gathers Revolution Pi CODESYS specific information.

    The output of this plugin is used in the revpi-soss-report archive, which
    often is requested by the support team.
    """

    short_desc = "Revolution Pi CODEDSYS information"

    requires_root = True
    profiles = ("system",)
    plugin_name = "revpi-codesys"

    packages = ("codesyscontrol",)

    def setup(self):
        self.add_copy_spec(
            [
                "/etc/CODESYSControl.cfg",
                "/etc/CODESYSControl_User.cfg",
                "/etc/codesyscontrol/CODESYSControl.cfg",
                "/etc/codesyscontrol/CODESYSControl_User.cfg",
                "/tmp/codesyscontrol.log",
                "/var/opt/codesys/codesyscontrol.log",
            ]
        )


# vim: set et ts=4 sw=4 :
