#!/bin/sh

cat <<EOF >> .env
SECRET_KEY=$SECRET_KEY
DB_NAME=$DB_NAME
DB_USER=$PB_USER
DB_PASS=$DB_PASS
DB_HOST=$DB_HOST
DJANGO_DEBUG=True
GOOGLE_APPLICATION_CREDENTIALS=$GOOGLE_APPLICATION_CREDENTIALS
ALLOW_TRANSLATION_IMPORT=True
FRONTEND_DOMAIN=$FRONTEND_DOMAIN
TWILIO_SID=$TWILIO_SID
TWILIO_TOKEN=$TWILIO_TOKEN
TWILIO_PHONE_NUMBER=$TWILIO_PHONE_NUMBER
SENDGRID=$SENDGRID
EOF
