#!/usr/bin/env python3

#
# pdfarranger - GTK+ based utility for splitting, rearrangement and 
# modification of PDF documents.
# Copyright (C) 2008-2017 Konstantinos Poulios
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

import os
import re

from DistUtilsExtra.auto import setup

data_files=[('share/applications', ['data/pdfarranger.desktop']),
            ('share/pdfarranger', ['data/pdfarranger.ui']),
            ('share/icons/hicolor/16x16/apps',
             ['data/hicolor/16x16/apps/pdfarranger.png']),
            ('share/icons/hicolor/32x32/apps',
             ['data/hicolor/32x32/apps/pdfarranger.png']),
            ('share/icons/hicolor/48x48/apps',
             ['data/hicolor/48x48/apps/pdfarranger.png']),
            ('share/icons/hicolor/256x256/apps',
             ['data/hicolor/256x256/apps/pdfarranger.png']),
            ('share/icons/hicolor/scalable/apps',
             ['data/hicolor/scalable/apps/pdfarranger.svg']),
            ('share/man/man1', ['doc/pdfarranger.1'])]

setup(name='pdfarranger',
      version='1.0',
      author='Jerome Robert',
      author_email='jeromerobert@gmx.com',
      description='A simple application for PDF Merging, Rearranging, and Splitting',
      url = 'https://github.com/jeromerobert/pdfarranger',
      license='GNU GPL-3',
      scripts=['bin/pdfarranger'],
      packages=['pdfarranger'],
      data_files=data_files
     )
