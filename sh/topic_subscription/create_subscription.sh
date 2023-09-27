#!/bin/bash

echo "---------- CREATE SUBSCRIPTION ----------"

RETENTION="600"
EXPIRATION="86400"
ACKDEADLINE="10"

gcloud pubsub subscriptions create $1 \
  --topic=$2 \
  --project=$PROJECT_ID \
  --message-retention-duration=$RETENTION \
  --expiration-period=$EXPIRATION \
  --ack-deadline=$ACKDEADLINE