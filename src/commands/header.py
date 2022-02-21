from commands._base import _ACommand

from validation import Signature, HeaderKindTy, AnyTy, Varargs, \
    VARARGS_EITHER_OR

class HeaderCmd(_ACommand):
    cmd_name = 'header'
    signature = Signature(
        std_only={
            'header_kind': HeaderKindTy(),
        },
        # TODO Do we have a use case for >1 argument passed to the header? If
        #  not, drop the varargs
        varargs=Varargs(VARARGS_EITHER_OR, AnyTy()),
    )
    __slots__ = ()

    def exec_command(self):
        pass

CMD_TYPE = HeaderCmd
