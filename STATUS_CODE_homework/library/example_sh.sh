#!/bin/bash
# WANT_JSON

link=$(cat $1 | grep -Po '(?<="link": ")(.*?)(?=")')

result_string=$(curl -LI $link -o /dev/null -w '%{http_code}\n' -s)

# sleep 300

if (($result_string==000))
then
 echo "{ \"msg\": \"Oops.. Can't reach the site.\"}"
else
 echo "{\"state\": \"$result_string\", \"msg\": \"successeded\"}"
fi
