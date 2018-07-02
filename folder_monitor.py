from time import sleep
import os
import configparser

#
def parse_settings(config_file):
    config_settings = {}
    # parse config file settings
    config = configparser.ConfigParser()
    config.read(config_file)

    for line in config['files']:
        config_settings[line] =  config['files'][line]

    return config_settings

# move filename from /Files to /Transfer
def move(filename):
    pass

# copies filename from /Files to /Transfer
def copy(filename):
    pass

# deletes filename
def delete(filname):
    pass

def file_action(filename):
    for extension in config_settings:
        if filename.endswith('.' + extension):
            action = config_settings[extension]
            if action == "move":
                move(filename)
            elif action == "copy":
                copy(filename)
            elif action == "delete":
                delete(filename)


config_settings = parse_settings('config.ini')

# go to desired directory
cwd = os.getcwd() + "/Files"
os.chdir(cwd)


# check folder each second
while True:
    filenames = os.listdir()
    for filename in filenames:
        file_action(filename)
    try:
        sleep(1)
    except:
        # manual shutdown
        print("==" * 10  + "finished monitoring" + "==" * 10)
        break

