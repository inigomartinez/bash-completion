import pytest


class TestSlackpkg(object):

    @pytest.mark.complete("slackpkg -")
    def test_1(self, completion):
        assert completion.list
