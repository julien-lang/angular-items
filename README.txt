docker build -t app_items.frontend frontend/

docker run -p 80:80 --volume=$PWD:/usr/share/nginx/html/app/:ro app_items.frontend
