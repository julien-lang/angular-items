
== Use docker ==

__Build__
	docker build -t app_items.backend backend/
	docker build -t app_items.frontend frontend/


__Dev & debug__

 * run backend
	docker run \
		-p 8080:8080 \
		--volume=$PWD/backend/:/app/:ro \
		--name=backend \
		app_items.backend

 * run frontend
	docker run \
		-p 80:80 \
		--volume=$PWD/frontend/:/app/:ro \
		--volume=$PWD/frontend/:/etc/nginx/conf.d/:ro \
		--link backend:backend \
		app_items.frontend


__Deploy for real__

	docker-compose up

	docker-compose kill
