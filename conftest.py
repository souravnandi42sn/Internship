import pytest

@pytest.fixture(scope='module')
def fixturetest1():
    #a="od_en_US"
    a=["od_en_US","fd89fba2959239b2"]
    return a
