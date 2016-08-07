"""Euclid's 5 postulates in Python

Copyright (C) 2016 Noel Niles noelniles@gmail.com

This file is part of elements.

    Elements is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Elements is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Elements. If not, see <http://www.gnu.org/licenses/>.
"""
import Plane


class Postulates:
    """Initialize the figure and the axes."""
    def __init__(self, plane):
        self.plane = plane.plane
        self.fig, self.ax = self.plane.subplots()

    def post1(self, a, b):
        """To draw a straight line from any point to any point.

        Given: 2 points a=(x1,y1) and b=(x2,y2)
        Describe: a line from a to b
        """
        line = [(a), (b)]
        (linexs, lineys) = zip(*line)
        self.ax.add_line(self.plane.Line2D(linexs, lineys, linewidth=2))
