############### TEST WAVE 1 (5 tests) PASSED #### #CORRECT

import pytest
# The following line imports the User class from the module user inside the fire_stonks package.
from fire_stonks.user import User
#### WAVE 1### #U

### test 1.1 PASSED ### in User #U
def test_user_has_stonk_picks():
    user = User()
    assert len(user.stonk_picks) is 0

### test 1.2 PASSED ### in User #U
def test_user_takes_optional_stonk_picks():
    stonk_picks = ["CTSO", "INSG", "ZIM"]
    user = User(stonk_picks=stonk_picks)
    assert len(user.stonk_picks) is 3
    assert "CTSO" in stonk_picks
    assert "INSG" in stonk_picks
    assert "ZIM" in stonk_picks

### test 1.3 PASSED ### in User #U
def test_adding_to_stonk_picks():
    user = User()
    stonk = "new stonk"

    result = user.add(stonk)

    assert len(user.stonk_picks) is 1
    assert stonk in user.stonk_picks
    assert result is stonk

### test 1.4 PASSED ### in User #U
def test_removing_from_stonk_picks_returns_stonk():
    bad_stonk = "stonk to remove"
    user = User(
        stonk_picks=["CTSO", "INSG", "ZIM", bad_stonk]
    )

    result = user.remove(bad_stonk)

    assert len(user.stonk_picks) is 3
    assert bad_stonk not in user.stonk_picks
    assert result is bad_stonk

### test 1.5 PASSED ### in User #U
def test_removing_not_found_is_false():
    bad_stonk = "stonk to remove"
    user = User(
        stonk_picks=["CTSO", "INSG", "ZIM"]
    )

    result = user.remove(bad_stonk)

    assert len(user.stonk_picks) is 3
    assert result is False
