"""Top-level package for basic_template_repo."""

__package_name__ = "{{cookiecutter.project_name}}"
__version__ = "{{cookiecutter.project_version}}"

__author__ = """{{cookiecutter.author}}"""
__email__ = "{{cookiecutter.email}}"
__repo_owner_github_user_name__ = "{{cookiecutter.repo_owner_github_user_name}}"
__repo_url__ = f"https://github.com/{__repo_owner_github_user_name__})/{__package_name__}/"
__repo_issues_url__ = f"{__repo_url__}issues"

import sys
from pathlib import Path

print(f"Thank you for using {__package_name__}!")
print(f"This is printing from: {__file__}")
print(f"Source code for this package is available at: {__repo_url__}")

base_package_path = Path(__file__).parent
print(f"adding base_package_path: {base_package_path} : to sys.path")
sys.path.insert(0, str(base_package_path))  # add parent directory to sys.path

from {{cookiecutter.project_name}}.system.default_paths import get_log_file_path
from {{cookiecutter.project_name}}.system.logging_configuration import configure_logging


configure_logging(log_file_path=get_log_file_path())