"""Coordinates form building via a builder."""
from __future__ import annotations

from typing import Any

from forms.builders.base import FormBuilder


class FormDirector:
    """Orchestrates building using a provided builder."""

    def __init__(self, builder: FormBuilder) -> None:
        """Initialize with a builder instance."""
        self.builder = builder

    def construct(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Add fields, optionally populate, then build."""
        self.builder.add_fields()
        if data:
            self.builder.populate(data)
        return self.builder.build()
