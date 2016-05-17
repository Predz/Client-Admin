'''

	Permission management for access to
	commands and menus. Based upon using
	players steamids and ASCII characters.

'''

admin_config = {
	
	## EXAMPLE
	'STEAM_1:0:120220385': 'ABC',

}

## ================ DEFAULT DICT ====================

from collections import defaultdict

admin_permissions = defaultdict(str)

admin_permissions.update(admin_config)

## =============== ALL DECLARTION ===================

__all__ = (
	'check_permission',
	)

## ================== DECORATOR =====================

from engines.server import engine_server

def check_permission(character):
	def decorator(method):
		def new(player, *args):
			if character in admin_permissions[player.steamid]:
				return method(player, *args)
			else:
				engine_server.client_printf(player.edict,
					'CA - You do not have permissions to use this command.\n')
		return new
	return decorator