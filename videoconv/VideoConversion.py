import ffmpy
from ffmpy import FFmpeg
import logging
from random import randint
from google.cloud import bigquery, storage
import time
import math

class VideoConversion(object):

    def __init__(self, _config_):

        self.configuration = _config_

    def convertvideo(self):
        n = str(randint(0, 1000))
        logging.info("convertVideo")
        ff = ffmpy.FFmpeg(executable='C:\\ffmpeg\\bin\\ffmpeg.exe',
            inputs={self.configuration.get_file_path() +'.mkv': None},
            outputs={self.configuration.get_file_path()+'-converted.avi': '-y -vcodec mpeg4 -b 4000k -acodec mp2 -ab 320k'}
        )
        ff.run()

    def uploadCloudStorage(self):
        before = time.time()
        client = storage.Client(self.configuration.get_cloud_project())
        bucket = client.get_bucket(self.configuration.get_cloud_bucket())
        blob = bucket.blob(self.configuration.get_file_path() + '-converted.avi')
        blob.upload_from_filename(self.configuration.get_file_path() + '-converted.avi')
        after = time.time()

        secondUpload = after - before
        bigQueryClient = bigquery.Client(self.configuration.get_cloud_project())
        datasetRef = bigQueryClient.dataset(self.configuration.get_cloud_dataset())
        tableRef = datasetRef.table(self.configuration.get_cloud_table())
        table = bigQueryClient.get_table(tableRef)

        rows_to_insert = [
            (2, math.floor(secondUpload), self.configuration.get_file_path() + '-converted.avi')
        ]
        errors = bigQueryClient.insert_rows(table, rows_to_insert)

    @staticmethod
    def get_last_split(_string_, _delimiter_):
        split = _string_.split(_delimiter_)
        return split[len(split) - 1]
