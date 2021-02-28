import configparser


def write_configparser():
    config = configparser.ConfigParser()

    config['DEFAULT'] = {
        'debug' : "True",
    }

    config['web_server'] = {
        'host' : '127.0.0.1',
        'port' : 80,
    }

    config['db_server'] = {
        'host' : '127.0.0.1',
        'port' : 3306
    }

    with open('config.ini', 'w') as config_file:
        config.write(config_file)

def read_configparser():
    config = configparser.ConfigParser()
    config.read('config.ini')
    print(config['web_server'])
    print(config['web_server']['host'])

write_configparser()
read_configparser()