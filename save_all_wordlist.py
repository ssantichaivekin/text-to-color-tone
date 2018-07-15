from dictionary.get_pixel_list import get_word_list

def save_all_wordlist(all_wordgroup, wordlist, targetpath) :
    '''
    For each of the wordgroup, we save its wordlist to a file.
    '''
    for wordgroup in all_wordgroup :
        name = wordgroup['name']
        wordlist2 = get_word_list(wordgroup, wordlist)
        func = wordgroup['func']
        filename = targetpath + name + '-list.txt'
        with open(filename, 'w') as f :
            for word in wordlist2 :
                print(word, file=f)

if __name__ == '__main__' :
    import os
    from writer.segment_word import get_all_words
    wordlist = get_all_words()
    from dictionary.word_group_generator import all_groups

    os.makedirs('./product/wordlist/', exist_ok=True)
    targetpath = './product/wordlist/'
    save_all_wordlist(all_groups, wordlist, targetpath)