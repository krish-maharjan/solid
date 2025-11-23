"""Abstract builder interface."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class FormBuilder(ABC):
    """Contract for form builders."""

    @abstractmethod
    def add_fields(self) -> None:
        """Add required form fields."""

    @abstractmethod
    def populate(self, data: dict[str, Any]) -> None:
        """Populate values from a data dict."""

    @abstractmethod
    def build(self) -> dict[str, Any]:
        """Return the final form dict."""
