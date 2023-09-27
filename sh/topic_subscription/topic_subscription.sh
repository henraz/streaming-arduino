#!/bin/bash

PROJECT_ID="project-id"
TOPIC_NAME="topic-name"
SUBSCRIPTION_NAME="subscription"


# Create Topic
TOPIC="./sh/topic_subscription/create_topic.sh"
source "$TOPIC" $TOPIC_NAME $PROJECT_ID


# Create Subscription
SUBSCRIPTION="./sh/topic_subscription/create_subscription.sh"
source "$SUBSCRIPTION" $SUBSCRIPTION_NAME $TOPIC_NAME $PROJECT_ID