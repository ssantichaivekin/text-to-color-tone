'''
Initialize progress.txt with init values.
'''

import os
import glob
from progress_editor import init_progress
from writer.segment_word import write_chunks

if __name__ == '__main__' :
    files = glob.glob('./writer/wordset/*')
    for f in files:
        os.remove(f)
    write_chunks()
    processlist = os.listdir('./writer/wordset')
    processlist.remove('.DS_Store')
    processlist.sort()
    init_progress(processlist)

