#!/bin/bash

# test httpd service is running and throw an error if not the case
systemctl is-enabled httpd.service
if [ $? -ne 0 ]; then
  echo "httpd.service is not enabled"
  exit 1

# test httpd service is running and throw an error if not the case
systemctl is-active httpd.service
if [ $? -ne 0 ]; then
  echo "httpd.service is not running"
  exit 1
