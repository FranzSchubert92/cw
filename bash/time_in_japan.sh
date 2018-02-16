#!/usr/bin/env bash

# Write a one-liner that returns the current date and time in Japan.
# Date must be in ISO-8601 format, with a precision of minutes, like this:

# 2017-09-23T00:33+0900

TZ='Asia/Tokyo' date --iso-8601=minutes
