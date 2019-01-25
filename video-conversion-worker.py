#!/usr/bin/python3.5

from configuration.configuration import Configuration
from videoconv.VideoConversion import VideoConversion
import logging


if __name__ == '__main__':
    logging.info("main")
    config = Configuration()
    conversion = VideoConversion(config)
    conversion.convertvideo()
    conversion.uploadCloudStorage()
