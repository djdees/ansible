
---

### roles/language-python/README.md

```markdown
# language-python role

This role manages Python versions and global packages using asdf.

## Variables

- `asdf_root`: Path to asdf root (e.g. `/home/djdees/.asdf`)
- `python_versions`: List of Python versions to install
- `python_default_version`: Default Python version to set globally
- `python_packages`: List of Python packages to install globally via pip

## Requirements

Requires the `asdf` role to be run first.

## Example Playbook

```yaml
- hosts: dev_machines
  vars:
    asdf_root: "/home/djdees/.asdf"
  roles:
    - asdf
    - language-python
