#!/bin/bash
# bash script for posting json data files and testing server
curl -s -d "@$2" -H "Content-Type: application/json" -X POST "$1"
