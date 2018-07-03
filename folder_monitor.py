from time import sleep
from shutil import copyfile, move
import os
import configparser

# parse cfg from file
def parse_settings(config_file):
    config_settings = {}
    # parse config file settings
    config = configparser.ConfigParser()
    config.read(config_file)

    for line in config['files']:
        config_settings[line] =  config['files'][line]

    return config_settings

# move filename from /Files to /Transfer
def move_file(filename):
    move(cwd + "/" + filename, transfer_folder + "/" + filename)

# copies filename from /Files to /Transfer (overwrites if file already exists in /Transfer)
def copy_file(filename):
    copyfile(cwd + "/" + filename, transfer_folder + "/" + filename)

# deletes filename
def delete_file(filname):
    os.remove(filename)

# compares file extension with needed action from dict and calls move/copy/delete func
def file_action(filename):
    for extension in config_settings:
        if filename.endswith('.' + extension):
            action = config_settings[extension]
            if action == "move":
                move_file(filename)
                print(filename, "moved")

            elif action == "copy":
                copy_file(filename)
                print(filename, "copied")

            elif action == "delete":
                delete_file(filename)
                print(filename, "deleted")



config_settings = parse_settings('config.ini')

# go to desired directory
cwd = os.getcwd() + "/Files"

# where we copy/move files
transfer_folder = os.getcwd() + "/Transfer"
os.chdir(cwd)


print("==" * 10  + "monitoring starts" + "==" * 10)
# check folder each second
while True:
    filenames = os.listdir()
    for filename in filenames:
        file_action(filename)
    try:
        # 1 sec
        sleep(1)
    except:
        # manual shutdown
        print("==" * 10  + "finished monitoring" + "==" * 10)
        break

