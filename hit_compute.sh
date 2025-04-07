#!/bin/bash

LOG_FILE="/home/ubuntuuser/cron.log"
ENDPOINT="http://127.0.0.1:5000/compute"

{
    echo "[$(date)] Hitting /compute endpoint..."
    RESPONSE=$(curl -s -w "\nHTTP Status: %{http_code}\n" "$ENDPOINT")
    echo "$RESPONSE"
    echo ""
} >> "$LOG_FILE"
