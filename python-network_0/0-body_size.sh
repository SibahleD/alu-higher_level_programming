#!/bin/bash
# Sends a request to the URL and displays the size of the response body in bytes
curl -s -w '%{size_download}\n' -o /dev/null "$1"
