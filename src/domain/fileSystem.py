from abc import ABC, abstractmethod

class FileSystem(ABC):
    """
    Abstract class defining the contract for file system operations.
    This allows switching between different file systems (os, dbutils).
    """

    @abstractmethod
    def create_folder(self, path):
        """
        Creates a folder at the specified path.
        
        Parameters:
        path (str): The path where the folder will be created.
        """
        pass

    @abstractmethod
    def create_file(self, path, content=""):
        """
        Creates a file at the specified path with the given content.
        
        Parameters:
        path (str): The path where the file will be created.
        content (str): The content to be written to the file. Default is an empty string.
        """
        pass

    @abstractmethod
    def file_exists(self, path):
        """
        Checks if a file or directory exists at the specified path.
        
        Parameters:
        path (str): The path to check.
        
        Returns:
        bool: True if the file or directory exists, False otherwise.
        """
        pass
