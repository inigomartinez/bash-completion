import pytest


class TestXxd(object):

    @pytest.mark.complete("xxd ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("xxd -")
    def test_2(self, completion):
        assert completion.list
