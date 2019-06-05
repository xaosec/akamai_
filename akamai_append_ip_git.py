#!/usr/bin/python

import sys
import requests
import json

from akamai.edgegrid import EdgeGridAuth
from urllib.parse import urlparse
from urllib.parse import urljoin

baseurl = 'https://akab-pgnevzzhaulr2ttb-4pnwdsnkjywvozpc.luna.akamaiapis.net'
s = requests.Session()

s.auth = EdgeGridAuth(
 client_token = '$client_token',
 client_secret = '$client_secret',
 access_token = '$access_token'
)


def main():
    # append IP addresses to the network list.
     f = open("guru99.txt","a+")
     for arg in sys.argv[1:]:
          result = s.put(urljoin(baseurl, '/network-list/v2/network-lists/43633_IPBLACKLISTTOP/elements?element=%s' % (arg)))
          f.write('%s\r\n' % (arg))
          f.close()
          print(result.json())
          print(result.status_code)

     print(' ')

     resultz = s.get(urljoin(baseurl, '/network-list/v2/network-lists/43633_IPBLACKLISTTOP/environments/STAGING/status'))
     print(resultz.json())

     print(' ')
     # resultx = s.post(urljoin(baseurl, '/network-list/v2/network-lists/43633_IPBLACKLISTTOP/environments/STAGING/activate'), data=json.dumps(reqdata))
     # print(resultx.json())


     # reqdata = {"comments":"Blacklist IPs of Bruteforce Attempts", "NotificationRecipients":["advanced.security@xyz.com"]}
     # headers = {'content-type': 'application/json'}

     # endpoint_result = s.post(urljoin(baseurl, '/network-list/v2/network-lists/43633_IPBLACKLISTTOP/environments/STAGING/activate'), data=json.dumps(reqdata), headers=headers)
     # print(json.dumps(endpoint_result.json()))



if __name__ == "__main__":
    main()
