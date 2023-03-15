# You can write tests here or create new files in this directory with the name test_[something].py
from character import Character

# Tests
# Create a character

def test_create_character():
    c = Character(name)
    assert isinstance(c, Character)

# Character has a name

def test_name_character():
    c = Character('Mufasa')
    assert hasattr(Character(), 'name')

# Character can set name



# Character can have alignment

def test_set_character_alignment():
    c = Character('Phil')
    c.alignment = 'Good'
    assert hasattr(c, 'alignment')

# Character has armor attribute and it defaulted to 10



# Character has hit points (hp) attribute defaulted to 5



# Character needs to be able to attack



# Character rolls a 20, attack succeeds
# Character rolls a 17, beats opp armor, attack succeeds
# Character rolls a 1, opp armor too much, attack fails
# some sort of loop test to test for all rolls



# On successful attack, combatant loses hit points by 1
# On roll = 20, crits times 2 damage
# Check hit points after successful attack, if < 0, dead




