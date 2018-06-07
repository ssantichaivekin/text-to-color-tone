# 0. cd to the directory containing THIS file.
# 1. Create necessary folders in case they are not already created.
# This includes creating the assets/info and assets/pics folders.
# 2. Run the function that saves images to files, according to parameters.

# Make the directories
import os
from writer.write_word import save_info

loc = os.path.abspath(__file__)
# just strip everything but leave /
os.chdir(loc.strip('save_image_info.py'))
os.makedirs('./assets/info/', exist_ok=True)
os.makedirs('./assets/pics/', exist_ok=True)

# Check the current progress and run the program to continue the progress

if __name__ == '__main__' :
    save_info('hippie')