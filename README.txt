== backend ==

docker build -t app_items.backend backend/

docker run -p 80:8080 --volume=$PWD/backend/:/app/:ro app_items.backend

== frontend ==

docker build -t app_items.frontend frontend/

docker run -p 80:80 --volume=$PWD:/usr/share/nginx/html/app/:ro app_items.frontend
