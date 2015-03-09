#!/usr/bin/env python3

import os
import subprocess
import sys

## ----------------------------------------------------------------------------
#                                  Utilities

def check_root():
    """
    Print error message and exit program if current user doesn't have
    root mode.
    """
    if os.geteuid() != 0:
        print("This script requires root priviledges.", file=sys.stderr)
        sys.exit(1)

def apt_get(*args):
    """
    Run apt-get with given 'args' in non-interactive (batch) mode.
    """

    batch_args = [
        '-y',
        '-o', 'Dpkg::Options::="--force-confdef"',
        '-o', 'Dpkg::Options::="--force-confold"'
    ]

    subprocess.check_call(
        ['apt-get'] + list(args) + batch_args,
        env={'DEBIAN_FRONTEND': 'noninteractive'}
    )

def write_sources_list(repo='stable', mirror='us.debian.org'):
    """
    Write /etc/apt/sources.list with 'deb' and 'deb-src' entries for
    given mirror and repository type.
    """

    r = '%s http://%s/debian %s main non-free contrib'

    with open('/etc/apt/sources.list', 'wt') as f:
        f.write(r % ('deb', mirror, repo))
        f.write(r % ('deb-src', mirror, repo))

def upgrade_to(repo):
    """
    Upgrade the whole system to 'testing' or 'unstable'.
    """

    write_sources_list(repo)
    apt_get('update')
    apt_get('dist-upgrade')
    apt_get('autoremove')

def install_locales(locales):
    """
    Install given locales.
    """

    # 1. Generate locale.gen
    with open('/etc/locale.gen', 'wt') as f:
        for locale in locales:
            region, encoding = locale.split('.')
            f.write('%s %s\n' % (locale, encoding))

    # 2. Run 'locale-gen'
    subprocess.check_call(['locale-gen'])

def which(program_name):
    result = subprocess.check_output(['which', program_name])
    if not result:
        raise Exception('Program %s not found in PATH' % program_name)
    return result

def set_default_program(role, program):
    subprocess.check_call(['update-alternatives', '--set', role, program])

def install_packages(*packages):
    apt_get('install', *packages)

## ----------------------------------------------------------------------------
#                                     Main

def main():
    check_root()
    upgrade_to('testing')
    upgrade_to('unstable')
    install_locales('en_US.UTF-8')
    install_packages(
        # System
        'openssh-client',
        'openssh-server',
        'rsync',
        'vim',
        'htop',
        'ranger',
        'unrar',
        'unzip',
        'curl',
        'wget',
        # Development
        'subversion',
        'git',
        'cmake',
        'binutils',
        'diffutils',
        'gdb',
        # GUI
        'xorg',
        'i3',
        'i3status',
        'arandr',
        'network-manager',
        'network-manager-gnome',
        'iceweasel',
        'evince',
        'feh',
        'fontconfig',
        'flashplugin-nonfree',
        'ttf-mscorefonts-installer',
        'graphviz',
        'gnome',
        'gedit',
        'xclip',
        'xserver-xorg',
        'xterm'
    )
    #set_default_program('editor', which('vim'))
    #set_default_program('pager', which('less'))
    set_default_program('x-terminal-emulator', which('uxterm'))
    set_default_program('x-www-browser', which('iceweasel'))
    set_default_program('x-window-manager', which('i3'))

if __name__ == '__main__':
    main()
