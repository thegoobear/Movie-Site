#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 17:16:44 2017

Makes a list of Movie objects and passes fresh_tomatoes to create a page

@author: Tripp
"""

import media
import fresh_tomatoes

#create Movie objects

the_matrix = media.Movie("The Matrix", "http://www.youtube.com/watch?v=m8e-FF8MsqU", "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg")

superbad = media.Movie("Superbad", "http://www.youtube.com/watch?v=4qnGIr3dvHk", "https://upload.wikimedia.org/wikipedia/en/8/8b/Superbad_Poster.png")

pineapple_express = media.Movie("Pineapple Express", "http://www.youtube.com/watch?v=wwhyPZGOU48", "https://upload.wikimedia.org/wikipedia/en/c/ca/Pineapple_Express_Poster.jpg")

the_other_guys = media.Movie("The Other Guys", "http://www.youtube.com/watch?v=r9I5c7r6nIU", "https://upload.wikimedia.org/wikipedia/en/6/6b/Other_guys_poster.jpg")

hot_fuzz = media.Movie("Hot Fuzz", "http://www.youtube.com/watch?v=ayTnvVpj9t4", "https://s-media-cache-ak0.pinimg.com/736x/35/02/0d/35020d0470940f57ea7eb2699c129cd8--movie-collection-film-posters.jpg")

nightcrawler = media.Movie("Nightcrawler", "https://www.youtube.com/watch?v=X8kYDQan8bw", "https://upload.wikimedia.org/wikipedia/en/d/d4/Nightcrawlerfilm.jpg")

#populate a list of movie objects

movies = [the_matrix, superbad, pineapple_express, the_other_guys, hot_fuzz, nightcrawler]

#Use fresh_tomatoes module to create page using movies list

fresh_tomatoes.open_movies_page(movies)