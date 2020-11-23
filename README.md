<div align="center">
  <a>
    <img width="230" src="./images/tablet.png">
  </a>
</div>
<div align="center">
  <h1>Screenbit</h1>
  <p>Server side implementation for screens content(ad's, media, etc.) managing</p>
  <!--
  optional images (remove <-- arrows and use this layout if you need)

  <p align="middle">
    <img height="160" src="./images/cbm.jpg">
    <img height="160" src="./images/earth.png">
    <img height="160" src="./images/nature.png">
  </p>
  -->
</div>

## ✨ Features / Tech stack
-   Dev / Production environments
- 🌍 PostgreSQL
- 🌍 redis
- 🌍 RabbitMQ
- 📦 Docker-compose

## 📦 Install / Usage

0. clone the project
1. enter project directory
    ```
    cd project directory
    ```
3. Clone [brainhublab/screenbit-api](https://github.com/brainhublab/screenbit-api)
4. Create .env file and fill in (use env-distrib for template)
5. Build images in docker compose:
    ```
    docker-compose build
    ```
6. Run images:
    ```
    docker-compose up
    ```
7. Migrate DB tables:
      - Enter api container:
        ```
        docker exec -it screenbit_api /bin/ash
        ```
      - Migrarate DB tables:
          ```
          python manage.py migrate
          ```
      - Create a super user:
          ```
          python manage.py createsuperuser
          ```
8. Configurate app:
      - Log in to django `api_uri/admin` (admin panel) and add a new Application for authentication:
      - client_id and client_secret shouldn't be changed
      - user should be your superuser
      - redirect_uris should be left blank
      - client_type should be set to 'confidential'
      - authorization_grant_type should be set to 'Resource owner password-based'
      - name can be set to whatever you want (i.e. 'password-based-auth')

      Change client id's and secrets for `web-client` and your `app`
      The rest of work is made by docker.


## 🤝 Contact

Email us at [brainhublab@gmail.com](mailto:brainhublab@gmail.com)
