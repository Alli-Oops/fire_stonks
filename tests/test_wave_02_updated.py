############### TEST WAVE 2 (5 tests) PASSED #### #CORRECT
import pytest
from fire_stonks.stonk import Stonk
from fire_stonks.duediligence import DueDiligence

### test 2.1 PASSED ### in Stonk #U
def test_stonk_has_ticker_default_empty_string():
    stonk = Stonk()
    assert stonk.ticker == ""

### test 2.2 PASSED ### in Stonk #U
def test_stonk_has_research_default_empty_list():
    stonk = Stonk()
    assert stonk.research == []

### test 2.3 PASSED ### in DueDiligence #U
def test_dd_have_blank_default_author():
    resource = "file"
    dd = DueDiligence(resource)
    assert dd.author == ""

### test 2.4 PASSED ### in Stonk #U
def test_get_dd_by_author():
    resource = "website"
    dd_pdf = DueDiligence(resource, author="usersource")
    dd_youtubelink = DueDiligence(resource, author="usersource")
    dd_website = DueDiligence(resource, author="citedsource")
    stonk = Stonk(
        research=[dd_pdf, dd_youtubelink, dd_website]
    )

    user_dds = stonk.get_by_author("usersource")

    assert len(user_dds) is 2
    assert dd_pdf in user_dds
    assert dd_youtubelink in user_dds
    assert dd_website not in user_dds

### test 2.5 PASSED ### in Stonk #U
def test_get_no_matching_dds_by_author():
    resource = "youtube video"
    dd_pdf_a = DueDiligence(resource, author="usersource")
    dd_pdf_b = DueDiligence(resource, author="usersource")
    dd_youtubelink = DueDiligence(resource, author="usersource")
    stonk = Stonk(
        research=[dd_pdf_a, dd_pdf_b, dd_youtubelink]
    )

    cited_dds = stonk.get_by_author("citedsource")

    assert len(cited_dds) is 0
