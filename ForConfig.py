import configparser

config = configparser.ConfigParser()
# letter - символ, который будет показывать, что это слово было
# последним в тексте и для него нельзя выбрать пару.
config['settings'] = {'letter': '$'}
with open('settings.ini', 'w') as configfile:
    config.write(configfile)
