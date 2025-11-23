"""
Entry-point for form construction.

This module demonstrates the Builder pattern by:
1. Selecting a concrete builder at runtime via FormFactory.
2. Delegating the step-by-step construction to FormDirector.
3. Emitting the final form object for downstream use.
"""

from forms.director import FormDirector
from forms.factory import FormFactory


USER_INPUT = "lead"  # runtime value

data = {
    "name": "Krish",
    "email": "krish@krish.com",
    "phone": "9800000000",
    "address": "Kathmandu",
    "product_id": "P123"
}

builder = FormFactory.create(USER_INPUT)
director = FormDirector(builder)
form = director.construct(data)

print(form)
