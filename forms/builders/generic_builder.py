"""Generic builder for simple field lists."""
from __future__ import annotations

from typing import Any

from forms.builders.base import FormBuilder


class GenericFormBuilder(FormBuilder):
    """Builds a form from a provided list of fields."""

    def __init__(self, fields: list[str]) -> None:
        """Initialize with field names."""
        self.form: dict[str, Any] = {}
        self.fields: list[str] = fields

    def add_fields(self) -> None:
        """Add each field with None default."""
        for field in self.fields:
            self.form[field] = None

    def populate(self, data: dict[str, Any]) -> None:
        """Set values for known keys."""
        for key, value in data.items():
            if key in self.form:
                self.form[key] = value

    def build(self) -> dict[str, Any]:
        """Return the form dict."""
        return self.form
