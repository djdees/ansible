
---

### roles/base_home/README.md

```markdown
# base_home role

Configures home directory environments for users on Raspberry Pi or other systems.

## Features

- Installs and configures user shells (bash, zsh)
- Copies user dotfiles and shell configurations
- Handles multi-user setups based on group_vars/users.yml
- Manages shell environment paths

## Variables

- `users`: list of user accounts to configure
- `default_shell`: shell to use per user (bash or zsh)
- `shell_paths`: shell paths and configuration files

## Usage

```yaml
- hosts: lab
  roles:
    - base_home
