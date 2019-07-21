import csv
from datetime import datetime
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # disable security warning for SSL certificate

def post_request(ipaddr, api_token, uri):
    base_url = f'https://{ipaddr}/api/v2/'
    headers = {'Authorization': f'Bearer {api_token}'}
    params = {'access_token': api_token}
    data = {
            "name": "string",
            "intrazone": "allow"
           }
    rep = requests.put(base_url + uri, json=data, params=params, verify=False) # Data MUST be passed as json=data and NOT data=data or will return 424
    # print(rep.url)                                                           # json= ensures that the Content-Type header is application/json, which is not default

    if rep.status_code != 200:
        print(f'Something went wrong when posting. status_code: {rep.status_code}')
        # print(rep.text) # uncomment to see full response
        return False

    return True

def get_request(ipaddr, api_token, uri):
    base_url = f'https://{ipaddr}/api/v2/'
    headers = {'Authorization': f'Bearer {api_token}'}
    params = {'access_token': api_token}
    data = {}
    rep = requests.put(base_url + uri, json=data, params=params, verify=False) # Data MUST be passed as json=data and NOT data=data or will return 424
    # print(rep.url)                                                           # json= ensures that the Content-Type header is application/json, which is not default

    if rep.status_code != 200:
        print(f'Something went wrong when posting. status_code: {rep.status_code}')
        # print(rep.text) # uncomment to see full response
        return False

    return True

def main():
    #ip_addr = '192.168.1.99'
    #api_token = '7by99mdbx1w6xxpdk4QN09stph1H3G'
    with open('api.csv') as firewall_list: #take initial backup
        firewall_reader = csv.reader(firewall_list, dialect='excel', lineterminator = '\r')
        for row in firewall_reader:
            if(get_request(row[1], row[2],'cmdb/system/zone')):
                print(f'did stuff.')
            else:
                print(f'FAIL.')



if __name__ == "__main__":
    main()
