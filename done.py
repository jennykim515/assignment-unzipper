import shutil
from main import PATH_TO_GRADING, PATH_TO_DOWNLOADS

"""
Deletes the grading folder 
"""


def delete():
    try:
        shutil.rmtree(PATH_TO_GRADING)
        shutil.rmtree(PATH_TO_DOWNLOADS)
    except:
        print('Error while deleting directory')


delete()
