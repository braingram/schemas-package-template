from pathlib import Path

import importlib.resources

from asdf_standard import DirectoryResourceMapping

import {{ cookiecutter.module_name }}


def get_resource_mappings():
    resources_root = importlib.resources.files({{ cookiecutter.module_name }}) / "resources"
    if not resources_root.is_dir():
        # In an editable install, the resources directory will exist off the
        # repository root:
        resources_root = Path(__file__).parent.parent.parent / "resources"
        if not resources_root.is_dir():
            raise RuntimeError("Missing resources directory")

    return [
        DirectoryResourceMapping(
            resources_root / "{{ cookiecutter.schema_org_uri }}" / "schemas",
            "asdf://{{ cookiecutter.schema_org_uri }}/{{ cookiecutter.package_uri_stub }}/schemas",
        ),
        DirectoryResourceMapping(
            resources_root / "{{ cookiecutter.manifest_org_uri }}" / "manifests",
            "asdf://{{ cookiecutter.manifest_org_uri }}/{{ cookiecutter.package_uri_stub }}/manifests",
        ),
    ]
