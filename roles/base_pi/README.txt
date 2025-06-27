
---

### roles/base_pi/README.md

```markdown
# base_pi role

Configures base system settings for Raspberry Pi nodes.

## Features

- System updates and package installation
- Basic network and hostname setup
- User and shell environment preparation
- Calls `base_home` internally or alongside it for user setup

## Usage

```yaml
- hosts: lab
  roles:
    - base_pi
