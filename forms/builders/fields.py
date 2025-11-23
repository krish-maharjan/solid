"""Field name lists for builders."""
from __future__ import annotations

from typing import Final

BASE_FIELDS: Final[list[str]] = [
    "name",
    "email",
]

CUSTOMER_FIELDS: Final[list[str]] = [
    *BASE_FIELDS,
    "address",
    "phone",
]

LEAD_FIELDS: Final[list[str]] = [
    *BASE_FIELDS
]
