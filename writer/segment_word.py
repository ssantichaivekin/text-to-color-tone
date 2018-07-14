from nltk.corpus import cmudict
from nltk.corpus import wordnet

# get pronounciation dictionary
pronun_word_list = list(cmudict.dict().keys())
# get definition dictionary
def_word_list= [ word for word in wordnet.words() ]

def get_all_words() :
    '''
    We want words that appear on both dict.
    '''

    all_words = []
    with open('count_1w.txt') as f :
        for i, line in zip(range(31000), f) :
            word, count = line.split()
            all_words += [word]
    # all_words = list(set(pronun_word_list + def_word_list))
    all_words = list(filter(str.isalpha, all_words))
    all_words = sorted(all_words)
    return all_words


def write_chunks(sep=1000, wordmax=1000000) :
    '''
    Write all chunks into a seperate file.
    '''
    words = get_all_words()
    for start in range(0, len(words), sep) :
        if start > wordmax :
            return
        wordset = words[start:start+sep]
        filename = 'wordset-%06d.txt' % start
        pathname = './writer/wordset/'
        fullname = pathname + filename
        with open(fullname, 'w') as f :
            for word in wordset :
                f.write('%s\n' % word)

def read_chunks(chunk_i) :
    '''
    Read the ith chuck into a list of string.
    '''
    return

if __name__ == '__main__' :
    write_chunks()