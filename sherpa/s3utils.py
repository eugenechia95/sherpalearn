# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:02:42 2018

@author: Eugene
"""

# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from storages.backends.s3boto import S3BotoStorage

class StaticS3BotoStorage(S3BotoStorage):
    """
    Storage for static files.
    """

    def __init__(self, *args, **kwargs):
        kwargs['location'] = 'static'
        super(StaticS3BotoStorage, self).__init__(*args, **kwargs)


class MediaS3BotoStorage(S3BotoStorage):
    """
    Storage for uploaded media files.
    """

    def __init__(self, *args, **kwargs):
        kwargs['location'] = 'media'
        super(MediaS3BotoStorage, self).__init__(*args, **kwargs)