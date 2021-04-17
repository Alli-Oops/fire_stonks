############### TEST WAVE 3 (4 tests) PASSED #### #CORRECT
import pytest
from fire_stonks.user import User
from fire_stonks.stonk import Stonk
from fire_stonks.duediligence import DueDiligence

### test 3.1 PASSED ### in DueDiligence #U
def test_dd_overrides_to_string():
    resource = "link"
    dd = DueDiligence(resource)
    stringified_dd = str(dd)
    assert stringified_dd == "This resource has information about a stonk pick"

### test 3.2 PASSED ### in User #U
def test_copy_stonk_returns_true():
### primary user's stock_picks and User instance ###
    stonk_a = Stonk(
        "CTSO", research = [], prediction = 1
    )
    stonk_b = Stonk(
        "INSG", research = [], prediction = 3
    )
    stonk_c = Stonk(
        "ZIM", research = [], prediction = 1
    )
    primary = User(
        stonk_picks = [stonk_a, stonk_b, stonk_c]
    )
### influencing user's stock_picks and User instance ###
    nice_stonk = Stonk(
        "ANTIBE", research = [], prediction = 1
    )
    stonk_e = Stonk(
        "SPCE", research = [], prediction = 3
    )
    influencer = User(
        stonk_picks = [nice_stonk, stonk_e]
    )

    result = primary.copy_stonk(influencer, nice_stonk)

    assert len(primary.stonk_picks) is 4
    assert stonk_e not in primary.stonk_picks
    assert nice_stonk in primary.stonk_picks
    assert stonk_a in primary.stonk_picks
    assert stonk_b in primary.stonk_picks
    assert stonk_c in primary.stonk_picks
    assert len(influencer.stonk_picks) is 2
    assert stonk_e in influencer.stonk_picks
    assert nice_stonk in influencer.stonk_picks
    assert result is True

### test 3.3 PASSED ### in User #U
def test_copy_stonk_when_nice_stonk_is_missing_returns_false():
    nice_stonk = Stonk(
        "LUMN", research = [], prediction = 1
    )
### primary user's stock_picks and User instance ###
    stonk_a = Stonk(
        "CTSO", research = [], prediction = 1
    )
    stonk_b = Stonk(
        "INSG", research = [], prediction = 3
    )
    stonk_c = Stonk(
        "ZIM", research = [], prediction = 1
    )
    primary = User(
        stonk_picks = [stonk_a, stonk_b, stonk_c]
    )
### influencing user's stock_picks and User instance ###
    stonk_d = Stonk(
        "NFLX", research = [], prediction = 1
    )
    stonk_e = Stonk(
        "SPCE", research = [], prediction = 3
    )
    influencer = User(
        stonk_picks = [stonk_d, stonk_e]
    )

    result = primary.copy_stonk(influencer, nice_stonk)

    assert len(primary.stonk_picks) is 3
    assert nice_stonk not in primary.stonk_picks
    assert stonk_a in primary.stonk_picks
    assert stonk_b in primary.stonk_picks
    assert stonk_c in primary.stonk_picks
    assert len(influencer.stonk_picks) is 2
    assert nice_stonk not in influencer.stonk_picks
    assert stonk_d in influencer.stonk_picks
    assert stonk_e in influencer.stonk_picks
    assert result is False


### 3.4 PASSED ### in User #U
def test_copy_stonk_from_influencer_empty_returns_false():
    nice_stonk = Stonk(
        "LUMN", research = [], prediction = 1
    )
### primary user's stock_picks and User instance ###
    stonk_a = Stonk(
        "CTSO", research = [], prediction = 1
    )
    stonk_b = Stonk(
        "INSG", research = [], prediction = 3
    )
    stonk_c = Stonk(
        "ZIM", research = [], prediction = 1
    )
    primary = User(
        stonk_picks = [stonk_a, stonk_b, stonk_c]
    )
### influencing user's stock_picks and User instance ###
    influencer = User(
        stonk_picks = []
    )

    result = primary.copy_stonk(influencer, nice_stonk)

    assert len(primary.stonk_picks) is 3
    assert len(influencer.stonk_picks) is 0
    assert result is False