#!/usr/bin/python3.5

import logging

from configuration.configuration import Configuration
from messaging.videoconversionmessaging import videoconversionmessaging
from videoconv.VideoConversion import VideoConversion
from database.conversion_database import ConversionDatabase


if __name__ == '__main__':

    config = Configuration()

    database = ConversionDatabase(config)
    conversion = VideoConversion(config)
    video_messaging = videoconversionmessaging(config, database, conversion)
