# Installation

You can use your favourite virtual environment for managing python modules. I recommend to use [conda](https://docs.conda.io/en/latest/).

## Setup

Create a virtual environment using python3.9.

```
conda create -n event_platform python=3.9
```

Install required modules

```
conda install django redis-py mysqlclient
```

# Local Development

## DB and cache setup

Please install [docker](https://www.docker.com/) first, then, run the following in this repository's root directory to host redis-cache service and mysql-database service in docker container.

```
docker-compose up -d
```

## Running Django Server

Go into `myproject` directory. Then, run the following to host the local django server.

```
cd myproject

python manage.py run server
```

# Live Hosting
