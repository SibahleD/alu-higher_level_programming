#!/bin/bash
#takes URL, sends a GET request and displays the response body
curl -sG "$1" "X-HolbertonSchool-User-Id: 98"
