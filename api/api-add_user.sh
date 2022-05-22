
sudo curl -X 'POST' \
  'http://{ip}/http/hub/api/users' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token {token}' \
  -d '{
  "usernames": [
    "username"
  ],
  "admin": true
}'

