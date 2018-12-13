import yaml
import logging
import os

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG)


class Configuration(object):

    def __init__(self):
        self.configuration_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'application.yml')
        self.configuration_data = None

        f = open(self.configuration_file, 'r')
        self.configuration_data = yaml.load(f.read())
        f.close()

    def get_cloud_project(self):
        return self.configuration_data['cloud']['project']

    def get_cloud_topic(self):
        return self.configuration_data['cloud']['topic']

    def get_database_name(self):
        return self.configuration_data['aws']['name']

    def get_database_table(self):
        return self.configuration_data['aws']['table']

    def get_database_region(self):
        return self.configuration_data['aws']['region']

    def get_bucket_name(self):
        return self.configuration_data['aws']['s3']['name']

    def get_bucket_region(self):
        return self.configuration_data['aws']['s3']['region']
