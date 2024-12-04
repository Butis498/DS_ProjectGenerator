import yaml
import json
import os

class GenerateTemplate:
    """
    A class that generates project structure based on a provided YAML template, configuration file,
    and file system adapter.
    """

    def __init__(self, config_file=None, template_file=None, base_folder=None, fs_adapter=None):
        """
        Initializes the GenerateTemplate class with provided parameters.
        
        Parameters:
        config_file (str): Path to the configuration JSON file. Default is None.
        template_file (str): Path to the template YAML file. Default is None.
        base_folder (str): Base folder where the project structure will be created. Default is None.
        fs_adapter (FileSystem): The file system adapter to use (e.g., OSFileSystem or DBUtilsFileSystem).
        """
        self.config_file = config_file
        self.template_file = template_file
        self.base_folder = base_folder
        self.fs_adapter = fs_adapter

    def create_folder_structure(self, base_path, structure):
        """
        Creates folders inside the base path according to the provided structure using the chosen file system adapter.
        
        Parameters:
        base_path (str): The path where the folder structure will be created.
        structure (list): List of folders to create inside the base path.
        
        Returns:
        None
        """
        for folder in structure:
            path = os.path.join(base_path, folder)
            if not self.fs_adapter.file_exists(path):
                self.fs_adapter.create_folder(path)
                self.create_gitkeep(path)  # Ensure .gitkeep is created in non-empty folders

    def create_gitkeep(self, path):
        """
        Creates a .gitkeep file in an empty folder to ensure Git tracks the folder.
        
        Parameters:
        path (str): The path where the .gitkeep file will be created.
        
        Returns:
        None
        """
        gitkeep_path = os.path.join(path, ".gitkeep")
        if not self.fs_adapter.file_exists(gitkeep_path):
            self.fs_adapter.create_file(gitkeep_path)

    def create_config_file(self, base_path, config_data):
        """
        Creates the configuration JSON file in the base path using the file system adapter.
        
        Parameters:
        base_path (str): The path where the config file will be created.
        config_data (dict): The data to be written to the config file.
        
        Returns:
        None
        """
        config_file_path = os.path.join(base_path, "config.json")
        if not self.fs_adapter.file_exists(config_file_path):
            self.fs_adapter.create_file(config_file_path, json.dumps(config_data, indent=4))

    def check_and_create_gitkeep(self, folder_path):
        """
        Checks if a folder is empty and creates a .gitkeep file if it's empty.
        
        Parameters:
        folder_path (str): The path of the folder to check.
        
        Returns:
        None
        """
        if not any(os.scandir(folder_path)):  # Check if the folder is empty
            self.create_gitkeep(folder_path)

    def generate_project_structure(self):
        """
        Generates the project structure and configuration file for the specified project.
        
        This function generates the folder structure based on the provided YAML template and the config 
        JSON file, then creates the necessary directories and configuration files.
        
        Returns:
        None
        """
        try:
            with open(self.template_file, 'r') as file:
                template = yaml.safe_load(file)

            if self.config_file:
                with open(self.config_file, 'r') as file:
                    config = json.load(file)
            else:
                config = {}

            project_name = config.get('project_name', 'default_project')

            project_structure = template

            project_path = os.path.join(self.base_folder, project_name)
            if not self.fs_adapter.file_exists(project_path):
                self.fs_adapter.create_folder(project_path)

            for category, folders in project_structure.items():
                if category != 'config':  # Skip 'config' folder
                    category_path = os.path.join(project_path, category)
                    if not self.fs_adapter.file_exists(category_path):
                        self.fs_adapter.create_folder(category_path)
                    if isinstance(folders, list) and not folders:  # If it's an empty list
                        self.create_gitkeep(category_path)  # Ensure .gitkeep in the empty folder
                    else:
                        self.create_folder_structure(category_path, folders)
                        for subfolder in folders:
                            subfolder_path = os.path.join(category_path, subfolder)
                            self.check_and_create_gitkeep(subfolder_path)  # Ensure empty subfolders get .gitkeep

            if 'config' in project_structure:
                self.create_config_file(project_path, project_structure['config'])

        except Exception as e:
            print(f"Error: {e}")
