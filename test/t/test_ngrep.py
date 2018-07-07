import pytest


class TestNgrep(object):

    @pytest.mark.complete("ngrep -")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("ngrep -d ")
    def test_2(self, completion):
        assert completion.list
