
---

### roles/unbound/README.md

```markdown
# unbound role

Installs and configures Unbound DNS resolver.

## Features

- Installs Unbound package
- Deploys custom Unbound configuration files
- Manages Unbound service lifecycle

## Usage

```yaml
- hosts: dns_servers
  roles:
    - unbound
