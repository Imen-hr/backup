# backup
<br>
To install the helm: 
<pre>
    <code>
git clone https://github.com/Imen-hr/backup
cd backup
helm install backintup backintimechart --set env.mode="'2'" --set env.ssh_host="192.168.100.7" --set env.ssh_user="imen" --set env.ssh_pass="imen" --set env.ssh_path="/home/imen"
    </code>
</pre>
mode : 
Allowed Values: 0|1|2|4|7|10|12|14|16|18|19|20|25|27|30|40|80
             Which  schedule  used  for  crontab.
              0 = Disabled
              1 = at every boot
              2 = every 5 minute
              4 = every 10 minute
              7 = every 30 minute
             10 = every hour
             12 = every 2 hours
             14 = every 4 hours
             16 = every 6 hours
             18 = every 12 hours
             19 = custom defined hours
             20 = every day
             25 = daily anacron
             27 = when drive get connected
             30 = every week
             40 = every month
             80 = every year

             Default: 2
ssh_host :
ip address of the host where snapshots will be saved

ssh_user :
username of the host where snapshots will be saved

ssh_pass:
password

ssh_path:
where exactly save the snapshot


# About Config file :
<br>
some configurations you may needto know :
profile1.snapshots.check_for_changes
             Type: bool      Allowed Values: true|false
             Perform a dry-run before taking snapshots. Don't take a new snapshot if nothing  has
             changed. Only valid with profile1.snapshots.full_rsync = false

             Default: false
profile1.snapshots.mode
             Type: str       Allowed Values: local|local_encfs|ssh|ssh_encfs
             Use mode (or backend) for this snapshot. Look at 'man backintime' section 'Modes'.

             Default: ssh


profile1.snapshots.cron.ionice
             Type: bool      Allowed Values: true|false
             Run cronjobs with 'ionice  -c2  -n7'.  This  will  give  BackInTime  the  lowest  IO
             bandwidth priority to not interupt any other working process.

             Default: true
profile1.snapshots.include.size
             Type: int       Allowed Values: 0-99999
             Quantity of profile.snapshots.include.<I> entries.

             Default: 20
<br>
For more informations check :
http://manpages.ubuntu.com/manpages/bionic/man1/backintime-config.1.html


