#!/bin/bash
# displays only the status code response
curl -s -o /dev/null -w "%{code_here}" "$1"
