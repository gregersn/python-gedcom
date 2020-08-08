# -*- coding: utf-8 -*-

#  Copyright (C) 2020
#
#  This file is part of the Python GEDCOM Parser.
#
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
#  For more, have a look at the GitHub repository at:
#  https://github.com/nickreynke/python-gedcom

"""
Module containing all relevant elements generated by a `gedcom.parser.Parser`.
An element represents a line within GEDCOM data.
"""

__all__ = [
    # Modules
    "element",
    "family",
    "header",
    "individual",
    "note",
    "object",
    "repository",
    "root",
    "source",
    "submission",
    "submitter",
    # Constants
    "ELEMENT_TYPES"
]

from gedcom import tags
from gedcom.elements.family import FamilyElement
from gedcom.elements.header import HeaderElement
from gedcom.elements.individual import IndividualElement
from gedcom.elements.note import NoteElement
from gedcom.elements.object import ObjectElement
from gedcom.elements.repository import RepositoryElement
from gedcom.elements.source import SourceElement
from gedcom.elements.submission import SubmissionElement
from gedcom.elements.submitter import SubmitterElement

ELEMENT_TYPES = {
    tags.GEDCOM_TAG_HEADER: HeaderElement,
    tags.GEDCOM_TAG_INDIVIDUAL: IndividualElement,
    tags.GEDCOM_TAG_FAMILY: FamilyElement,
    tags.GEDCOM_TAG_NOTE: NoteElement,
    tags.GEDCOM_TAG_OBJECT: ObjectElement,
    tags.GEDCOM_TAG_SOURCE: SourceElement,
    tags.GEDCOM_TAG_SUBMISSION: SubmissionElement,
    tags.GEDCOM_TAG_SUBMITTER: SubmitterElement,
    tags.GEDCOM_TAG_REPOSITORY: RepositoryElement
}