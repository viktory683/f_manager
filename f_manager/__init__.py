from f_manager import _config as config
from f_manager import _exceptions as exceptions
from f_manager import _helpers as helpers
from f_manager._launcher import Launcher, Save
from f_manager._logger import logger
from f_manager._mod import Mod, ModController
from f_manager._profile import Profile, TempProfile

# TODO:
#     * should be better to put here some docs of module

# NOTE load profiles without using --mod-directory option
# NOTE no need at all to create a lot of folder containing ~1GB of mods

# * some-like of technical specification

# ! first start has to create a directory containing .json files with mods
# ! information of default mod-list.json file format and default profile

# ! default profile is
# ! {
# !   'mods':
# !       [
# !           {
# !               'name' : 'base',
# !               'enabled': true
# !           },
# !           {
# !               'name': 'mod-name.zip',
# !               'enabled': false
# !           }
# !           ...
# !       ]
# ! }
# ! and it can't be removed or renamed

# ! every launch should scan mods folder for newly downloaded mods and update
# ! created profiles with {'name': 'new-mod', 'enabled': false}
# ! newly downloaded mod updates all profiles too
# ! so set and length of mods in profiles will be always the same

# ! if profile has mod that is not being downloaded ask user to download it
# ! (on load that profile need to be extended of all downloaded mods)

# *

# V enable/disable mod/mods in profiles
# V create/delete profiles
# V rename profiles
# V load game with profile
# V delete mod/mods
#     V disable/enable for all
#     V download
#     V upgrade mod
#         V upgrade only mods from profile
