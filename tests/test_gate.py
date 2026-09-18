import numpy as np
from nemotron_kernel.gate import accept


def test_integer_must_match_exactly():
    assert accept(np.array([1, 2], dtype=np.int64), np.array([1, 2], dtype=np.int64))
    assert not accept(np.array([1, 2], dtype=np.int64), np.array([1, 3], dtype=np.int64))


def test_float_allclose_stays():
    assert accept(np.array([1.0]), np.array([1.0000001]))
