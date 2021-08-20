import subprocess
import urllib3
import requests
import socket

hostname = socket.gethostname() #get your system hostname

proxies = {
        'http': 'socks5h://<your-socks5-proxy>',
        'https': 'socks5h://<your-socks5-proxy>'
        } #if you need proxy enter proxy details here
service = "<your service name>"

stat = subprocess.call(["systemctl", "is-active", "--quiet", service]) # service you want to check
if(stat != 0):  # if 0 (active), print "Active"
    message = socket.gethostname() + " " + service + " is down"
    print(message)
    data = {'text':message}
    bot_token = '<telegram bot token>'
    bot_chatID = '<telegram channel id>'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + message
    requests.get(send_text, proxies=proxies)
