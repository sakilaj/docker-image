from distutils.core import setup

setup(
    name='docker-image',
    version='0.0.1',
    packages=['docker_image', 'docker_image.cli'],
    url='',
    license='',
    author='nikita prianichnikov',
    author_email='lpenguin@yandex.ru',
    description='', requires=['sh', 'pyyaml', "typing"],
    scripts=['bin/docker-image']
)
