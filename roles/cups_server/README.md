
---

### roles/cups/README.md

```markdown
# cups role

Installs and configures CUPS printing system along with Avahi for AirPrint support.

## Features

- Installs CUPS and related packages (hplip, hpijs-ppd)
- Deploys custom CUPS configuration files
- Installs and configures Avahi daemon for service discovery
- Provides service handlers for restarting cups and avahi-daemon

## Usage

```yaml
- hosts: print_servers
  roles:
    - cups
