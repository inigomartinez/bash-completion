import pytest


class TestSitecopy(object):

    @pytest.mark.complete("sitecopy --")
    def test_1(self, completion):
        assert completion.list
