import pytest


class TestChronyc(object):

    @pytest.mark.complete("chronyc ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("chronyc -")
    def test_2(self, completion):
        assert completion.list
