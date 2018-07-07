import pytest


class TestCurl(object):

    @pytest.mark.complete("curl --h")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("curl -o f", cwd="shared/default/foo.d")
    def test_2(self, completion):
        assert completion.list == ["foo"]

    @pytest.mark.complete("curl -LRo f", cwd="shared/default/foo.d")
    def test_3(self, completion):
        assert completion.list == ["foo"]

    @pytest.mark.complete("curl --o f")
    def test_4(self, completion):
        assert not completion.list
