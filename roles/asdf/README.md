# asdf role

This role installs the [asdf version manager](https://asdf-vm.com/) for managing multiple runtime versions.

## Variables

- `asdf_install_path`: Directory to install asdf (default: `~/.asdf`)
- `asdf_plugins`: List of plugins to install (optional)

## Usage

Run this role first to set up asdf before installing any language versions.

```yaml
- hosts: all
  roles:
    - asdf
