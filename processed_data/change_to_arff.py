import os


def get_all_file_paths(rootDir):

    for dir_, _, files in os.walk(rootDir):
        for fileName in files:
            relDir = os.path.relpath(dir_, rootDir)
            relFile = os.path.join(rootDir, relDir, fileName)
            print relFile


if __name__ == "__main__":

    get_all_file_paths('./CSV/')
