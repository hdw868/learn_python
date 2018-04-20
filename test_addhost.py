import subprocess
# import admin
# if not admin.isUserAdmin():
#     admin.runAsAdmin()


def add_iserver_host(hostname, ip):
    subprocess.call('runas /administrator hostsman -r {}'.format(hostname))
    subprocess.call(
        'runas /administrator hostsman -i {}:{}'.format(hostname, ip))
    subprocess.call(
        'runas /administrator hostsman -l')


ip = '10.244.20.196'
hostname = 'CentOS-DEBUG-RB-10-244-20-196'
add_iserver_host(hostname, ip)
