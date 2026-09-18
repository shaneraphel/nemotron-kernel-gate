"""Decide whether a generated kernel matches a reference."""

from __future__ import annotations

import numpy as np


def accept(candidate, reference) -> bool:
    candidate = np.asarray(candidate)
    reference = np.asarray(reference)
    if np.issubdtype(np.asarray(candidate).dtype, np.integer) or np.issubdtype(
        np.asarray(reference).dtype, np.integer
    ):
        accepted = bool(np.array_equal(candidate, reference))
    else:
        accepted = bool(np.allclose(candidate, reference, rtol=1e-3, atol=1e-3))
    return accepted
