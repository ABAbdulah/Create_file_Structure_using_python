import os

def create_project_structure():
    structure = {
        "project": [
            ".env",
            "requirements.txt",
            {
                "dump_restore": []
            },
            {
                "scripts": [
                    "FairSource.users.py",
                    "FairSource.products.py",
                    "FairSource.orders.py",
                    "master.py"
                ]
            },
            {
                "utils": [
                    "index_utils.py"
                ]
            }
        ]
    }

    def create_structure(base_path, items):
        for item in items:
            if isinstance(item, str):
                # Create a file
                open(os.path.join(base_path, item), 'w').close()
            elif isinstance(item, dict):
                # Create a directory and its contents
                for folder, content in item.items():
                    folder_path = os.path.join(base_path, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    create_structure(folder_path, content)

    # Create the base project folder
    base_dir = list(structure.keys())[0]
    os.makedirs(base_dir, exist_ok=True)
    create_structure(base_dir, structure[base_dir])

if __name__ == "__main__":
    create_project_structure()
    print("Project structure created successfully!")
