import pytest


class TestXmlwf(object):

    @pytest.mark.complete("xmlwf ")
    def test_1(self, completion):
        assert completion.list
