import yaml
from typing import List, Dict, Any

from os.path import dirname, join

from docker_image.service import Service


def _read_service(name: str, compose_dir: str, service_desc: Dict[str, Any])->Service:
    build_desc = service_desc.get('build', {})
    image_url = service_desc['image']  # type: str

    if '/' in image_url:
        registry, name_tag = image_url.split('/')
    else:
        registry = 'docker.io'
        name_tag = image_url

    if ':' in name_tag:
        image_name, _ = name_tag.split(':')
    else:
        image_name = name_tag

    context_dir = join(compose_dir, build_desc.get('context', '.'))
    docker_file = join(compose_dir, build_desc.get('dockerfile', 'Dockerfile'))
    return Service(
        name=name,
        context_dir=context_dir,
        docker_file=docker_file,
        image=image_name,
        registry=registry,
    )


def read_services(compose_file: str)->List[Service]:
    with open(compose_file) as f:
        desc = yaml.load(f)

    compose_dir = dirname(compose_file)
    return [
        _read_service(name, compose_dir, service_desc)
        for name, service_desc in desc.get('services', {}).items()
    ]



