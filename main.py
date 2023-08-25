#################################################################################################
#                                                                                               #
#   name:   Jenny Kim                                                                           #
#   email:  yjkim@usc.edu                                                                       #
#                                                                                               #
#   How To: Define global variables - downloads and grading paths                               #
#################################################################################################
import os
from os import path
import re
import zipfile
from pathlib import Path

# TODO: Add path to unzipped assignments folder
PATH_TO_DOWNLOADS = "/Users/jennykim/Downloads/gradebook_20231_itp_115_mm-rp_Assignment1_2023-08-24-18-29-58"

# TODO: Add path to where you want a new grading folder
PATH_TO_GRADING = "/Users/jennykim/Documents/grading/"


# Move files to designated grading folder and removes them from Downloads
def move_files():
    items = os.listdir(PATH_TO_DOWNLOADS)
    if not path.isdir(PATH_TO_GRADING):
        os.mkdir(PATH_TO_GRADING)
    for file in items:
        if file.endswith('.zip'):
            Path(PATH_TO_DOWNLOADS + "/" + file).rename(PATH_TO_GRADING + "/" + file)



def unzip():
    print(os.listdir(PATH_TO_GRADING))
    for item in os.listdir(PATH_TO_GRADING):
        if item.endswith('.zip'):
            with zipfile.ZipFile(PATH_TO_GRADING + "/" + item, 'r') as zip_ref:
                zip_ref.extractall(PATH_TO_GRADING)
                os.remove(PATH_TO_GRADING + "/" + item)


def main():
    move_files()
    unzip()


main()


