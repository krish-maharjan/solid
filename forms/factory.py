"""Form factory with registration and auto-discovery."""
from __future__ import annotations

import importlib
import pkgutil
from typing import Type

from forms.builders.base import FormBuilder


class FormFactory:
    """Create builders by key; supports lazy auto-discovery."""

    registry: dict[str, Type[FormBuilder]] = {}

    @classmethod
    def register(cls, key: str, builder_cls: Type[FormBuilder]) -> None:
        """Register a builder class under a key."""
        cls.registry[key] = builder_cls

    @classmethod
    def autodiscover(cls, package_path: str = "forms.builders.concrete") -> None:
        """Import all modules in the concrete builders package."""
        try:
            pkg = importlib.import_module(package_path)
        except ModuleNotFoundError:
            return
        for _finder, name, _ispkg in pkgutil.iter_modules(pkg.__path__):
            full_name = f"{package_path}.{name}"
            importlib.import_module(full_name)

    @classmethod
    def create(cls, key: str) -> FormBuilder:
        """Return a builder instance for the given key."""
        if not cls.registry:
            cls.autodiscover()
        builder_cls = cls.registry.get(key)
        if not builder_cls:
            raise ValueError("Unknown form type")
        return builder_cls()


def register_form(key: str):
    """Decorator that registers the decorated class under a key."""

    def decorator(builder_cls: Type[FormBuilder]) -> Type[FormBuilder]:
        FormFactory.register(key, builder_cls)
        return builder_cls

    return decorator
