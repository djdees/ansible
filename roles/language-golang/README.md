
---

### roles/language-golang/README.md

```markdown
# language-golang role

This role manages Go (Golang) versions using asdf.

## Variables

- `asdf_root`: Path to asdf root
- `golang_versions`: List of Go versions to install
- `golang_default_version`: Default Go version to set globally
- `golang_packages`: List of Go tools/packages to install globally (optional)

## Notes

- Installs Go versions via asdf.
- Supports installing global Go tools if specified.

## Example Playbook

```yaml
- hosts: dev_machines
  vars:
    asdf_root: "/home/djdees/.asdf"
  roles:
    - asdf
    - language-golang
