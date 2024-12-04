from src.domain import FileSystem

class DBUtilsFileSystem(FileSystem):
    """
    DBUtils-based implementation of the FileSystem class.
    Uses dbutils.fs to create folders and files.
    """

    def create_folder(self, path):
        """
        Creates a folder at the specified path using dbutils.fs.mkdirs().
        
        Parameters:
        path (str): The path where the folder will be created.
        """
        if not dbutils.fs.mkdirs(path):
            raise Exception(f"Failed to create folder: {path}")

    def create_file(self, path, content=""):
        """
        Creates a file at the specified path with the given content using dbutils.fs.put().
        
        Parameters:
        path (str): The path where the file will be created.
        content (str): The content to be written to the file.
        """
        dbutils.fs.put(path, content, overwrite=True)

    def file_exists(self, path):
        """
        Checks if a file or directory exists at the specified path using dbutils.fs.exists().
        
        Parameters:
        path (str): The path to check.
        
        Returns:
        bool: True if the file or directory exists, False otherwise.
        """
        return dbutils.fs.exists(path)
