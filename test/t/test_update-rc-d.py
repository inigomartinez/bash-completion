import pytest


@pytest.mark.command("update-rc.d")
class TestUpdateRcD(object):

    @pytest.mark.complete("update-rc.d -")
    def test_1(self, completion):
        assert completion.list
