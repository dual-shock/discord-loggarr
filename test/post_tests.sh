#!/usr/bin/env bash

URL="http://localhost:12345/webhook"

for file in *.json; do
  echo "➡ Sending $file"
  curl -s -X POST "$URL" \
    -H "Content-Type: application/json" \
    --data @"$file"
  echo -e "\n✔ Done $file\n"
  sleep 1
done