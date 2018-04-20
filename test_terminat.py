import paramiko


def ssh_pty_command(cmd, ip, username, passwd=None, key_filename=None):
    """run ssh.exec_command with realtime output and return exit_code."""
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        logging.debug('Connecting to remote server {}...'.format(ip))
        ssh.connect(ip, 22, username, password=passwd,
                    key_filename=key_filename, timeout=5)
        stdin, stdout, stderr = ssh.exec_command(cmd, get_pty=True)
        logging.info('ssh_In: {}'.format(cmd))
        # print '$: {}'.format(cmd)
        for line in iter(stdout.readline, ""):
            logging.info('ssh_Out: {}'.format(
                line.rstrip('\n').encode('utf-8')))
        for err in iter(stderr.readline, ""):
            logging.error('ssh_Error: {}'.format(
                err.rstrip().encode('utf-8')))
        exit_code = stdout.channel.recv_exit_status()
        logging.debug('Task exit with code {}.\n'.format(exit_code))
        return exit_code
    except Exception as err:
        logging.error('*** Caught SSH exception: %s: %s' %
                      (err.__class__, err))
        raise
    finally:
        ssh.close()
