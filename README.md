### Setting up

1. Copy `docker-compose.override.yml.dist` to `docker-compose.override.yml` then adjust content appropriately. 

2. Build image then install python packages.

```bash
$ docker-compose build
$ docker-compose run --rm lambda pipenv install
```

### Running

#### Flask development server

```bash
$ docker-compose up
```

#### Shell access

```bash
$ docker-compose run --rm lambda pipenv shell
```

### Deployment

```bash
$ docker-compose run --rm lambda pipenv shell
$ # First time
$ zappa deploy dev
$ # From second time
$ zappa update dev
```