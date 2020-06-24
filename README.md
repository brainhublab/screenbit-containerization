# docker integration for screenbit project

first clone `screenbitApi` from git

create env: `cp env-distrib .env`

`docker-compose up` (use `-d` to detach it)

> open container terminal
  `docker exec -it screenbit_api /bin/ash`

  > Migrarate DB tables
    `python manage.py migrate`
  > Create a super user
    `python manage.py createsuperuser`

> Go to django `api_uri/admin` (admin panel) and add a new Application for authentication:
> - client_id and client_secret shouldn't be changed
> - user should be your superuser
> - redirect_uris should be left blank
> - client_type should be set to confidential
> - authorization_grant_type should be set to 'Resource owner password-based'
> - name can be set to whatever you want (i.e. 'password-based-auth')
>
> Change client id's and secrets for `web-client` and your `app`
> The rest of work is made by docker.

P.s. it's worth reviewing `docker-compose.yml` file.

Contact: team@brainhub.co
