# 0. cd to the directory containing THIS file.
# 1. Create necessary folders in case they are not already created.
# This includes creating the assets/info and assets/pics folders.
# 2. Run the function that saves images to files, according to parameters.

# Make the directories
import os
from writer.write_word import save_info

loc = os.path.abspath(__file__)
os.chdir(loc.strip('save_image_info.py'))

# Check the current progress and run the program to continue the progress
from progress_editor import get_next_process, has_next_process, write_progress, log_error
from do_process import do_process

if has_next_process() :
    process_name, process_status = get_next_process()
    assert process_status != 'failure'
    try :
        do_process(process_name)
        write_progress(process_name, 'success')
    except BaseException as err :
        log_error(process_name, err)
        write_progress(process_name, 'failure')