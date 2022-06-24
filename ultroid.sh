
kill -9 `ps -efjH |grep "[p]ython3 -m pyUltroid"|awk '{print $2}'`

nohup python3 -m pyUltroid > ~/Utroid.log&lnav ~/Utroid.log
