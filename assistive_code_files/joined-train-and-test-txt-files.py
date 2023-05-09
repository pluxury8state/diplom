

"""
Course:  Training YOLO v3 for Objects Detection with Custom Data

Section-4
Creating Custom Dataset in YOLO format
File: joined-train-and-test-txt-files.py
"""


# Creating files train.txt and test.txt for joined datasets
# for training in Darknet framework
#
# Algorithm:
# Setting up full path --> List of paths -->
# --> Extracting 15% of paths to save into test.txt file -->
# --> Writing paths into train and test txt files
#
# Result:
# Files train.txt and test.txt with full paths to images


# Importing needed library
import os
import random


"""
Start of:
Setting up full path to directory with joined images
"""

# Full or absolute path to the folder with labelled and downloaded images
# Find it with second Py file getting-full-path.py
# Pay attention! If you're using Windows, yours path might looks like:
# r'C:\Users\my_name\Downloads\Labelled-Custom'
# or:
# 'C:\\Users\\my_name\\Downloads\\Labelled-Custom'
full_path_to_joined_images = \
    r'D:\Pycharm_Projects\Make_model_with_YOLO\imgs\joined_bolts'

"""
End of:
Setting up full path to directory with joined images
"""


"""
Start of:
Getting list of full paths to joined images
"""

# Check point
# Getting the current directory
# print(os.getcwd())

# Changing the current directory
# to one with images
os.chdir(full_path_to_joined_images)

# Check point
# Getting the current directory
# print(os.getcwd())

# Defining list to write paths in
p = []

# Using os.walk for going through all directories
# and files in them from the current directory
# Fullstop in os.walk('.') means the current directory
for current_dir, dirs, files in os.walk('.'):
    # Going through all files
    for f in files:
        # Checking if filename ends with '.jpeg' or '.jpg'
        if f.endswith('.jpeg') or f.endswith('.jpg'):
            # Preparing path to save into train.txt file
            # Pay attention!
            # If you're using Windows, it might need to change
            # this: + '/' +
            # to this: + '\' +
            # or to this: + '\\' +
            path_to_save_into_txt_files = \
                full_path_to_joined_images + '\\' + f

            # Appending the line into the list
            # We use here '\n' to move to the next line
            # when writing lines into txt files
            p.append(path_to_save_into_txt_files + '\n')

# shuffle sequence
random.shuffle(p)


# Slicing first 15% of elements from the list
# to write into the test.txt file
p_test = p[:int(len(p) * 0.15)]

# Deleting from initial list first 15% of elements
p_valid = p[int(len(p) * 0.15):int(len(p) * 0.3)]

# valid_data_set
p_train = p[int(len(p) * 0.3):]

print(list(map(len, (p_test, p_train,p_valid, p))))

"""
End of:
Getting list of full paths to joined images
"""


"""
Start of:
Creating train.txt and test.txt files
"""

# Creating file train.txt and writing 85% of lines in it
with open('train.txt', 'w') as train_txt:
    # Going through all elements of the list
    for e in p_train:
        # Writing current path at the end of the file
        train_txt.write(e)

# Creating file test.txt and writing 15% of lines in it
with open('test.txt', 'w') as test_txt:
    # Going through all elements of the list
    for e in p_test:
        # Writing current path at the end of the file
        test_txt.write(e)

"""
End of:
Creating train.txt and test.txt files
"""
#
# with open('valid.txt', 'w') as test_txt:
#     # Going through all elements of the list
#     for e in p_valid:
#         # Writing current path at the end of the file
#         test_txt.write(e)
