#!/bin/bash
# Sends GET request with header variable X-School-User_Id=98
curl -s "$1" -X GET -H "X-School-User-Id: 98"
