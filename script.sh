curl -X POST "http://localhost:8000/api/auth/register" -d '{"name": "Hon Hao Chen", "email": "honhc@garena.com", "password": "123456"}'
curl -X POST -c cookies.txt "http://localhost:8000/api/auth/login" -d '{"email": "honhc@garena.com", "password": "123456"}'
curl -X GET -b cookies.txt "http://localhost:8000/api/events/view"
curl -X POST -b cookies.txt "http://localhost:8000/api/events/comment" -d '{"id": "4197", "comment": "Hello World!"}'
curl -X POST -b cookies.txt "http://localhost:8000/api/events/participate" -d '{"id": "4197"}'
curl -X POST -b cookies.txt "http://localhost:8000/api/events/like" -d '{"id": "4197"}'