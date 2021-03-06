# This file define dict helper functions. The functions
# check a specific characteristic of a word and either
# return a characteristic trait or a boolean value.
# Note that these functions will require the NLTK
# dictionary.

from nltk.corpus import cmudict
from nltk.corpus import wordnet

# get CMU pronouncing dictionary
p_dict = cmudict.dict()

def get_num_syllable(word) :
    '''
    Return the number of syllable a word (string) has.
    Throw KeyError exception if the word is not in the dictionary.
    This only returns the first phoneme of the word in cmudict.
    '''
    word = word.lower()
    # a word may have many pronunciations -- for the sake of
    # simplicity, we can just use the first one
    pronunciation = p_dict[word][0]
    # save the number vowel phone in each phoneme of the word
    # vowel phone will have an in integer at the end
    count_syl = len([phoneme for phoneme in pronunciation if phoneme[-1].isdigit()])
    return count_syl

def is_type(word, pos_type) :
    '''
    Return the type of the word (noun, verb, adjective, etc)
    The list of symbols used are:

    ADJ, ADJ_SAT, ADV, NOUN, VERB = 'a', 's', 'r', 'n', 'v'

    If there are many meaning type a word can take, we choose to use
    the first meaning. For example, the word 'transform' should be
    considered as a verb although it can be considered as a noun.
    '''
    synsets = wordnet.synsets(word)
    if synsets == [] :
        raise KeyError('No word in dictionary')
    for synset in synsets :
        if pos_type == synset.pos() :
            return True
    return False

def get_first_character(word) :
    '''
    Get the first character of a word.
    '''
    return word[0].lower()

def starts_with_vowel(word) :
    '''
    Return whether the string word starts with a vowel or not.
    '''
    vowels = 'aeiou'
    return get_first_character(word) in vowels

def starts_with_consonant(word) :
    '''
    Return whether the string word starts with a consonant or not.
    '''
    return not starts_with_vowel(word)

def all_consonant_sound() :
    '''
    Return  a list of all possible starting consonant sound.
    '''
    cons_list = ['none', 'B', 'CH', 'D', 'DH', 'F', 'G', 'HH', 'JH', 'K'
    , 'L', 'M', 'N', 'NG', 'P', 'R', 'S', 'SH', 'T', 'TH', 'V', 'W', 'Y', 'Z', 'ZH']
    return cons_list

def all_vowel_sound() :
    '''
    Return  a list of all possible starting vowel sound.
    '''
    vow_list = ['none', 'AA', 'AE','AH', 'AO', 'AW', 'AY', 'EH', 'ER','EY'
    , 'IH', 'IY', 'OW', 'OY', 'UH', 'UW'] 
    return vow_list

def get_first_consonant_sound(word) :
    '''
    Return the starting consonant sound (str) of the syllable_index 
    position of the word. The index is counted from 0..n from front 
    to back.
    
    For example, the 0th syllable of the word hippo is [hip] (sound).
    '''
    word = word.lower()
    pronunciation = p_dict[word][0]

    phoneme = pronunciation[0]
    if(not phoneme[-1].isdigit()) :
        return phoneme
    else :
        return 'none'

def get_first_vowel_sound(word) :
    '''
    Return the starting consonant sound (str) of the syllable_index 
    position of the word. The index is counted from 0..n from front 
    to back.
    
    For example, the 1th syllable of the word hippo is [po] (sound).
    '''
    word = word.lower()
    # a word may have many pronunciations -- for the sake of
    # simplicity, we can just use the first one
    pronunciation = p_dict[word][0]
    for phoneme in pronunciation :
        if(phoneme[-1].isdigit()) :
            return phoneme[:-1]
    # Don't know why, but these words in cmudict does not have a vowel sound
    # {'fs', 'mmmm', 'shh', 'ths'}
    return 'none'

# Test cases:
if __name__ == '__main__' :
    assert(get_first_consonant_sound('United') == 'Y')
    assert(get_first_vowel_sound('United') == 'UW')
    assert get_num_syllable("Acceleration") == 5
    assert get_first_character('Game') == 'g'
    assert starts_with_consonant('Hello') == True 
    assert starts_with_consonant('hello') == True
    assert starts_with_consonant('University') == False
    assert starts_with_consonant('university') == False
    assert get_first_consonant_sound('hello') == 'HH'
    assert get_first_vowel_sound('hello') == 'AH'
    assert get_type('dog') == 'n'
    assert get_type('beautiful') == 'a'
    assert all_consonant_sound() == ['none', 'B', 'CH', 'D', 'DH', 'F', 'G', 'HH', 'JH', 'K'
    , 'L', 'M', 'N', 'NG', 'P', 'R', 'S', 'SH', 'T', 'TH', 'V', 'W', 'Y', 'Z', 'ZH']
    assert all_vowel_sound() == ['none', 'AA', 'AE','AH', 'AO', 'AW', 'AY', 'EH', 'ER','EY'
    , 'IH', 'IY', 'OW', 'OY', 'UH', 'UW']
    all_consonant_arr = set([get_first_consonant_sound(x) for x in list(p_dict.keys()) ])
    assert all_consonant_arr == set(all_consonant_sound())
    all_vowel_arr = set([get_first_vowel_sound(x) for x in list(p_dict.keys()) ])
    assert all_vowel_arr == set(all_vowel_sound())

