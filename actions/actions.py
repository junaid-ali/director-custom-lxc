#!/usr/bin/python

import os
import sys

sys.path.append('hooks/')

from charmhelpers.core.hookenv import action_fail
from pg_dir_utils import (
    restart_pg
)


def restart(args):
    """Pause the Ceilometer services.
    @raises Exception should the service fail to stop.
    """
    restart_pg('lxc')


# A dictionary of all the defined actions to callables (which take
# parsed arguments).
ACTIONS = {"restart": restart}


def main(args):
    action_name = os.path.basename(args[0])
    try:
        action = ACTIONS[action_name]
    except KeyError:
        return "Action %s undefined" % action_name
    else:
        try:
            action(args)
        except Exception as e:
            action_fail(str(e))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
