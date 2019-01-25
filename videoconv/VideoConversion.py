import ffmpy

from random import randint
import logging


class VideoConversion(object):

    def __init__(self, _config_):

        self.configuration = _config_

    def convertvideo(self):
        logging.info("convertVideo")
        #self.s3.Bucket(self.configuration.get_bucket_name()).download_file(key, 'local_temp_' + n + '.' + extension)
        ff = ffmpy.FFmpeg(
            inputs={self.configuration.get_file_path(): None},
            outputs={'file_converted.avi': '-y -vcodec mpeg4 -b 4000k -acodec mp2 -ab 320k'}
        )
        ff.run()
            #self.client.upload_file('output_temp_' + n + '.avi', self.configuration.get_bucket_name(),key.replace(extension, 'avi'))
        #except ClientError as e:
            #if e.response['Error']['Code'] == "404":
                #logging.error('The object does not exist.')
            #else:
                #raise

    @staticmethod
    def get_last_split(_string_, _delimiter_):
        split = _string_.split(_delimiter_)
        return split[len(split) - 1]
