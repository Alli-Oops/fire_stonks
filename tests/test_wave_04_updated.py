############### TEST WAVE 4 (5 tests) P????? #### #C??????
import pytest
from fire_stonks.user import User
from fire_stonks.stonk import Stonk
from fire_stonks.duediligence import DueDiligence

### test 4.1 PASSED ### in User #C
def test_user_has_influence_count_with_zero_default():
    user = User()
    assert int(user.influence_count) is 0

### test 4.2 PASSED ### in Stonk #C
def test_stonk_has_copy_count_with_zero_default():
    stonk = Stonk()
    assert int(stonk.copy_count) is 0

### test 4.3 ### in User #C
def test_copy_stonk_increase_correct_influence_count_by_one():
    user = User(stonk_picks = [])
    
    zim_dd_website = DueDiligence("Top Buys In Shipping: Review With J Mintzmyer", "Cited Source", "https://seekingalpha.com/article/4407925-top-buys-in-shipping-review-j-mintzmyer-podcast-transcript")
    zim_dd_youtube = DueDiligence("ZIM Integrated Shipping Going Public January 28 2021", "User Source", "https://www.youtube.com/watch?v=rRKnGvB_Ibw")
    zim = Stonk("ZIM", research = [zim_dd_website, zim_dd_youtube], copy_count=0)
    influencer = User(stonk_picks = [zim])
    nice_stonk = influencer.stonk_picks[0]
    result = user.copy_stonk(influencer, nice_stonk)

    assert zim in user.stonk_picks
    assert user.influence_count == 0
    assert influencer.influence_count == 1
    assert result is True

### test 4.3 ### in User #C
def test_copy_stonk_increase_nice_stonk_copy_count_by_one():
    user = User(stonk_picks = [])

    zim_dd_website = DueDiligence("Top Buys In Shipping: Review With J Mintzmyer", "Cited Source", "https://seekingalpha.com/article/4407925-top-buys-in-shipping-review-j-mintzmyer-podcast-transcript")
    zim_dd_youtube = DueDiligence("ZIM Integrated Shipping Going Public January 28 2021", "User Source", "https://www.youtube.com/watch?v=rRKnGvB_Ibw")
    zim = Stonk("ZIM", research = [zim_dd_website, zim_dd_youtube], copy_count=0)
    influencer = User(stonk_picks = [zim])
    nice_stonk = influencer.stonk_picks[0]
    
    result = user.copy_stonk(influencer, nice_stonk)

    assert zim in user.stonk_picks
    assert zim.copy_count == 1
    assert user.stonk_picks[0].copy_count == 1
    assert influencer.stonk_picks[0].copy_count == 1
    assert result is True

### test 4.5 ### in User 
def test_adds_influencers_unique_research_if_nice_stonk_already_in_stonk_picks():
    gme_dd_website = DueDiligence("GameStop Corp. CI A", "Cited Source", "https://www.marketwatch.com/investing/stock/gme")
    primary_gme = Stonk("GME", research = [gme_dd_website], copy_count=0)
    primary_user = User(stonk_picks = [primary_gme])
    
    gme_dd_youtube = DueDiligence("GME: The Big Short SQUEEZE", "User Source", "https://www.youtube.com/channel/UC0patpmwYbhcEUap0bTX3JQ")
    influencers_gme = Stonk("GME", research = [gme_dd_youtube], copy_count=0)
    roaring_kitty = User(stonk_picks = [influencers_gme])

    nice_stonk = roaring_kitty.stonk_picks[0]
    
    result = primary_user.copy_stonk(roaring_kitty, nice_stonk)
    
    assert primary_gme in primary_user.stonk_picks
    assert primary_gme not in roaring_kitty.stonk_picks
    assert primary_gme.research[-1] == gme_dd_youtube
    assert len(primary_gme.research) == 2

    assert influencers_gme in roaring_kitty.stonk_picks
    assert influencers_gme not in primary_user.stonk_picks
    assert len(influencers_gme.research) == 1

    assert result is True
