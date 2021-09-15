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
<br>mode :  
<br>Allowed Values: 0|1|2|4|7|10|12|14|16|18|19|20|25|27|30|40|80
<br>             Which  schedule  used  for  crontab.
<br>              0 = Disabled
<br>              1 = at every boot
<br>              2 = every 5 minute
<br>              4 = every 10 minute
<br>              7 = every 30 minute
<br>             10 = every hour
<br>             12 = every 2 hours
<br>             14 = every 4 hours
<br>             16 = every 6 hours
<br>             18 = every 12 hours
<br>             19 = custom defined hours
<br>             20 = every day
<br>             25 = daily anacron
<br>             27 = when drive get connected
<br>             30 = every week
<br>             40 = every month
<br>             80 = every year
<br>
             Default: 2

<br>
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
<br>some configurations you may need to know :

<br>
<br>profile1.snapshots.check_for_changes
<br>             Type: bool      Allowed Values: true|false
<br>             Perform a dry-run before taking snapshots. Don't take a new snapshot if nothing  has
<br>             changed. Only valid with profile1.snapshots.full_rsync = false
<br>
<br>             Default: false
<br>profile1.snapshots.mode
<br>             Type: str       Allowed Values: local|local_encfs|ssh|ssh_encfs
<br>             Use mode (or backend) for this snapshot. Look at 'man backintime' section 'Modes'.
<br>
             Default: ssh
<br>
<br>
<br>profile1.snapshots.cron.ionice
<br>             Type: bool      Allowed Values: true|false
<br>             Run cronjobs with 'ionice  -c2  -n7'.  This  will  give  BackInTime  the  lowest  IO
<br>             bandwidth priority to not interupt any other working process.
<br>
             Default: true
<br>profile1.snapshots.include.size
<br>             Type: int       Allowed Values: 0-99999
<br>             Quantity of profile.snapshots.include.<I> entries.
<br>
             Default: 20
<br>
For more informations check :
http://manpages.ubuntu.com/manpages/bionic/man1/backintime-config.1.html


