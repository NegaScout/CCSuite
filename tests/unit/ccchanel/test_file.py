from tests.dropbox_login_base import WithDropboxLogin
from ccsuite.ccchanel import file


class TestFileListFiles(WithDropboxLogin):
    def test_list_files(self):
        file.list_files(self.dbx, '')
