#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 12:55:17 2017

Class for a Movie containing
youtube url, title, poster url

@author: Tripp Green
"""


class Movie():
    """Creates a movie object.

    Args:
    title: Movie title
    trailer_youtube_url: URL to film's trailer
    poster_image_url: URL to film's poster

    Returns: Void"""

    def __init__(self, title, trailer_youtube_url, poster_image_url):

        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
