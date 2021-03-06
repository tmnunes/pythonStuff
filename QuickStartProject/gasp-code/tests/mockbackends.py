# -*- coding: utf-8 -*-
#
# This program is part of GASP, a toolkit for newbie Python Programmers.
# Copyright (C) 2009, the GASP Development Team
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

class MockBackEnd(object):
    def __init__(self):
        self.screen = None
        self.rate = None

    def create_screen(self, screen):
        self.screen = screen

    def set_frame_rate(self, rate):
        self.rate = rate
