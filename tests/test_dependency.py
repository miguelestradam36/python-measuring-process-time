import pytest
def test_denpendency():
    import sys
    assert sys.version_info[0] <= 3