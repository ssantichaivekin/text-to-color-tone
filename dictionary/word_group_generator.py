'''
Get the list of a hash of group functions as follow
[ {'name': name, 'func': func} ]
this will provide us with catagorizations to work with.
'''

from dictionary.combiner import group_product, func_and, name_concat
from dictionary.dict_helper import get_type, get_first_character, get_first_consonant_sound, get_first_vowel_sound
from dictionary.dict_helper import all_consonant_sound, all_vowel_sound
from string import ascii_lowercase

# TODO: write the lambdas!
wordtypes = [
    {'name': 'noun', 'func': lambda x: x},
    {'name': 'verb', 'func': lambda x: x},
    # we should merge adj and adj-sat
    {'name': 'adj', 'func': lambda x: x},
    {'name': 'adj-sat', 'func': lambda x: x},
    {'name': 'adj', 'func': lambda x: x},
]

first_character_types = [
    {
        'name': 'starts-with-%s' % character,
        'func': lambda w: get_first_character(w) == character
    }
    for character in list(ascii_lowercase)
]

first_con_sound = [
    {
        'name': 'first-con-sound-%s' % sound,
        'func': lambda w: get_first_consonant_sound(w) == sound
    }
    for sound in all_consonant_sound()
]

first_vowel_sound = [
    {
        'name': 'first-vowel-sound-%s' % sound,
        'func': lambda w: get_first_vowel_sound(w) == sound
    }
    for sound in all_vowel_sound()
]


