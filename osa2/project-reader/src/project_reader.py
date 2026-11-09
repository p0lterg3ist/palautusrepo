from urllib import request

import toml
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")
        data = toml.loads(content)

        project_data = data["project"]
        dependencies = [
            dependency.split(">=")[0]
            for dependency in project_data["dependencies"]
        ]
        dependencies = [
            "Flask" if name.lower() == "flask" else name
            for name in dependencies
        ]

        dev_dependencies = [
            dependency.split(">=")[0]
            for dependency in data["dependency-groups"]["dev"]
        ]
        authors = [
            author["name"]
            for author in project_data["authors"]
        ]
        name = project_data["name"].replace("-", " ").capitalize()

        return Project(
            name,
            project_data["description"],
            dependencies,
            dev_dependencies,
            project_data["license"],
            authors,
        )
