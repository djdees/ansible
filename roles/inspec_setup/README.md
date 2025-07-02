# inspec_setup role

Installs and manages the InSpec tool on Debian/Ubuntu hosts.

## Features

- Installs InSpec `.deb` package from Chef's official repository
- Checks current installed InSpec version and upgrades only if needed
- Uses version variable from `group_vars/versions.yml` or role defaults
- Cleans up temporary installation files

## Variables

- `inspec_version` (default: from role defaults)
  - Version of InSpec to install, typically set in `group_vars/versions.yml` as `inspec_default_version`

## Requirements

- Debian/Ubuntu based hosts (adjust URLs if using other distros)
- `curl` installed (role ensures this)

## Usage

```yaml
- hosts: all
  roles:
    - inspec_setup
