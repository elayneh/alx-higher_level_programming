#!/bin/bash
# display all allowed verbs here
curl -sI "$1" | grep "Allow: " | sed 's/Allow: //'
