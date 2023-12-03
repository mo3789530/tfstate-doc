class State:

    version = "format_version"
    terraform_version = "terraform_version"
    value = "values"
    root = "root_module"
    resources = "resources"

    def __init__(self) -> None:
        pass

    def parse(self, json) -> dict:
        version = json.get(self.version)
        terraform_version = json.get(self.terraform_version)
        resources = json.get(self.resources, [])

        return {
            "version": version,
            "terraform_version": terraform_version,
            "resources": resources
        }