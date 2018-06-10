'''
This file defines functions that help you read and write progress.
'''
def write_all_progress(progress_list) :
    '''
    write the progress file.
    '''
    with open('progress.txt', 'w') as f :
        for progress_name, progress_status in progress_list :
            print('%s:%s' % (progress_name, progress_status), file=f)

def init_progress(progressnamelist, initmsg='init') :
    '''
    write the progress file.
    '''
    with open('progress.txt', 'w') as f :
        for progressname in progressnamelist :
            print('%s:%s' % (progressname, initmsg), file=f)

def read_all_progress() :
    '''
    Read the progress file and return a list of
    (progressname, progress_status_str) tuple.
    '''
    progress_list = []
    with open('progress.txt') as f :
        for line in f :
            progress_name, progress_status = line.strip().split(':')
            progress_list += [(progress_name, progress_status)]
    return progress_list


def all_progress_names() :
    '''
    Return a list of all progress names.
    '''
    names = [ name for name, status in read_all_progress() ]
    return names

def unique_check() :
    # we check that all progress names are unique.
    # If they are not, we don't know which one to return!
    names = all_progress_names()
    assert len(names) == len(set(names))

def read_progress(target_progress_name) :
    '''
    read the msg from a progress name
    '''
    unique_check()
    
    # Return the status of the corresponding name
    progress_list = read_all_progress()
    for progress_name, progress_status in progress_list :
        if progress_name == target_progress_name :
            return progress_status

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
    progress_list = read_all_progress()
    for progress_name, progress_status in progress_list :
        if progress_status != 'finished' :
            return progress_name, progress_status

def write_progress(target_progress_name, target_msg) :
    '''
    Modify progress.txt so that the progress message of the 
    target progress name becomes the target message.
    '''
    unique_check()
    # write the progress to the progress name
    progress_list = read_all_progress()
    for i in range(len(progress_list)) :
        progress_name, progress_status = progress_list[i]
        if progress_name == target_progress_name :
            progress_list[i] = (progress_name, target_msg)
    write_all_progress(progress_list)

if __name__ == '__main__' :
    dummylist = ['dummy-%d' % i for i in range(10)]
    init_progress(dummylist)