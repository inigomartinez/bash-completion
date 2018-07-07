import pytest


class TestSh(object):

    @pytest.mark.complete("sh -")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("sh +")
    def test_2(self, completion):
        assert completion.list

    @pytest.mark.complete("sh -o ")
    def test_3(self, completion):
        assert completion.list

    @pytest.mark.complete("sh -c ")
    def test_4(self, completion):
        assert not completion.list
