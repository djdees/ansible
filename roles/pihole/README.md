
---

### roles/pihole/README.md

```markdown
# pihole role

Installs and configures Pi-hole DNS ad-blocking software.

## Features

- Installs Pi-hole packages
- Configures Pi-hole with custom settings
- Manages service state and updates

## Usage

```yaml
- hosts: piholes
  roles:
    - pihole
