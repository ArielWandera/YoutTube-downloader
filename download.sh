#!/bin/bash

URL=$1
FORMAT=$2

if [ -z "$URL" ]; then
    echo "Usage: ./download.sh <youtube_url> [format_code]"
    exit 1
fi

if [ -z "$FORMAT" ]; then
    FORMAT="bestvideo+bestaudio"
fi

python yt_downloader.py "$URL" "$FORMAT"
