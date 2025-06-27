# language-nodejs role

This role installs Node.js versions and global npm packages using asdf.

## Variables

- `asdf_root`: Path to asdf root (should be set externally, e.g. `~/.asdf`)
- `nodejs_versions`: List of Node.js versions to install
- `nodejs_default_version`: Default Node.js version to set globally
- `nodejs_packages`: List of global npm packages to install

## Example usage

Make sure you have the `asdf` role installed and run this role after it.
