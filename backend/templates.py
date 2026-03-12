from jinja2 import Environment, FileSystemLoader
import os

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "..", "templates")
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

def render_template(template_name: str, **kwargs) -> str:
    template = env.get_template(template_name)
    return template.render(**kwargs)

def save_artifact(content: str, relative_path: str):
    workspace_root = os.path.join(os.path.dirname(__file__), "..", "workspace")
    full_path = os.path.join(workspace_root, relative_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)
    return full_path