'''
Get the list of a hash of group functions as follow
[ {'name': name, 'func': func} ]
this will provide us with catagorizations to work with.
'''

from dictionary.combiner import group_product, func_and, name_concat
from dictionary.dict_helper import is_type, get_first_character, get_first_consonant_sound, get_first_vowel_sound
from dictionary.dict_helper import all_consonant_sound, all_vowel_sound
from string import ascii_lowercase

wordtypes = [
    # ADJ, ADJ_SAT, ADV, NOUN, VERB = 'a', 's', 'r', 'n', 'v'
    {'name': 'noun', 'func': lambda w: is_type(w, 'n')},
    {'name': 'verb', 'func': lambda w: is_type(w, 'v')},
    # we should merge adj and adj-sat
    {'name': 'adj', 'func': lambda w: is_type(w, 'a') or is_type(w, 's')},
    {'name': 'adv', 'func': lambda w: is_type(w, 'r')},
]

first_character_alpha = [
    {
        'name': 'starts-with-%s' % character,
        'func': lambda w, character=character: get_first_character(w) == character
    }
    for character in list(ascii_lowercase)
]

first_con_sound = [
    {
        'name': 'first-con-sound-%s' % sound,
        'func': lambda w, sound=sound: get_first_consonant_sound(w) == sound
    }
    for sound in all_consonant_sound()
]

first_vowel_sound = [
    {
        'name': 'first-vowel-sound-%s' % sound,
        'func': lambda w, sound=sound: get_first_vowel_sound(w) == sound
    }
    for sound in all_vowel_sound()
]

# product of groups :
word_type_first_alpha = group_product(func_and, name_concat, wordtypes, first_character_alpha)
word_type_first_con_sound = group_product(func_and, name_concat, wordtypes, first_con_sound)
word_type_first_vow_sound = group_product(func_and, name_concat, wordtypes, first_vowel_sound)

# all groups :
all_groups = []
all_groups += wordtypes + first_character_alpha + first_con_sound + first_vowel_sound
all_groups += word_type_first_alpha + word_type_first_con_sound + word_type_first_vow_sound

