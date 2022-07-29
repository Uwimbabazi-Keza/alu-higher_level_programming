#!/bin/bash
# Returns the body if status code is 200, after a GET request
curl -sLX GET "$1"
