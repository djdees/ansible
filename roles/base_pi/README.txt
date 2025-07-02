# base_pi role

Configures base system settings for Raspberry Pi hosts.

## Features

- Creates and configures local user accounts
- Ensures required system groups exist
- Deploys a standardized public SSH key to all managed user accounts
- Allows passwordless sudo for the `admin` group
- Configures SSH server settings
- Disables Wi-Fi hardware and services on headless systems (optional)
- Applies static IP network configuration (if using `network-config` dependency)

## Variables

- `users`: list of user accounts to create and configure
- `standard_groups`: list of required system groups (typically `admin` and `sudo`)
- `ssh_public_key_path`: path to a public SSH key on the Ansible control host to install for each managed user (default: `/home/djdees/.ssh/id_ed25519.pub`)

## Notes

- The `ssh_public_key_path` variable ensures a consistent, secure SSH key is deployed to all managed accounts. The key file should be present on the Ansible control node at the specified path.
- Wi-Fi disabling tasks are controlled via tags (`wireless`) and can optionally trigger a reboot.
- Network configuration uses systemd-networkd and may require inventory host_vars or group_vars to define `gateway`, `dns_servers`, etc.

## Usage

```yaml
- hosts: pihole
  roles:
    - base_pi
