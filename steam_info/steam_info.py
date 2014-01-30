import os
import ctypes
from collections import namedtuple


Friend = namedtuple("Friend", "id, username")


class EFriendFlags:
    k_EFriendFlagNone           = 0x00
    k_EFriendFlagBlocked        = 0x01
    k_EFriendFlagFriendshipRequested    = 0x02
    k_EFriendFlagImmediate      = 0x04
    k_EFriendFlagClanMember     = 0x08
    k_EFriendFlagOnGameServer   = 0x10 
    k_EFriendFlagRequestingFriendship = 0x80
    k_EFriendFlagRequestingInfo = 0x100
    k_EFriendFlagIgnored        = 0x200
    k_EFriendFlagIgnoredFriend  = 0x400
    k_EFriendFlagSuggested      = 0x800
    k_EFriendFlagAll            = 0xFFFF


_steam_info_dll = ctypes.cdll.LoadLibrary(
    os.path.join(os.path.dirname(__file__), r"steam_info.dll")
)
_steam_info_dll.get_steam_id.restype = ctypes.c_uint64
_steam_info_dll.get_steam_username.restype = ctypes.c_char_p
_steam_info_dll.get_friend_by_index.restype = ctypes.c_uint64
_steam_info_dll.get_friend_username.restype = ctypes.c_char_p
_steam_info_dll.get_friend_username.argtypes = [ctypes.c_uint64]


def get_steam_id():
    """ Returns 64 unsigned integer. 0 is returned on error
    """
    return _steam_info_dll.get_steam_id()


def get_steam_username():
    """ Returns steam username str. Empty string is returned on error
    """
    return _steam_info_dll.get_steam_username().decode("utf-8")


def get_friend_count(friend_flags=EFriendFlags.k_EFriendFlagAll):
    """ Returns friends count, -1 on error. You can filter friends with flags, 
    e.g. EFriendFlags.k_EFriendFlagSuggested | EFriendFlags.k_EFriendFlagIgnored
    """
    return _steam_info_dll.get_friend_count(friend_flags)


def get_friend_by_index(index, friend_flags=EFriendFlags.k_EFriendFlagAll):
    """ Returns Friend(steam_id, username) for concrete index. None returned on error
    """
    steam_id = _steam_info_dll.get_friend_by_index(index, friend_flags)
    if not steam_id:
        return None
    name = get_friend_username(steam_id)
    return Friend(steam_id, name)


def get_friend_username(steam_id):
    """ Returns friends username string for concrete steam_id. Empty string on error
    """
    return _steam_info_dll.get_friend_username(steam_id).decode("utf-8")


def iter_friends(friend_flags=EFriendFlags.k_EFriendFlagAll):
    """ Yields Friend(id, username) for all friends
    """
    count = get_friend_count(friend_flags)
    for i in range(count):
        yield get_friend_by_index(i, friend_flags)
