from numpy import genfromtxt

def get_word_list(wordgroup, wordlist) :
    '''
    Iterate through the wordlist using constraint found in
    wordgroup function return a list of words that is in both
    the wordlist and wordgroup.
    '''
    func = wordgroup['func']
    newlist = list(filter(func, wordlist))
    return newlist

def get_pixel_list(wordlist) :
    '''
    From a list of word, get a continuous list of pixel.
    The pixels are concatenated from those in each word.
    '''
    alllist = []
    for word in wordlist :
        pixellist = []
        centers = genfromtxt('./assets/info/%s-centers.csv' % word, delimiter = ',')
        hist = genfromtxt('./assets/info/%s-hist.csv' % word, delimiter = ',')
        for i in range(len(centers)) :
            prob = int(hist[i] * 100)
            pixellist += [centers[i] for _ in range(prob)]
        alllist += pixellist
    return alllist

def gen_process(wordgroup, wordlist) :
    name = wordgroup['name']
    pixellist = get_pixel_list(get_word_list(wordgroup, wordlist))
    return name, pixellist

if __name__ == '__main__' :
    wordlist = ['apple', 'banana', 'beautiful', 'cat', 'run', 'walk']
    from dictionary.word_group_generator import all_groups
    for wordgroup in all_groups :
        name = wordgroup['name']
        words = get_word_list(wordgroup, wordlist)
        print(name, ':', words)
