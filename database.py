import base64
import datetime
import sqlite3

import sys
import os
import uuid
import random

import threading
import os


class Database:

    def __init__(self):
        self.database_file = './resume.db'
        self.con = sqlite3.connect(self.database_file)
        self.cur = self.con.cursor()

    def close_connection(self):
        self.con.close()