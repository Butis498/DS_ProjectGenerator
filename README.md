
# Project Structure Generator

## Overview  
This project automates the creation of a customizable project directory structure using YAML templates and JSON configurations. It supports multiple file system adapters (OS, DBUtils) and ensures Git tracks empty folders by creating `.gitkeep` files where needed.

## Features  
- **Dynamic Project Structure**: Uses YAML templates to define directory structures.  
- **Configurable Settings**: Reads project configuration from a JSON file.  
- **File System Abstraction**: Supports both `os` and `dbutils` adapters.  
- **Auto Git Tracking**: Adds `.gitkeep` files to empty directories.  
- **Cross-Platform Compatibility**: Works on macOS, Linux, and Windows.

## Installation  

Clone the repository:  
```bash
git clone <repository-url>
cd <repository-folder>
```

Install the required dependencies:  
```bash
pip install -r requirements.txt
```

## Usage  

Run the script using the following command:  
```bash
python script.py <config.json> <template.yml> <base_folder>
```

Example:  
```bash
python script.py config/genIA.json config/template.yml Test/
```

## Configuration  

### `config.json` (Example)  
```json
{
  "project_name": "MyProject"
}
```

### `template.yml` (Example)  
```yaml
core:
  - utils
  - data
  - models
  - logging
  - tests
ml_experiments:
  - hyperparameter_tuning
  - model_training
queries:
  - exploratory
  - production
dashboards:
  - overview
  - detailed
gold: []
silver: []
bronze: []
```

## Project Structure  

Upon execution, the tool will create a project structure similar to this:  

```
MyProject/
│
├── core/
│   ├── utils/
│   ├── data/
│   ├── models/
│   ├── logging/
│   └── tests/
│
├── ml_experiments/
│   ├── hyperparameter_tuning/
│   └── model_training/
│
├── queries/
│   ├── exploratory/
│   └── production/
│
├── dashboards/
│   ├── overview/
│   └── detailed/
│
├── gold/
│   └── .gitkeep
├── silver/
│   └── .gitkeep
└── bronze/
    └── .gitkeep
```

## File System Adapters  

### OS Adapter (Default)  
Uses Python's `os` module to manage files and directories.  

### DBUtils Adapter  
For Databricks environments using `dbutils`. 

## License  
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing  
Contributions are welcome! Please submit issues and pull requests via GitHub.

## Contact  
**Author**: Esteban Salazar  
**Email**: estebansalazar498@gmail.com
