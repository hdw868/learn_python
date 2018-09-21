import sys
import argparse


def main(args=sys.argv[1:]):
    try:
        # get ruining argv
        parser = argparse.ArgumentParser()
        group = parser.add_mutually_exclusive_group()
        group.add_argument(
            "-t", "--test", action="store_true",
            help='test mode, it will run test and update test result to DB and Rally')
        group.add_argument(
            "-c", '--custom', action='store_true',
            help='custom mode, it will run the test with pre-defined warehouse.json file'
                 ' in the test suit and skip the destroy warehouse step.')
        group.add_argument(
            "-d", '--debug', action='store_true',
            help='debug mode, aka. interactive mode which will pause at every key step'
                 ' and wait for your input!')
        parser.add_argument(
            "--tags", metavar='tags', nargs='?', type=str,
            help="run test scenarios that match the tags, by default, it only runs scenario tagged with 'ERT'")
        parser.add_argument(
            "config_file", metavar='configuration file', nargs='?', type=str,
            help="run test with specify configuration")
        group.add_argument(
            "--just-test", action='store_true', dest='just_test',
            help="skip init environment and restore metadata steps etc, go straight forward to update db and test steps")
        # get the running mode
        _args = parser.parse_args(args)
        config_file = _args.config_file
        _tags = _args.tags
        if _args.test:
            _mode = 'test'
        elif _args.custom:
            _mode = 'custom'
        elif _args.debug:
            _mode = 'debug'
        elif _args.just_test:
            _mode = 'just_test'
        else:
            _mode = 'normal'

        print _mode, _tags, config_file
    except Exception:
        pass


if __name__ == '__main__':
    main()
