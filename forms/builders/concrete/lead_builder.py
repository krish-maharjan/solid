"""Lead form builder."""
from __future__ import annotations

from typing import Any

from forms.builders.fields import LEAD_FIELDS
from forms.builders.generic_builder import GenericFormBuilder
from forms.factory import register_form


@register_form("lead")
class LeadFormBuilder(GenericFormBuilder):
    """Builder for simple lead forms using the generic builder base."""

    def __init__(self) -> None:
        """Initialize with the predefined lead field list."""
        super().__init__(LEAD_FIELDS)
        # Explicit type ensures form dict is properly annotated for tooling
        self.form: dict[str, Any]
