import sys

import sh
from sh import docker
from typing import List


def _p(l):
    # print(l)
    sys.stdout.write(l)


def _e(l):
    sys.stderr.write(l)


class Service:
    def __init__(self, name: str, context_dir: str, docker_file: str, registry:str, image: str):
        self.name = name
        self._context_dir = context_dir
        self._docker_file = docker_file
        self._registry = registry
        self._image = image

    def build(self, tags: List[str]):
        print("Building service: {}".format(
            self.name,
        ))
        tags = tags or ['latest']

        build_tag = "{registry}/{image}:{tag}".format(
            registry=self._registry,
            image=self._image,
            tag="_build_"
        )

        try:
            docker.build(
                self._context_dir,
                file=self._docker_file,
                tag=build_tag,
                _out=_p,
                _err=_e,
                _out_bufsize=0,
            )

            for tag in tags:
                reg_tag = "{registry}/{image}:{tag}".format(
                    registry=self._registry,
                    image=self._image,
                    tag=tag
                )
                print("Tagged: {}".format(reg_tag))
                docker.tag(build_tag, reg_tag, _out=_p, _err=_e, _out_bufsize=0)
            docker.rmi(build_tag, _out=_p)
        except sh.ErrorReturnCode_1:
            pass

    def push(self, tags: List[str]):
        # try:
        for tag in tags:
            reg_tag = "{registry}/{image}:{tag}".format(
                registry=self._registry,
                image=self._image,
                tag=tag
            )
            print("Pushing: {}".format(reg_tag))
            docker.push(reg_tag, _out=_p, _err=_e, _out_bufsize=0)
        # except sh.ErrorReturnCode_1:
        #     pass

    def pull(self, tags: List[str]):
        # try:
        for tag in tags:
            reg_tag = "{registry}/{image}:{tag}".format(
                registry=self._registry,
                image=self._image,
                tag=tag
            )
            print("Pulling: {}".format(reg_tag))
            docker.pull(reg_tag, _out=_p, _err=_e,_out_bufsize=0)
        # except sh.ErrorReturnCode_1:
        #     pass
