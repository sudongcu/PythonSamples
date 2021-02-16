from configparser import ConfigParser

config = ConfigParser()

config['settings'] = {
    'debug': 'true',
    'secret_key': 'abc123',
    'log_path': '/my_app/log',
    'python_version': '3',
    'packages_path': '/usr/local'
}

config['db'] = {
    'db_name': 'myapp_dev',
    'db_host': 'localhost',
    'db_port': '8889'
}

config['files'] = {
    'use_cdn': 'false',
    'images_path': '/my_app/images',
    'image_name': 'dobby',
    'python_path': '${settings:packages_path}/bin/python${settings:python_version}'
}

config['url'] = {
    'host': 'http://jsonplaceholder.typicode.com',
    'photo_domain':'${url:host}/photos',
    'post_domain':'${url:host}/posts',
    'todo_domain':'${url:host}/todos',
    'user_domain':'${url:host}/users'
}

config['nameurl'] = {
    'host': 'http://names.drycodes.com',
    'large': '${nameurl:host}/50',
    'medium': '${nameurl:host}/25',
    'small': '${nameurl:host}/10'
}

with open('./config/config.ini', 'w') as f:
      config.write(f)
