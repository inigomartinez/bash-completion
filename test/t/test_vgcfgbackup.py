import pytest


class TestVgcfgbackup(object):

    @pytest.mark.complete("vgcfgbackup -",
                          skipif="! vgcfgbackup --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
