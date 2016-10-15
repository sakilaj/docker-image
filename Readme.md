# Requirements
* python >= 3.4

# Installation
```bash
python3 setup.py install
```

# Command line options
```bash
docker-image -h
usage: __main__.py [-h] [-f FILE] [-t TAGS] [-L]
                   {build,push,pull} [services [services ...]]

positional arguments:
  {build,push,pull}
  services

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  docker-compose file (default: docker-compose.yml)
  -t TAGS, --tags TAGS
  -L, --dont-tag-latest
```

# Image build example
```bash
# Build service1 described in docker-compose.service1.yml
# Add tags `0.0.1`, `testing`, `latest`
# Use `-L` options to remove `latest` tag
docker-image -f docker-compose.service1.yml  -t 0.0.1 -t testing build service1
```