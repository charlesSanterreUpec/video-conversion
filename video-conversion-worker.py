#!/usr/bin/python3.5

import logging

from configuration.configuration import Configuration
from messaging.videoconversionmessaging import videoconversionmessaging
from videoconvunixsocket.videoconversion import videoconversion


if __name__ == '__main__':

    logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG)
    configuration = Configuration()

    #logging.info(configuration.get_rabbitmq_host())
    #logging.info(configuration.get_rabbitmq_port())
    #logging.info(configuration.get_messaging_conversion_queue())
    #logging.info(configuration.get_database_name())
    #logging.info(configuration.get_video_conversion_collection())


    video = videoconversion()
    video.start()
    video_conversion_service = videoconversion(configuration)
    video_messaging = videoconversionmessaging(configuration, video_conversion_service)
    video.setVideoConversionMessaging(video_messaging)

