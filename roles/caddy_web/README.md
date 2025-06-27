# caddy_web role

Installs and configures the Caddy web server for serving multiple static sites.

## Features

- Installs Caddy package
- Creates necessary users and groups (`www-data`)
- Sets up directories and symlinks for site content
- Deploys Caddyfile configuration supporting multiple hostnames
- Manages Caddy service via systemd

## Variables

- Sites and content directories are generally managed via templates and task files.

## Usage

```yaml
- hosts: web_servers
  roles:
    - caddy_web
