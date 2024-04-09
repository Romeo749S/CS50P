from project import Jack , card_sum , player_ends , dealer_ends
import pytest

player = Jack()

player._cards = ['A', 'A', 'J']
card_sum(player.cards, player) 
print(player._cards)

def test_card_sum():
    assert card_sum(['A', 'Q']) == 21
    assert card_sum(['A', 'A' , 'A' , 'A']) == 14

def test_player_ends():
    with pytest.raises(OSError):
        assert player_ends('A') == 11
        assert player_ends('3') == 3

def test_dealer_ends():
    with pytest.raises(TypeError):
        assert dealer_ends('2') == 11
        assert dealer_ends(3) == 3

        