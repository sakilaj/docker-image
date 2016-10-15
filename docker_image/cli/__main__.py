import argparse

from docker_image import reader


def main():
    description="""
Simple utility for building-pulling-pushing docker images with multiple tags.
"""
    p = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        prog='docker-image',
    )
    p.add_argument('-f', '--file', default='docker-compose.yml', help='docker-compose file')
    p.add_argument('-t', '--tags', action='append', default=['latest'])
    p.add_argument('-L', '--dont-tag-latest', action='store_true')
    p.add_argument('command', choices=['build', 'push', 'pull'])
    p.add_argument('services', nargs='*', default=[])

    args = p.parse_args()

    if args.dont_tag_latest:
        args.tags = [
            t for t in args.tags
            if t !='latest'
        ]

    service_func = {
        'build': lambda s: s.build(args.tags),
        'push': lambda s: s.push(args.tags),
        'pull': lambda s: s.pull(args.tags),
    }[args.command]

    services = {
        s.name: s
        for s in reader.read_services(args.file)
        }

    if not args.services:
        args.services = services.keys()

    for service_name in sorted(args.services):
        if service_name not in services:
            print("Service {} not found".format(service_name))
        service = services[service_name]
        service_func(service)
        print("")


if __name__ == '__main__':
    main()