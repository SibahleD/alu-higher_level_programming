#!/bin/bash
# sends a POST request to a passed URL and displays the response body
curl -sd "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
