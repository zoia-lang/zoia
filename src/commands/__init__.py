import importlib
import pkgutil
import sys

from exception import ValidationError

def get_command_type(node):
    try:
        return _cmd_map[node.cmd_name]
    except TypeError: # _cmd_map is None
        _init_cmd_map()
        return get_command_type(node)
    except KeyError: # node.cmd_name not in _cmd_map
        raise ValidationError(
            node.src_pos,
            f"Unknown command '\\{node.cmd_name}'")

_cmd_map: dict | None = None

def _init_cmd_map():
    global _cmd_map
    _cmd_map = {}
    commands_name = __name__
    commands_path = sys.modules[commands_name].__path__
    for _imp, mod_name, _is_pkg in pkgutil.iter_modules(commands_path):
        # Internal module, does not define a command
        if mod_name.startswith('_'):
            continue
        module = importlib.import_module(f'{commands_name}.{mod_name}')
        cmd_type = getattr(module, 'CMD_TYPE')
        _cmd_map[cmd_type.cmd_name] = cmd_type
