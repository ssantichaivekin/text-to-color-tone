'''
This file defines functions that help you read and write progress.
'''

def init_progress(progressnamelist, initmsg='init') :
    '''
    write the progress file.
    '''
    with open('progress.txt', 'w') as f :
        for progressname in progressnamelist :
            print('%s:%s' % (progressname, initmsg), file=f)

def all_progress() :
    '''
    Return a list of all progress names.
    '''
    return

def read_progress(progressname) :
    '''
    read the msg from a progress name
    '''
    return

def log_error(progressname, error) :
    '''
    Log an error from exception.
    '''
    with open('errorlog.txt', 'w') as f :
        print(progressname, file=f)
        print(error, file=f)

def get_next_process() :
    '''
    Return the first progressname that is not finished
    '''
    return

def write_progress(progressname, msg) :
    # write the progress to the progress name
    return

if __name__ == '__main__' :
    dummylist = ['dummy-%d' % i for i in range(10)]
    init_progress(dummylist)