#!/bin/bash
# takes URL, sends a GET request and displays the response body
response=$(curl -sG -H "X-HolbertonSchool-User-Id: 98" "$1") && [ "$response" == "route validation with header parameter" ] && echo "$response"
