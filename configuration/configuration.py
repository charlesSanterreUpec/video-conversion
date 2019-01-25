import yaml
import logging
import os

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG)


class Configuration(object):

    def __init__(self):
        self.configuration_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../application.yml')
        self.configuration_data = None

        f = open(self.configuration_file, 'r')
        self.configuration_data = yaml.load(f.read())
        f.close()

    def get_cloud_project(self):
        return self.configuration_data['cloud']['project']

    def get_cloud_bucket(self):
        return self.configuration_data['cloud']['bucket']

    def get_file_path(self):
        return self.configuration_data['file']['path']
