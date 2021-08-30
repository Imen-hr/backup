from kubernetes import client, config
import os
# Configs can be set in Configuration class directly or using helper utility
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
