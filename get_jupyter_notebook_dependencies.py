import pkg_resources
import types
def get_imports():
    for name, val in globals().items():
        if isinstance(val, types.ModuleType):
            name = val.__name__.split(".")[0]

        elif isinstance(val, type):
            name = val.__module__.split(".")[0]
        poorly_named_packages = {
            "sklearn": "scikit-learn"
        }
        if name in poorly_named_packages.keys():
            name = poorly_named_packages[name]

        yield name
imports = list(set(get_imports()))
requirements = []
for j in pkg_resources.working_set:
    if j.project_name in imports and j.project_name!="pip":
        requirements.append((j.project_name, j.version))

for r in requirements:
    print("{}: {}".format(*r))
