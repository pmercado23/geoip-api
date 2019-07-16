# geoip-api

Simple web API that echoes out latitude and longitude information for a given IP

# Setting/Install

Install git. `brew install git` definitely installs git.

### lat-long-api


```
git clone git@github.com:pmercado23/geoip-api.git
cd geoip-api

```


Use `Makefile` to install

run `make devinstall`

This will create the required env and install required dependency's.


## Running

### Local non-Docker

To run use `make local_run` to run dev server on local machine.

This then should be accessible at http://localhost:8000


### Local Docker

Install Docker for desktop:

Currently developed on Mac: https://docs.docker.com/docker-for-mac/

run `make docker_run`

This will build and create a docker Image then deploy
and run it in a local docker container.

This then should be accessible at http://localhost:8000 or another defined in DockerFile


### Google Cloud Platform Deploy

Follow the steps to create a GCP account and create a cluster.

https://cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster

Once cluster is created, you can access the cluster via the console and download git.

```
git clone git@github.com:pmercado23/geoip-api.git
cd geoip-api

```

for running on GCP:

run `make delpoy_gcp`

This will do the following steps:

1. Create Docker Image at `gcr.io/test-project-245416/geoip-app`
2. Push docker image up
3. using `.yaml` files located in `deploy/`
    1. Create Deployment
    2. Create Service
    3. Create CronJob

Verify Deployment by running:

1. `kubectl get deployments`
2. `kubectl get services`
3. `kubectl get cronjobs`


# Usage

Live example url:   http://35.238.204.176/status

`http://35.238.204.176/where_am_i/<IPv4>/`

Given an IPv4, the api returns information about the given IP via MaxMind GeoLite2 database as a json blob.

downloadable here: https://dev.maxmind.com/geoip/geoip2/geolite2/

Example:

```
└─[0] <> curl -v "http://35.238.204.176/where_am_i/65.49.253.128/"
*   Trying 35.238.204.176...
* Connected to 35.238.204.176 (35.238.204.176) port 80 (#0)
> GET /where_am_i/65.49.253.128/ HTTP/1.1
> Host: 35.238.204.176
> User-Agent: curl/7.43.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Date: Tue, 16 Jul 2019 19:09:53 GMT
< Server: WSGIServer/0.2 CPython/3.6.9
< Content-Type: application/json
< X-Frame-Options: SAMEORIGIN
< Content-Length: 187
<
* Connection #0 to host 35.238.204.176 left intact
{"ip": "65.49.253.128", "country": "United States", "city": "Kalamazoo", "subdivisions_most_specific_name": "Michigan", "postal_code": "49009", "latitude": 42.2789, "longitude": -85.6904}%

```

# Development

Using:
- Language: Python3.6 https://docs.python.org/3.6/
- Framework: Django 2.2.3 https://docs.djangoproject.com/en/2.2/
- Packages: geoip2 2.9.0 https://www.maxmind.com/en/geoip-demo, requests 2.22.0 https://2.python-requests.org/en/master/
- Deployment:
   - Docker: https://docs.docker.com/
   - Kubernetes: https://kubernetes.io/docs/home/
   - Google Cloud Platform: https://cloud.google.com/

# Testing

In when in local dev, run tests by `make test`

These tests are ran from `geoip-api/locateme/quickstart/tests.py`

See Django Tests Docs for more information: https://docs.djangoproject.com/en/2.2/intro/tutorial05/
