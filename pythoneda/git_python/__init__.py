"""
pythoneda/git_python/__init__.py

This file ensures pythoneda.git_python is a namespace.

Copyright (C) 2023-today rydnr's pythoneda-git-python/application

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
__path__ = __import__('pkgutil').extend_path(__path__, __name__)

# Ugly hack to avoid sorting PYTHONPATH
from pythoneda.git_python.python_git_repo import PythonGitRepo
from pythoneda.git_python.python_git_repo_repo import PythonGitRepoRepo
from pythoneda.git_python.python_git_repo_resolver import PythonGitRepoResolver
