#!/usr/bin/env python3
import argparse
import configparser

import os
import sys

import yaml
import subprocess

# verified and get services from args command line
def get_args_services(shell_services, compose_services):
    docker_services = set()
    if shell_services is not None:
        for service in shell_services:
            if not service in compose_services:
                print('Some of the specified service does not exist' + 
                        '\nServices: ' + str(list(compose_services)))
                sys.exit(1)
            else:
                docker_services.add(service)
    return docker_services

# get services from docker-compose.yml file
def get_compose_services():
    with open("docker-compose.yml", 'r') as stream:
        try:
            compose_services = set()
            for service in yaml.safe_load(stream)['services'].keys():
                compose_services.add(service)
            return compose_services
        except yaml.YAMLError as exc:
            print(exc)

def start(environment, shell_services, compose_services):
    env = read_env('.env', environment)
    services = get_args_services(shell_services, compose_services)

    if not services:
        services = compose_services
    pre_up_do(services, env, environment)
            
    command = ("docker-compose up --build -d {}".
               format(str(services).replace('{', '').replace(',', '').replace('}', '')))
    subprocess.call(command, shell=True)

# own project and services logic!
def pre_up_do(services, env, section):
    if 'registry' in services:
        if env.get(section, 'REGISTRY_FLOW_PROVIDER') == 'git':
            #do
            action_code = os.system("rm -rf volumes/nifi-registry/git && "
                        "mkdir volumes/nifi-registry/git && "
                        "cd volumes/nifi-registry/git && "
                        "git clone https://github.com/{0}/{1}.git".
                        format(env.get(section, 'REGISTRY_GIT_USER'), env.get(section, 'REGISTRY_FLOW_STORAGE')))
            if action_code != 0:
                print("Stoping deployment...")
                sys.exit(1)

        if 'postgresql' in env.get(section, 'REGISTRY_DB_URL'):
            services.add('postgresql')
        else:
            services.remove('postgresql')
            services.remove('pgadmin')
            
def read_env(file, section):
    settings = configparser.ConfigParser()
    settings.read(file)
    print('Using {0} properties...'.format(section))
    return settings    

def parseArgs(services):
    # Create the parser
    parser = argparse.ArgumentParser(description='Services: ' + str(list(services)))

    # Add the arguments
    parser.add_argument('env', metavar='environment', type=str,
                    help='section environment to use')
    parser.add_argument('-s', metavar='services', type=str, nargs='+',
                    help='services (i.e. service1 service2 ...)')

    # return the parse_args() method
    return parser.parse_args()

def main():
    services = get_compose_services()
    args = parseArgs(services)
    start(args.env, args.s, services)

if __name__ == "__main__":
    main()