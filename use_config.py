from configparser import ConfigParser, ExtendedInterpolation

#config = ConfigParser()
config = ConfigParser(interpolation=ExtendedInterpolation())
config.read('./config/config.ini')


# sections(): 모든 section 리스트 반환
# get(<section_name>,<option_name>): 섹션의 옵션값 str로 반환
# get 대신 config['section_name']['option_name']도 가능
# getint(),getfloat(),getboolean(): int/float/boolean으로 반환
# options(<section_name>):섹션 안의 선택가능한 옵션들반환
# in: 섹션 존재 여부 확인

print(config.sections())  # ['settings', 'db', 'files']
print(config.get('settings', 'secret_key'))  # abc123
print(config.options('settings'))  # ['debug', 'secret_key', 'log_path']


print('db' in config)  # True
if 'db' in config:
    print(config.get('db', 'db_port'), type(config.get('db', 'db_port')))  # 8889 <class 'str'>
    print(int(config.get('db', 'db_port')))  # 8889 (as int)
    print(config.getint('db', 'db_default_port', fallback=3306))  # 3306

print(config.getboolean('settings', 'debug', fallback=False))  # True

print(config.get('files', 'python_path'))
print(config['files']['image_name'])
