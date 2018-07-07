import pytest


class TestPylint(object):

    @pytest.mark.complete("pylint --v")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("pylint --confidence=HIGH,")
    def test_2(self, completion):
        assert completion.list
