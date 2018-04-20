import configparser

config = configparser.ConfigParser()
config['settings'] = {'letter': '$'}
with open('settings.ini', 'w') as configfile:
    config.write(configfile)
