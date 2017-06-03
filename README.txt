docker build -t my-angular-app .

docker run -p 80:80 --volume=$PWD:/usr/share/nginx/html/app/:ro my-angular-app
