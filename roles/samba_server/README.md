
---

### roles/samba_server/README.md

```markdown
# samba_server role

Installs and configures Samba server for file and printer sharing.

## Features

- Installs Samba package
- Deploys custom smb.conf configuration
- Creates spool directories for printing
- Manages Samba service via systemd

## Variables

- Samba configuration can be customized via `templates/smb.j2`

## Usage

```yaml
- hosts: samba_servers
  roles:
    - samba_server
