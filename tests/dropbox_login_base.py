from unittest import TestCase
import dropbox
import os


class WithDropboxLogin(TestCase):
    def setUp(self):
        self.dbx = dropbox.Dropbox(os.environ['DROPBOX_TOKEN'])
