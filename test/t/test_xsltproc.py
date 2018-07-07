import pytest


class TestXsltproc(object):

    @pytest.mark.complete("xsltproc ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("xsltproc -")
    def test_2(self, completion):
        assert completion.list
