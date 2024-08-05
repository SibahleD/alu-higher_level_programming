#!/usr/bin/python3
""" Fetches a https and displays response body """
import urllib.request
url = 'https://intranet.hbtn.io/status'
if url.startswith('https://'):
    url = 'https://alu-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    body = response.read()
print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
print("\t- utf8 content: {}".format(body.decode('utf-8')))
