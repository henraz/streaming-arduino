#!/bin/bash

echo "---------- CREATE TOPIC ----------"

gcloud pubsub topics create $1 --project=$2