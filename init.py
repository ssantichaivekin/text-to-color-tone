'''
Initialize progress.txt with init values.
'''

import os
import glob
from progress_editor import init_progress
from writer.segment_word import write_chunks

loc = os.path.abspath(__file__)
# just strip everything but leave /
os.chdir(loc.strip('init.py'))
os.makedirs('./assets/info/', exist_ok=True)
os.makedirs('./assets/pics/', exist_ok=True)
os.makedirs('./assets/jsons/', exist_ok=True)


if __name__ == '__main__' :
    files = glob.glob('./writer/wordset/*')
    for f in files:
        os.remove(f)
    if not os.path.isfile('google-api-key.txt') :
        key = input('What is your google api key?')
        with open('google-api-key.txt', 'w') as f :
            f.write(key)
    # Real work starts here >> init :
    write_chunks()
    processlist = os.listdir('./writer/wordset')
    processlist.remove('.DS_Store')
    processlist.sort()
    init_progress(processlist)

