import pytest


class TestVgscan(object):

    @pytest.mark.complete("vgscan -",
                          skipif="! vgscan --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
