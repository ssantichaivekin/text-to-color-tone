from nltk.corpus import cmudict

# get CMU pronouncing dictionary
dictionary = cmudict.dict()

def write_chunks() :
    '''
    Write all chunks into a seperate file.
    '''
    words = (list)(dictionary.keys())
    for start in range(0, len(words), 1000) :
        wordset = words[start:start+1000]
        filename = 'wordset-%d.txt' % start
        pathname = './writer/wordset/'
        fullname = pathname + filename
        with open(fullname, 'w') as f :
            f.writelines(wordset)

def read_chunks(chunk_i) :
    '''
    Read the ith chuck into a list of string.
    '''
    return

if __name__ == '__main__' :
    write_chunks()