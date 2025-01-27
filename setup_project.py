import os

# Define the folder structure
folders = [
    "docs",
    "src/app",
    "src/tests",
    "infra",
    "pipelines",
    "scripts",
    "config",
    ".github"
]

# Define the files to be created
files = [
    "docs/README.md",
    "docs/CONTRIBUTING.md",
    "docs/CHANGELOG.md",
    "src/app/main.py",
    "src/app/requirements.txt",
    "src/tests/test_main.py",
    "infra/main.bicep",
    "infra/variables.bicep",
    "pipelines/azure-pipelines.yml",
    "scripts/setup.sh",
    "scripts/deploy.sh",
    "config/dev.env",
    "config/prod.env",
    ".github/github-pipelines.yml"
]

# Create the folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create the files
for file in files:
    with open(file, 'w') as f:
        pass

print("Project structure created successfully!")
