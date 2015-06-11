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
        config_out_file.write(d)

def read_config_from_file(configpath):
    """
    Read the configuration from the user-accessible config file.

    Raise 'NoValidConfigfileError' if this is not possible.

    Return:
        dict   with (configvariable_name, configvariable_value)
    """
    try:
        with open(configpath, 'r') as configfile:
            try:
                cfg = yaml.safe_load(configfile)
            except Exception as e:
                print("error while loading: {0}".format(e))
                raise NoValidConfigfileError(e)
    except IOError:
        cfg = {}
        raise NoValidConfigfileError(
            "config.yml not found at {0}".format(configpath))
    else:
        if not isinstance(cfg, dict):
            raise NoValidConfigfileError(
                "Invalid configfile at {0}".format(configpath))
        return cfg


def load_config():
    """
    Load configuration dict either from YAML config-file or from defaults.
    """
    configpath = os.path.join(config_dir, config_filename)
    ethunder.config = {}
    ethunder.config.update(default_config)
    try:
        cfg_from_file = read_config_from_file(configpath)
    except NoValidConfigfileError:
        raise
    else:
        ethunder.config.update(cfg_from_file)


def configurate():
    """
    Make sure we have the needed configuration values.
    """
    try:
        load_config()
    except NoValidConfigfileError:
        create_default_configfile()

if __name__ == "__main__":
    configurate()
