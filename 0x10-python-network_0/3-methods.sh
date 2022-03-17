#!/bin/bash
# display all allowed verbs here
curl -sI "$1" | grep "allow: " | sed 's/allow: //'
