# -*- coding: utf-8 -*-

# Python GEDCOM Parser
#
# Copyright (C) 2020 Christopher Horn (cdhorn at embarqmail dot com)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
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
# Further information about the license: http://www.gnu.org/licenses/gpl-2.0.html

"""
Substructure parser for a `INDIVIDUAL_EVENT_DETAIL` emdedded record.

This is referenced as part of a larger structure so there is no anchor tag.
"""

import gedcom.tags as tags
from gedcom.element.element import Element
from gedcom.subparsers.event_detail import event_detail


def individual_event_detail(element: Element) -> dict:
    """Parses and extracts a `INDIVIDUAL_EVENT_DETAIL` structure.

    The `element` should be the parent that contains it.
    """
    record = event_detail(element)
    record['age'] = ''
    for child in element.get_child_elements():
        if child.get_tag() == tags.GEDCOM_TAG_AGE:
            record['age'] = child.get_value()

    return record