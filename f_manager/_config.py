import pathlib

from environs import Env

env = Env()
env.read_env("settings.env")

# TODO:
#     * do not raise exception if variable is not set but make them equals to None all usages have to check this before using

game_folder: pathlib.Path = env.path("GAME_FOLDER")
mods_file: pathlib.Path = env.path("MOD_LIST_FILE")
profiles_dir: pathlib.Path = env.path("PROFILES_DIR")

LOG_LEVEL = env.log_level("LOG_LEVEL")
