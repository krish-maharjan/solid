"""Lead form builder."""
from __future__ import annotations

from typing import Any

from forms.builders.base import FormBuilder
from forms.builders.fields import LEAD_FIELDS
from forms.factory import register_form


@register_form("lead")
class LeadFormBuilder(FormBuilder):
    """Builds the lead form."""

    def __init__(self) -> None:
        """Initialize empty form dict."""
        self.form: dict[str, Any] = {}

    def add_fields(self) -> None:
        """Add base and lead fields."""
        for field in LEAD_FIELDS:
            self.form[field] = None

    def populate(self, data: dict[str, Any]) -> None:
        """Set values for known fields."""
        for key, value in data.items():
            if key in self.form:
                self.form[key] = value

    def build(self) -> dict[str, Any]:
        """Return the form dict."""
        return self.form
