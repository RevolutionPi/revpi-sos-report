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

        # Per-thread scheduling: spot RT-priority contention between
        # CODESYS tasks and the piControl/piBridge kernel threads.
        self.add_cmd_output(
            "ps -eLo pid,lwp,cls,rtprio,nice,psr,pcpu,comm",
            suggest_filename="ps_thread_scheduling",
        )

        # Per CODESYS thread: policy, RT priority, CPU affinity and
        # schedstat (field 2 = runqueue wait time = starvation signal).
        self.add_cmd_output(
            'sh -c \'p=$(pgrep -f "[c]odesyscontrol" | head -1); '
            '[ -n "$p" ] || { echo "no codesys process found"; exit 0; }; '
            "for t in /proc/$p/task/*; do "
            'echo "=== $(cat "$t/comm") (tid ${t##*/}) ==="; '
            'chrt -p "${t##*/}"; taskset -cp "${t##*/}"; '
            'echo "schedstat: $(cat "$t/schedstat")"; '
            "done'",
            suggest_filename="codesys_thread_scheduling",
        )

        # CODESYS process limits (RTPRIO/memlock) and memory-lock/context
        # switch counters.
        self.add_cmd_output(
            'sh -c \'p=$(pgrep -f "[c]odesyscontrol" | head -1); '
            '[ -n "$p" ] || { echo "no codesys process found"; exit 0; }; '
            "cat /proc/$p/limits; "
            'grep -E "^(Threads|VmLck|VmRSS|voluntary_ctxt_switches|'
            "nonvoluntary_ctxt_switches):\" /proc/$p/status'",
            suggest_filename="codesys_process_resources",
        )


# vim: set et ts=4 sw=4 :
