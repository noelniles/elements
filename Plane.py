"""A Euclidean plane surface

Copyright (C) 2016 Noel Niles noelniles@gmail.com

This file is part of elements.

    Elements is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Elements is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
"""
import matplotlib.pyplot as plt


class Plane:
    """Euclidean plane

    A plane surface is that which lies evenly with the straight lines on
    itself.
    """
    def __init__(self):
        self.plane = plt

    def planeshow(self):
        self.plane.plot()
        self.plane.show()
