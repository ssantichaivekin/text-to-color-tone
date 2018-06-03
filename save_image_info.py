# 1. Create necessary folders in case they are not already created.
# This includes creating the assets/info and assets/pics folders.

# 2. Run the function that saves images to files, according to parameters.

# Make the directories
import os
os.makedirs('./assets/info/', exist_ok=True)
os.makedirs('./assets/pics/', exist_ok=True)

# Check the current progress and run the program to continue the progress