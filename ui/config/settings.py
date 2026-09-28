import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    base_url: str


_ENVIRONMENTS: dict[str, Settings] = {
    "staging": Settings(base_url="https://automationsimplified.vercel.app/"),
}

TEST_ENV = os.getenv("TEST_ENV", "staging").lower()

if TEST_ENV not in _ENVIRONMENTS:
    raise KeyError(
        f"Unknown TEST_ENV={TEST_ENV!r}. Available: {sorted(_ENVIRONMENTS)}"
    )

settings = _ENVIRONMENTS[TEST_ENV]
