# Client-Admin
A client admin plugin for SourcePython. Gives access to decorators and permissions to create dynamic client commands for users of the server.


Usage of the available decorators.
```
from .commands.manager import command_manager
from .permissions import check_permission

@check_permission(<character>)
@command_manager.add_command(<name of command>)
def _appropriate_function_name(player, <arguments for command>, ...):
    pass
```

Example using the decorators.
```
from .commands.manager import command_manager
from .commands.filters import Filter
from .permissions import check_permission

import operator

operators = {
	'+': operator.add,
	'-': operator.sub,
}

@check_permission('A')
@command_manager.add_command('speed')
def _change_speed(player, filters, operator, value):
	op = operators[operator]
	
	for target in Filter(filters, player):
		target.speed = op(target.speed, float(value))
```
To use this client command a user with permission character 'A', must input in their console.
Example uses:
- `"speed @ct + 0.2"` will give all CTs + 0.2 to their speed.
- `"speed #Predz + 0.2"` will give player named Predz + 0.2 to his speed.
- `"speed @ct,#Predz + 0.2"` will give all CTs and player named Predz + 0.2 to their speed.


To add a permission character to a player, go to the permissions.py and alter the dictionary provided.
```
admin_config = {
	
	## EXAMPLE
	'STEAM_1:0:120220385': 'ABC',
	'<players steamid>': '<permission characters>',

}
```
