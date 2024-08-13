#!/bin/bash


#set -x
HOPRD_API_URL=https://hoprd-core-rotsee-${1}.core-team.staging.hoprnet.link/api/v3

channels=$(curl -s -X 'GET' "${HOPRD_API_URL}/channels" -H 'accept: application/json' -H "X-Auth-Token: ${HOPRD_API_TOKEN}" | jq -r '.incoming[] | select(.status=="Open").id')
for channel_id in ${channels[@]}; do
  echo "Agregating tickets for channel id ${channel_id}"
  curl --max-time 300 --connect-timeout 300 -X 'POST' "${HOPRD_API_URL}/channels/${channel_id}/tickets/aggregate" -H 'accept: */*' -H "X-Auth-Token: ${HOPRD_API_TOKEN}" -d ''
  sleep 2

  #echo "Redeeming tickets for channel ${channel_id}"
  curl -X 'POST' "${HOPRD_API_URL}/channels/${channel_id}/tickets/redeem" -H 'accept: */*' -H "X-Auth-Token: ${HOPRD_API_TOKEN}" -d ''
  sleep 5

done
