#!/bin/bash
# Send POST request with variables email=test@gmail.com" and subject="I will always be here for PLD"
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
