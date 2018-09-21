#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 19:52:19 2018

@author: nsammut
"""

class Loader:
    def load(self):
        import pandas as pd
        x = pd.read_csv(self.path + self.filename)
        return(x)
        
    def __init__(self, path, filename):
        self.path = path
        self.filename = filename
    