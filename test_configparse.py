import ConfigParser


def add_custom_dsn(entry, odbc_ini, dsn, driver, database, host, port):
    config = ConfigParser.RawConfigParser()
    config.optionxform = str
    config.read(odbc_ini)
    config.set('ODBC Data Sources', dsn,
               entry)
    config.remove_section(dsn)
    config.add_section(dsn)
    config.set(dsn, 'Driver', driver)
    config.set(dsn, 'Database', database)
    config.set(dsn, 'HostName', host)
    config.set(dsn, 'PortNumber', port)
    with open(odbc_ini, 'w') as configfile:
        config.write(configfile)


def read_config(fname):
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    # config.optionxform = str
    config.read(fname)
    test_suites = config.options('test_suites')
    env_ids = config.options('env_ids')
    mode = config.options('mode')
    return (test_suites, env_ids, mode)


print read_config('config.cfg')
