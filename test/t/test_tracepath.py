import pytest


class TestTracepath(object):

    @pytest.mark.complete("tracepath ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("tracepath -")
    def test_2(self, completion):
        assert completion.list
