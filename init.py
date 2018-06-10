'''
Initialize progress.txt with init values.
'''

import os
from progress_editor import init_progress

if __name__ == '__main__' :
    processlist = os.listdir('./writer/wordset')
    processlist.remove('.DS_Store')
    processlist.sort()
    init_progress(processlist)

