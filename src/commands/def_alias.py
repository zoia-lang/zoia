from exception import EvalError
from validation import Signature, WordTy, ContentTy

from commands._base import _ACommand

_ARG_KEY = 'key'
_ARG_VAL = 'val'

class DefAliasCmd(_ACommand):
    # FIXME Idea/Wishlist for an API
    # req_state = StateRequest(
    #     var={
    #         'seen_alias_key': set,
    #         'alias_dict': dict,
    #     },
    # )
    cmd_name = 'def_alias'
    signature = Signature(
        std_only={
            _ARG_KEY: WordTy(),
            _ARG_VAL: ContentTy(),
        },
    )
    __slots__ = ()

    def exec_command(self, state):
        alias_key = self.cmd_args[_ARG_KEY]
        seen_alias_keys = state.var['seen_alias_keys']
        if alias_key in seen_alias_keys:
            raise EvalError(self.cmd_args_pos[_ARG_KEY],
                            f"Duplicate alias key '{alias_key}'")
        seen_alias_keys.add(alias_key)
        state.var['alias_dict'][alias_key] = self.cmd_args[_ARG_VAL]

CMD_TYPE = DefAliasCmd
