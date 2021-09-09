from kubernetes import client, config
import os
import schedule
import time 

host= os.environ['SNAP_HOST']
ssh_host= os.environ['SSH_HOST']
ssh_path= os.environ['SSH_PATH']
ssh_user= os.environ['SSH_USER']
ssh_pass= os.environ['SSH_PASS']
backintime_args = os.environ['BACKINTIME_ARGS']
mode= os.environ['MODE']

os.system("service cron start")
os.system("service ssh start")
os.system('ssh-keygen -b 3072 -t RSA -N "" -f /root/.ssh/id_rsa')
os.system("sshpass -p %s ssh-copy-id -o StrictHostKeyChecking=no %s@%s"%(ssh_pass,ssh_user,ssh_host))
os.system("backintime check-config ")

with open('config', 'a') as file:
    file.write("profile1.snapshots.ssh.host=%s\n"%ssh_host)
    file.write("profile1.snapshots.ssh.path=%s\n"%ssh_path)
    file.write("profile1.snapshots.ssh.user=%s\n"%ssh_user)
    file.write("profile1.snapshots.automatic_backup_mode=%s\n"%mode)

def conf_pv():
    os.system("cp config /root/.config/backintime")
    config.load_incluster_config()

    v1 = client.CoreV1Api()
    ret = v1.list_persistent_volume(watch=False)
    j=0
    for i in ret.items:
        os.system("mkdir -p %s"%(i.spec.nfs.path))
        os.system("mount %s:%s %s"%(i.spec.nfs.server,i.spec.nfs.path,i.spec.nfs.path))
        with open('/root/.config/backintime/config', 'a') as file:
              file.write("profile1.snapshots.include.%s.type=0\n"%(j))
              file.write("profile1.snapshots.include.%s.value=%s\n"%(j,i.spec.nfs.path))
        j=j+1
conf_pv()
schedule.every(5).minutes.do(conf_pv)
os.system("log 'Checking configuration of backintime'")
os.system("backintime check-config %s"%backintime_args )
os.system('log "Starting actual backup with backintime"')
os.system("backintime backup %s"%backintime_args)

while 1:
    schedule.run_pending()
    time.sleep(1)
