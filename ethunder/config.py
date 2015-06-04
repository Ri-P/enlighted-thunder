# -*- coding: utf-8 -*-
"""
Provide tools to load configuration parameters from text-file using YAML.
"""

from __future__ import print_function
from __future__ import unicode_literals

import yaml
import os.path
import appdirs
import shutil
import datetime
import ethunder
from ethunder import EThunderError

__author__ = "Richard Pfeifer"


config_dir = appdirs.user_config_dir("ethunder", appauthor=None)
config_filename = "config.yml"

default_config = {
    "path_to_rainbow": "ick schwörs µus",
    "value1": 0,
    "is_awesome": True,
}


class NoValidConfigfileError(EThunderError):
    pass


def construct_yaml_str(self, node):
    """
    Override the default string handling function to always return unicode
    objects.
    """
    return self.construct_scalar(node)
yaml.Loader.add_constructor("tag:yaml.org,2002:str", construct_yaml_str)
yaml.SafeLoader.add_constructor("tag:yaml.org,2002:str", construct_yaml_str)


def create_default_configfile():
    """
    Create a configfile with default config-values at the configpath.
    """
    config_path = os.path.join(config_dir, config_filename)
    if os.path.isfile(config_path):
        backup_filename = "config_backup_{0}.yml".format(
            datetime.datetime.now().isoformat())
        backup_filename = backup_filename.replace(":", "-")
        backup_filepath = os.path.join(config_dir, backup_filename)
        shutil.move(config_path, backup_filepath)
    with open(config_path, 'w') as config_out_file:
        d = yaml.safe_dump(
            ethunder.config,
            default_flow_style=False,
            encoding=('utf-8'),
            allow_unicode=True)
        print(d)
        config_out_file.write(d)

def set_config():
    """
    Set configuration either from YAML config-file or from defaults.
    """
    configpath = os.path.join(config_dir, config_filename)
    ethunder.config = {}
    ethunder.config.update(default_config)
    try:
        try:
            print("try open")
            with open(configpath, 'r') as configfile:
                print("opened")
                try:
                    cfg = yaml.safe_load(configfile)
                except Exception as e:
                    print("error while loading: {0}".format(e))
                    raise NoValidConfigfileError(e)
                else:
                    print("should have cfg")
        except IOError:
            print("create empty cfg")
            cfg = {}
            raise NoValidConfigfileError(
                "config.yml not found at {0}".format(configpath))
        else:
            if not isinstance(cfg, dict):
                raise NoValidConfigfileError(
                    "Invalid configfile at {0}".format(configpath))
    except NoValidConfigfileError:
        raise
    else:
        ethunder.config.update(cfg)
        print("Following config was read: {0}".format(ethunder.config))


def configurate():
    """
    Make sure we have the needed configuration values.
    """
    try:
        set_config()
    except NoValidConfigfileError:
        create_default_configfile()

if __name__ == "__main__":
    configurate()
