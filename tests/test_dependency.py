import pytest
@pytest.fixture
def example_module():
    return "requests"
def test_denpendency(example_module):
    """
    This test is used only for measuring the execution time
    """
    import sys
    assert __import__(str(example_module))
    assert sys.version_info[0] <= 3