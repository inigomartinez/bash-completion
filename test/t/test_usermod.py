import pytest


class TestUsermod(object):

    @pytest.mark.complete("usermod ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("usermod -")
    def test_2(self, completion):
        assert completion.list
