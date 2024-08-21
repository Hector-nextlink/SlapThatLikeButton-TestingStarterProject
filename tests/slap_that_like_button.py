import pytest 

def slap_that_like_button():
    return "Slapped that like button!"

def test_slap_that_like_button():
    assert slap_that_like_button() == "Slapped that like button!"