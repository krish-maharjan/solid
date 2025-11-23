# Solid Builder

A minimal Python demonstration of the Builder pattern for form construction with lazy auto‑discovery of concrete builders. It uses a simple `FormFactory` and `FormDirector` to compose and build forms at runtime.

## Features
- Runtime selection of builders via `FormFactory.create(key)`
- Lazy auto‑discovery: imports `forms.builders.concrete.*` on demand
- Clean separation: factory, director, builders, and field definitions

## Quick Start

Requirements: Python 3.11+ (tested), no third‑party deps.

```bash
# From repo root
python -m forms.main
```

This runs a small demo that selects a builder by key (e.g., `lead` or `customer`) and prints the built form.

## Usage

```python
from forms.factory import FormFactory
from forms.director import FormDirector

# Choose a builder key at runtime
builder = FormFactory.create("customer")

# Drive construction via the director
director = FormDirector(builder)
form = director.construct({
    "name": "Krish",
    "email": "krish@krish.com",
    "address": "Kathmandu",
})

print(form)
# {'name': 'Krish', 'email': 'krish@krish.com', 'address': 'Kathmandu', 'phone': None}
```

## Architecture

- `forms/factory.py`
  - `FormFactory.register(key, cls)`: internal registry mapping keys to builders
  - `FormFactory.autodiscover()`: imports `forms.builders.concrete` modules to trigger `@register_form`
  - `FormFactory.create(key)`: lazily calls `autodiscover()` when registry is empty, returns builder instance
  - `register_form(key)`: decorator that registers a builder class
- `forms/director.py`
  - `FormDirector.construct(data=None)`: calls `add_fields()`, optional `populate(data)`, then `build()`
- `forms/builders/base.py`: abstract `FormBuilder` contract (`add_fields`, `populate`, `build`)
- `forms/builders/concrete/`: concrete builders (`customer`, `lead`) that use `@register_form`
- `forms/builders/fields.py`: shared field lists

## Adding a New Builder

1. Create a module under `forms/builders/concrete/`, e.g. `account_builder.py`.
2. Implement a class that conforms to `FormBuilder`.
3. Decorate with `@register_form("account")`.
4. On first use, `FormFactory.create("account")` will auto‑discover and register it.

Example skeleton:

```python
from typing import Any
from forms.builders.base import FormBuilder
from forms.factory import register_form

@register_form("account")
class AccountFormBuilder(FormBuilder):
    def __init__(self) -> None:
        self.form: dict[str, Any] = {}

    def add_fields(self) -> None:
        for field in ("name", "email", "account_id"):
            self.form[field] = None

    def populate(self, data: dict[str, Any]) -> None:
        for k, v in data.items():
            if k in self.form:
                self.form[k] = v

    def build(self) -> dict[str, Any]:
        return self.form
```

## Conventions
- PEP 257 compliant
- Type annotations throughout; return types explicit
- Key naming and structure follow PEP 8