
---

### roles/package_maintenance/README.md

```markdown
# package_maintenance role

Handles system package updates and cleanups.

## Features

- Updates package caches
- Upgrades packages to latest versions
- Removes unused packages and cleans cache
- Supports Debian/Raspbian systems

## Usage

```yaml
- hosts: all
  roles:
    - package_maintenance
