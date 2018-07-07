import pytest


class TestDropdb(object):

    # --help can fail due to missing package dependencies, e.g. on Ubuntu 14
    @pytest.mark.complete("dropdb -",
                          skipif="! dropdb --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
