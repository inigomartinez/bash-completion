import pytest


class Test2to3(object):

    @pytest.mark.complete("2to3 ")
    def test_1(self, completion):
        assert completion.list
