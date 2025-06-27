#!/usr/bin/python

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import subprocess
from ansible.module_utils.basic import AnsibleModule

def run_cmd(module, cmd, check_rc=True):
    rc, out, err = module.run_command(cmd, check_rc=check_rc)
    return rc, out.strip(), err

def main():
    module = AnsibleModule(
        argument_spec=dict(
            plugin=dict(type='str', required=True),
            version=dict(type='str', required=False),
            global_install=dict(type='bool', default=False),
            user=dict(type='str', required=True),
            asdf_dir=dict(type='str', default="~/.asdf"),
            state=dict(type='str', choices=['present', 'absent'], default='present'),
        ),
        supports_check_mode=True
    )

    plugin = module.params['plugin']
    version = module.params['version']
    global_install = module.params['global_install']
    user = module.params['user']
    asdf_dir = os.path.expanduser(module.params['asdf_dir'])
    state = module.params['state']

    changed = False
    plugin_dir = os.path.join(asdf_dir, 'plugins', plugin)
    env = os.environ.copy()
    env["HOME"] = os.path.expanduser(f"~{user}")
    env["ASDF_DIR"] = asdf_dir

    # Install plugin if missing
    if not os.path.isdir(plugin_dir):
        if module.check_mode:
            module.exit_json(changed=True)
        cmd = ['sudo', '-u', user, 'asdf', 'plugin-add', plugin]
        rc, out, err = run_cmd(module, cmd)
        changed = True

    if state == 'present' and version:
        # Check if version installed
        versions_dir = os.path.join(asdf_dir, 'installs', plugin, version)
        if not os.path.isdir(versions_dir):
            if module.check_mode:
                module.exit_json(changed=True)
            cmd = ['sudo', '-u', user, 'asdf', 'install', plugin, version]
            rc, out, err = run_cmd(module, cmd)
            changed = True

        # Set global version if requested
        if global_install:
            cmd = ['sudo', '-u', user, 'asdf', 'global', plugin, version]
            rc, out, err = run_cmd(module, cmd)
            changed = True

    module.exit_json(changed=changed)

if __name__ == '__main__':
    main()
