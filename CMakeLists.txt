# SPDX-FileCopyrightText: 2023-2024 KUNBUS GmbH
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

add_custom_target(
  revpi-sos.1 ALL
  COMMAND scdoc < ${CMAKE_SOURCE_DIR}/revpi-sos.1.scd > ${PROJECT_BINARY_DIR}/revpi-sos.1
  DEPENDS ${CMAKE_SOURCE_DIR}/revpi-sos.1.scd
)

install(FILES ${PROJECT_BINARY_DIR}/revpi-sos.1
  DESTINATION ${CMAKE_INSTALL_MANDIR}/man8/
)
