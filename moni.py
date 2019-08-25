#!/usr/bin/python


from os import system
from sys import argv
from time import asctime

#import sys, traceback
import smtplib
import datetime
import urllib
import urllib2
import httplib
import socket
import re




bot_id = 'input here id'

# Request latest messages

def send_telegram(msg):
    result = urllib2.urlopen("https://api.telegram.org/bot" + bot_id + "/getUpdates").read()
    print result

    url1 = "https://api.telegram.org/bot" + bot_id + "/sendMessage?" + urllib.urlencode({ "chat_id": '211283897', "text": msg })
    # Send a message to a chat room (chat room ID retrieved from getUpdates)
    print url1
    result = urllib2.urlopen(url1).read()
    print result





def dns_test(host):
    """ This function checks to see if a host name has a DNS entry by checking
        for socket info. If the website gets something in return, 
        we know it's available to DNS.
    """
    try:
        socket.gethostbyname(host)
    except socket.gaierror:
        return False
    else:
        return True

def proxy_test(proxy_my):
  try:
   proxy = urllib2.ProxyHandler({'http': proxy_my})
   OPENER = urllib2.build_opener(proxy)
   OPENER.addheaders = [('User-agent', 'Mozilla/5.0')]
   urllib2.install_opener(OPENER)
   req = urllib2.Request(url = "http://www.kernel.org/", data = "")
   resp = urllib2.urlopen(req)
#   urllib2.urlopen('http://ya.ru')
  except Exception as detail:
        print "ERROR:", detail
	proxy_my += "  "+str(detail)
        return False
  else:
        return True

def page_test(host, path="/"):
    """ This function retreives the status code of a website by requesting
        HEAD data from the host. This means that it only requests the headers.
        If the host cannot be reached or something else goes wrong, it returns
        False.
    """
    try:
        conn = httplib.HTTPConnection(host)
        conn.request("HEAD", path)
        if re.match("^[23]\d\d$", str(conn.getresponse().status)):
            return True
    except StandardError:
        return None

def tcp_test(server_info):
    cpos = server_info.find(':')
    try:
        sock = socket.socket()
	sock.settimeout(15.0)
        sock.connect((server_info[:cpos], int(server_info[cpos+1:])))
        sock.close
        return True
    except:
        return False


def http_test(server_info):
    try:
        data = urllib2.urlopen(server_info).read()
        return True
    except:
        return False
 
def server_test(test_type, server_info):
    if test_type.lower() == 'tcp':
        return tcp_test(server_info)
    elif test_type.lower() == 'http':
        return http_test(server_info)
    elif test_type.lower() == 'dns':
        return dns_test(server_info)
    elif test_type.lower() == 'page':
        return page_test(server_info)
    elif test_type.lower() == 'proxy':
        return proxy_test(server_info)


def send_error(test_type, server_info, comment):

    sender = 'root@evrasia.ufanet.ru'
    receivers = 'admin@evrasia.ufanet.ru'


    subj = server_info + '    '+ asctime()
    date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )

    message_text = "ALARM\n"+ server_info+ " "+comment+ "\nNO TEST   " + test_type+ "  \n\n"

    msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( sender, receivers, subj, date, message_text )

    print subj + message_text

    # for good sleeping!!!    send after am7:00 in workdays and after am09:00 in weekend
    now = datetime.datetime.now()    
    if (now.hour > 8) and (now.minute < 5)  or  ((now.hour > 6) and ( now.weekday() < 5 ) and (now.minute > 32)) :
#         system('/var/moni/yowsup-cli demos  -c /var/moni/config1 -s  79174707723 "%s \n %s" ' % (subj,message_text))
#	print "Telegram test"
	send_telegram(date +"\n"+ message_text) 

    try:
        smtp = smtplib.SMTP('192.168.1.98')
	smtp.sendmail(sender, receivers, msg)
        smtp.quit()
	print msg
	print "Successfully sent email to "+receivers 
    except SMTPException:
        print "Error: unable to send email"
    




#    system('echo "%s" | mail -s "%s" %s' % (message, subject, email_address))

if __name__ == '__main__':
  if len(argv) < 3:
        print('Wrong number of arguments.')
  elif not server_test(argv[1], argv[2]):
        if len(argv)==4:
	     send_error(argv[1], argv[2], argv[3])
        else:
	     send_error(argv[1], argv[2], "")



