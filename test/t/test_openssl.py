import pytest


class TestOpenssl(object):

    @pytest.mark.complete("openssl ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("openssl pkey -cipher ")
    def test_2(self, completion):
        assert completion.list

    @pytest.mark.complete("openssl dgst -s")
    def test_3(self, completion):
        assert completion.list
