import os
from src.domain import FileSystem
class OSFileSystem(FileSystem):
    """
    OS-based implementation of the FileSystem class.
    Uses the 'os' module to create folders and files.
    """

    def create_folder(self, path):
        """
        Creates a folder at the specified path using os.makedirs().
        
        Parameters:
        path (str): The path where the folder will be created.
        """
        if not os.path.exists(path):
            os.makedirs(path)

    def create_file(self, path, content=""):
        """
        Creates a file at the specified path with the given content using open().
        
        Parameters:
        path (str): The path where the file will be created.
        content (str): The content to be written to the file.
        """
        with open(path, 'w') as f:
            f.write(content)

    def file_exists(self, path):
        """
        Checks if a file or directory exists at the specified path using os.path.exists().
        
        Parameters:
        path (str): The path to check.
        
        Returns:
        bool: True if the file or directory exists, False otherwise.
        """
        return os.path.exists(path)
