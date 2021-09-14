# backup
<br>
To install the helm: 
<pre>
    <code>
helm install backintime backup --set env.MODE="'2'" \
--set env.SSH_HOST="192.168.100.7" \
--set env.SSH_USER="imen" \
--set env.SSH_PATH="/home/imen"
    </code>
</pre>
