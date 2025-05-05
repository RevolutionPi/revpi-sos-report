# SPDX-FileCopyrightText: 2023 KUNBUS GmbH
#
# SPDX-License-Identifier: GPL-2.0-or-later
#
cmake_minimum_required(VERSION 3.13)

project(revpi-sos)

include(GNUInstallDirs)
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)

install(PROGRAMS revpi-sos
  DESTINATION ${CMAKE_INSTALL_BINDIR}
)

install(FILES plugins/revpi.py plugins/revpi-eep.py plugins/revpi-codesys.py
  DESTINATION ${Python3_SITELIB}/sos/report/plugins/
)

install(FILES revpi-sos.1
  DESTINATION ${CMAKE_INSTALL_MANDIR}/man1
)
