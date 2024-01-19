import os

def create_folder_structure(project_name):
    # Define the folder structure
    folders = [
        'data/raw/dataset_name',
        'data/processed/dataset_name',
        'notebooks',
        'src/data',
        'src/features',
        'src/models',
        'src/utils',
        'config',
    ]

    # Create project directory
    os.makedirs(project_name, exist_ok=True)

    # Create folders within the project directory
    for folder in folders:
        folder_path = os.path.join(project_name, folder)
        os.makedirs(folder_path, exist_ok=True)
        # Add an __init__.py file in Python packages
        if '__init__.py' not in folder:
            init_file = os.path.join(folder_path, '__init__.py')
            with open(init_file, 'w') as f:
                pass

    # Create README.md and requirements.txt files
    with open(os.path.join(project_name, 'README.md'), 'w') as readme:
        readme.write(f'# {project_name}\n\nProject description here.')

    with open(os.path.join(project_name, 'requirements.txt'), 'w') as reqs:
        reqs.write('')

if __name__ == "__main__":
    project_name = "my_ml_project"  # Replace with your project name
    create_folder_structure(project_name)
    print(f"Folder structure for '{project_name}' created successfully.")
