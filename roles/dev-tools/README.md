
---

### roles/dev-tools/README.md

```markdown
# dev-tools role

This role installs various development tools and utilities globally.

## Variables

- `tools_packages`: List of packages to install (e.g., git, jq, csvkit)

## Usage

Simply include this role to ensure your standard dev tools are installed.

```yaml
- hosts: dev_machines
  roles:
    - dev-tools
