import docker
import requests
from termcolor import colored


def get_docker_client():
    return docker.from_env()


def check_docker():
    try:
        get_docker_client().info()

        return True
    except requests.exceptions.ConnectionError:
        print(colored("Docker is not running or may not be installed in your system.", 'red'))
        print(colored("To install docker visit 'http://www.docker.com'", 'red'))

        return False
    except docker.errors.APIError as ex:
        print(colored(ex.message, 'red'))

        return False
    except:
        print(colored("Something went wrong.", 'red'))

        return False


def get_docker_version():
    return str(get_docker_client().version()['Version'])


def check_image(image_name, version='latest'):
    client = get_docker_client()
    try:
        client.images.get('%s:%s' % (image_name, version))
    except docker.errors.ImageNotFound:
        print(colored("%s:%s docker image does not exists in your system" % (image_name, version), 'red'))

        return False

    return True


def pull_image(image_name, version='latest'):
    client = get_docker_client()
    try:
        print(colored("Pulling image: '%s:%s' from docker repository" % (image_name, version), 'yellow'))
        client.images.pull('%s' % image_name, tag=version)
        print(colored("Pulled image: '%s:%s' from docker repository" % (image_name, version), 'blue'))

        return True
    except docker.errors.ImageNotFound:
        print(colored("Unable to pull image: '%s:%s' from docker repository." % (image_name, version), 'red'))
        print(colored("Something went wrong.", 'red'))
        print
        print("##########################################################")
        print(colored("You can create an issue in the github repository at:", 'yellow'))
        print(colored("https://github.com/iBoneYard/phpmyadmin/issues", 'blue'))
        print
        print(colored('If you are a developer, please checkout the codebase at:', 'yellow'))
        print(colored("https://github.com/iBoneYard/phpmyadmin/", 'blue'))
        print
        print(colored("Pull requests are always welcomed :)", 'green'))
        print("##########################################################")
        print

        return False


def get_container(image_name, version='latest'):
    client = get_docker_client()
    for container in client.containers.list():
        print(container.attrs['Config']['Image'])
        print('%s:version' % [image_name, version])
        if container.attrs['Config']['Image'] == '%s:%s' % (image_name, version):
            return container
    return False


def run_container(image_name, version='latest'):
    client = get_docker_client()
    for container in client.containers.list():
        print(container.attrs['Config']['Image'])
        print('%s:version' % [image_name, version])
        if container.attrs['Config']['Image'] == '%s:%s' % (image_name, version):
            container.start()
            return True

    client.containers.run('%s:%s' % (image_name, version))


def stop_container(image_name, version='latest'):
    client = get_docker_client()
    for container in client.containers.list():
        print(container.attrs['Config']['Image'])
        print('%s:version' % [image_name, version])
        if container.attrs['Config']['Image'] == '%s:%s' % (image_name, version):
            container.stop()
            return True

    return True


def delete_container(image_name, version='latest'):
    client = get_docker_client()
    for container in client.containers.list():
        print(container.attrs['Config']['Image'])
        print('%s:version' % [image_name, version])
        if container.attrs['Config']['Image'] == '%s:%s' % (image_name, version):
            container.kill()
            return True

    return True
