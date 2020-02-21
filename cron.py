import utils


def autoupdate_key():
    """Key auto-renewal every 8 hours"""
    try:
        utils.update_keys()
        utils.format_key()
    except:
        print('Error in autoupdate_key()')
