#!/bin/bash
# takes URL, sends a GET request and displays the response body
curl -sG -H "X-HolbertonSchool-User-Id: 98" "$1"
