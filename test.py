from src import GenerateTemplate
from src import OSFileSystem
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <config.json> <template.yml> <base_folder>")
        sys.exit(1)

    config_file = sys.argv[1]
    template_file = sys.argv[2]
    base_folder = sys.argv[3]
    file_system = OSFileSystem()

    project_generator = GenerateTemplate(config_file=config_file, template_file=template_file, base_folder=base_folder, fs_adapter=file_system)
    project_generator.generate_project_structure()