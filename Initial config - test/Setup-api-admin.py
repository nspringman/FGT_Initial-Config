from netmiko import Netmiko
from getpass import getpass
import random
import string
import csv
import sys



#Netmiko will not accept a variable. This needs to be resolved. 
net_connect = Netmiko(
    "192.168.1.99",
    username="admin",
    password="",
    device_type="fortinet",
)



print(net_connect.find_prompt())

output = net_connect.send_command('config system accprofile')
output = net_connect.send_command('edit "readWrite"')
output = net_connect.send_command('set mntgrp read-write')
output = net_connect.send_command('set admingrp read-write')
output = net_connect.send_command('set updategrp read-write')
output = net_connect.send_command('set authgrp read-write')
output = net_connect.send_command('set sysgrp read-write')
output = net_connect.send_command('set netgrp read-write')
output = net_connect.send_command('set loggrp read-write')
output = net_connect.send_command('set routegrp read-write')
output = net_connect.send_command('set fwgrp read-write')
output = net_connect.send_command('set vpngrp read-write')
output = net_connect.send_command('set utmgrp read-write')
output = net_connect.send_command('set endpoint-control-grp read-write')
output = net_connect.send_command('set wifi read-write')
output = net_connect.send_command('end')

output = net_connect.send_command('config system api-user')
output = net_connect.send_command('edit api-admin')
output = net_connect.send_command('set accprofile "readWrite"')
output = net_connect.send_command('set api-key RaSzoz68vMGesyaIYTtJrhbpbvf4da')
output = net_connect.send_command('api-key')
output = net_connect.send_command('config trusthost')
output = net_connect.send_command('edit 1')
output = net_connect.send_command('set ipv4-trusthost 192.168.0.0 255.255.0.0')
output = net_connect.send_command('next')
output = net_connect.send_command('config trusthost')
output = net_connect.send_command('edit 2')
output = net_connect.send_command('set ipv4-trusthost 10.0.0.0 255.00.0.0')
output = net_connect.send_command('next')
output = net_connect.send_command('edit 3')
output = net_connect.send_command('set ipv4-trusthost 66.0.0.2 255.255.255.255')
output = net_connect.send_command('next')
output = net_connect.send_command('end')
output = net_connect.send_command('end')
output = net_connect.send_command('end')


output = net_connect.send_command('execute api-user generate-key api-admin')

print(output)

net_connect.disconnect()
