# Ansible

A collection of Ansible components for managing my home lab. No passwords stashed in it and all very generic on purpose. 

## Commands:

- Distribute ansible host's ssh keys
    ```sh
    ansible-playbook -i inventory/inventory.yml playbooks/copy_ssh_keys.yml --ask-pass
    ```
    Can be used with --limit if just interacting with specific host(s).
- 

## Installing Ansible

Not that I'll forget, but cut & paste is convenient

```sh
sudo apt-get update && sudo apt-get upgrade -y
sudo apt install ansible
```