'''
Get the list of a hash of group functions as follow
[ {'name': name, 'func': func} ]
this will provide us with catagorizations to work with.
'''

from dictionary.combiner import group_product, func_and, name_concat
from dictionary.dict_helper import get_type, get_first_character, get_first_consonant_sound, get_first_vowel_sound
from string import ascii_lowercase

wordtypes = [
    {'name': 'noun', 'func': lambda x: x},
    {'name': 'verb', 'func': lambda x: x},
    {'name': 'adj', 'func': lambda x: x},
    {'name': 'adj', 'func': lambda x: x},
    {'name': 'adj', 'func': lambda x: x},
]


first_character_types = [
    {
        'name': 'starts-with-%s' % c,
        'func': lambda w: get_first_character(w) == c
    }
    for c in list(ascii_lowercase)
]


