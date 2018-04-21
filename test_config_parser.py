import ConfigParser

# config = ConfigParser.ConfigParser()
config = ConfigParser.RawConfigParser()
config.optionxform = str

config.add_section('Section1')
config.set('Section1', 'An_Int', '15')
config.set('Section1', 'A_Bool', 'true')
config.set('Section1', 'A_Float', '3.1415')
config.set('Section1', 'baz', 'fun')
config.set('Section1', 'bar', 'Python')
config.set('Section1', 'foo', '%(bar)s is %(baz)s!')

# write to file
with open('tmp/config.ini', 'wb') as f:
    config.write(f)
