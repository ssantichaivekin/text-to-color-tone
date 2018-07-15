from writer.write_word import bulk_save_info

def do_process(filename) :
    '''
    Save the information of every vocab in filename.
    '''
    textlist = []
    with open('./writer/wordset/' + filename) as f :
        for line in f :
            line = line.strip()
            textlist += [line]
    bulk_save_info(textlist)

if __name__ == '__main__' :
    do_process('wordset-000000.txt')