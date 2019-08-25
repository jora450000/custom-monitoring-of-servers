#!/bin/sh

echo `date +%D`  `date +%R` test servers start     >> /var/log/moni.log
#office
/usr/bin/python /var/moni/moni.py tcp 192.168.1.98:25       >> /var/log/moni.log  
/usr/bin/python /var/moni/moni.py tcp 192.168.1.100:3389    >> /var/log/moni.log  
/usr/bin/python /var/moni/moni.py tcp 192.168.1.231:80      >> /var/log/moni.log 
/usr/bin/python /var/moni/moni.py tcp 192.168.1.2:445      >> /var/log/moni.log 

 
/usr/bin/python /var/moni/moni.py tcp 192.168.7.133:3389     >> /var/log/moni.log 


/usr/bin/python /var/moni/moni.py tcp 192.168.7.120:3389   >> /var/log/moni.log


/usr/bin/python /var/moni/moni.py tcp 192.168.7.252:8291 "li_mk_router"   >> /var/log/moni.log


 /usr/bin/python /var/moni/moni.py tcp 192.168.7.31:5005 "big screen lcd"   >> /var/log/moni.log



/usr/bin/python /var/moni/moni.py tcp 192.168.7.2:3389     >> /var/log/moni.log


/usr/bin/python /var/moni/moni.py tcp 192.168.6.3:3389  "ALTAIR SERVER"  >> /var/log/moni.log

/usr/bin/python /var/moni/moni.py tcp 192.168.6.2:3389   "DEMOS SERVER"  >> /var/log/moni.log


/usr/bin/python /var/moni/moni.py tcp 192.168.9.254:22 "berd.."    >> /var/log/moni.log


/usr/bin/python /var/moni/moni.py tcp 192.168.9.254:22 "raz.."    >> /var/log/moni.log



/usr/bin/python /var/moni/moni.py tcp 192.168.9.254:22 "zue..."    >> /var/log/moni.log



/usr/bin/python /var/moni/moni.py tcp 192.168.8.254:22 "nizhegor"    >> /var/log/moni.log

/usr/bin/python /var/moni/moni.py tcp 192.168.11.1:22 "helga"    >> /var/log/moni.log


#sites
/usr/bin/python /var/moni/moni.py http  http:/net.ru    >> /var/log/moni.log   
/usr/bin/python /var/moni/moni.py http  http://urta.ru        >> /var/log/moni.log  
/usr/bin/python /var/moni/moni.py http  http://rryua.ru        >> /var/log/moni.log  

#/usr/bin/python /var/moni/moni.py http  http://www.galatepla.ru    >> /var/log/moni.log
/usr/bin/python /var/moni/moni.py page  www.mysite.ru    >> /var/log/moni.log   



echo `date  +%D` `date  +%R` test servers stop    >> /var/log/moni.log
