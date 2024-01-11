from tests.dropbox_login_base import WithDropboxLogin
from ccsuite.ccchanel import file
import os

#todo: rewrite implementation, so:
# - hidding is modular (more testable)
# - CC channel is modular (more testable)
class TestFileListFiles(WithDropboxLogin):
    def test_list_files(self, remote_path_to_list=''):
        print(os.getcwd())
        file.list_files(self.dbx, remote_path_to_list)


class TestUploadFiles(WithDropboxLogin):

    def test_upload_file_fp(self, file_pointer=None):
        # empty fp, valid fp, None
        pass

    def test_upload_file(self, path_to_list=''):
        # empty file, valid file, nonexistent filepath, None
        pass


class TestDownloadFiles(WithDropboxLogin):

    def test_download_file(self, remote_path=''):
        # empty file, valid file, nonexistent filepath, None
        pass

    def test_download_file_as(self, remote_path='', local_path=''):
        # empty file, valid file, nonexistent filepath, None
        pass


class TestEncodeBytes(WithDropboxLogin):
    def test_encode_to_bytes(self, payload: object, image_path=''):
        # empty file, valid file, nonexistent filepath, None
        pass


class TestDecodeBytes(WithDropboxLogin):
    def test_decode_from_bytes(self, bytes_to_decode=b''):
        # empty file, valid file, nonexistent filepath, None
        pass
