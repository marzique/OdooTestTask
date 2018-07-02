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


def file_action(filename):
    print(filename)

config_settings = parse_settings('config.ini')
print(config_settings)

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

