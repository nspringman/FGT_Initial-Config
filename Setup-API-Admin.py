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

def fgt_command(command):
    return net_connect.send_command(command, expect_string='#')

output = fgt_command('config system accprofile')
output = fgt_command('edit "readWrite"')
output = fgt_command('set mntgrp read-write')
output = fgt_command('set admingrp read-write')
output = fgt_command('set updategrp read-write')
output = fgt_command('set authgrp read-write')
output = fgt_command('set sysgrp read-write')
output = fgt_command('set netgrp read-write')
output = fgt_command('set loggrp read-write')
output = fgt_command('set routegrp read-write')
output = fgt_command('set fwgrp read-write')
output = fgt_command('set vpngrp read-write')
output = fgt_command('set utmgrp read-write')
output = fgt_command('set endpoint-control-grp read-write')
output = fgt_command('set wifi read-write')
output = fgt_command('end')

output = fgt_command('config system api-user')
output = fgt_command('edit api-admin')
output = fgt_command('set accprofile "readWrite"')
output = fgt_command('set api-key RaSzoz68vMGesyaIYTtJrhbpbvf4da')
output = fgt_command('api-key')
output = fgt_command('config trusthost')
output = fgt_command('edit 1')
output = fgt_command('set ipv4-trusthost 192.168.0.0 255.255.0.0')
output = fgt_command('next')
output = fgt_command('config trusthost')
output = fgt_command('edit 2')
output = fgt_command('set ipv4-trusthost 10.0.0.0 255.0.0.0')
output = fgt_command('next')
output = fgt_command('edit 3')
output = fgt_command('set ipv4-trusthost 66.0.0.2 255.255.255.255')
output = fgt_command('next')
output = fgt_command('end')
output = fgt_command('end')
output = fgt_command('end')

output = fgt_command('execute api-user generate-key api-admin')

with open('API_KEY.txt', 'w+') as API_KEY:
    API_KEY.write(output)

net_connect.disconnect()
