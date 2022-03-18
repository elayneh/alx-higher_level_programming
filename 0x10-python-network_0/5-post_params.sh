#!/bin/bash
# this script is to post request and display the response
curl -sd email="test@gmail.com&subject=I will always be here for PLD" "$1"
