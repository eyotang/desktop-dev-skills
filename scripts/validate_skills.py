"""Validate the repository's skill packages without reading user credentials."""
from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]

def validate():
    errors = []
    seen = set()
    folders = sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())
    if not folders:
        errors.append("No skills found")
    for folder in folders:
        try:
            content = (folder / "SKILL.md").read_text(encoding="utf-8")
            match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n(.*)\Z", content, re.S)
            if not match:
                raise ValueError("Missing YAML frontmatter")
            meta = yaml.safe_load(match[1])
            if not isinstance(meta, dict):
                raise ValueError("Frontmatter must be a mapping")
            name = meta.get("name")
            if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
                raise ValueError("Invalid skill name")
            if name != folder.name or name in seen:
                raise ValueError("Name must match folder and be unique")
            seen.add(name)
            if not isinstance(meta.get("description"), str) or not meta["description"].strip():
                raise ValueError("Missing description")
            if not match[2].strip():
                raise ValueError("Missing instructions")
            ui = folder / "agents" / "openai.yaml"
            if ui.exists():
                config = yaml.safe_load(ui.read_text(encoding="utf-8"))
                interface = config.get("interface", {}) if isinstance(config, dict) else {}
                for key in ("display_name", "short_description", "default_prompt"):
                    if not isinstance(interface.get(key), str) or not interface[key].strip():
                        raise ValueError(f"Missing interface.{key}")
                if f"${name}" not in interface["default_prompt"]:
                    raise ValueError("Default prompt must invoke the skill")
        except (OSError, ValueError, yaml.YAMLError) as exc:
            errors.append(f"{folder.name}: {exc}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(folders)} skill(s).")
    return 0

if __name__ == "__main__":
    sys.exit(validate())
