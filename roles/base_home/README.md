
---

### `roles/base_home/README.md`

```markdown
# base_home role

Configures home directory environments and shell setups for user accounts.

## Features

- Installs and configures user shells (bash, zsh, etc.)
- Copies user-specific dotfiles and shell configuration files
- Ensures `.ssh` directories and `authorized_keys` are properly created
- Deploys a standardized public SSH key to all managed user accounts
- Handles multi-user setups based on `group_vars/all.yml`

## Variables

- `users`: list of user accounts to configure
- `default_shell`: shell to assign to new users (default: bash)
- `shell_paths`: mapping of shell names to their filesystem paths
- `ssh_public_key_path`: path to a public SSH key on the Ansible control host to install for each managed user

## Notes

- The shared `ssh_public_key_path` ensures a consistent SSH key is deployed to all managed users created by this role.
- This role assumes user accounts and required system groups are already managed (typically by `base_pi` or equivalent).

## Usage

```yaml
- hosts: lab
  roles:
    - base_home
