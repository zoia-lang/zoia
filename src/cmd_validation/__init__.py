from cmd_validation.default import *
from cmd_validation.tys import *
from cmd_validation.signature import *
from cmd_validation.varargs import *

# # \def_alias
# s = Signature(
#     std_only={
#         'key': WordTy(),
#         'val': ContentTy(),
#     },
# )
# print('\\def_alias' + s.compact())
#
# # \header
# s = Signature(
#     std_only={
#         'ty': WordTy(),
#     },
#     varargs=Varargs(VARARGS_EITHER_OR, AnyTy()),
# )
# print('\\header' + s.compact())
#
# # \add
# s = Signature(
#     varargs=Varargs(VARARGS_STD, IntTy()),
#     ret_ty=IntTy(),
# )
# print('\\add' + s.compact())
#
# # \complex
# s = Signature(
#     std_only={
#         'a1': IntTy(),
#         'a2': WordTy(),
#         # Note: once you start adding defaults, all later args must have
#         # defaults too.
#         'a3': Default(TextTy(), 'bla bla bla'),
#     },
#     either_or={
#         'b1': Default(IntTy(), '0'),
#         'b2': Default(WordTy(), 'foo'),
#         'b3': Default(TextTy(), ''),
#     },
#     kwd_only={
#         'c1': Default(IntTy(), '1'),
#         'c2': Default(WordTy(), ''),
#         'c3': Default(TextTy(), 'bar qux'),
#     },
#     varargs=Varargs(VARARGS_KWD, TextTy()),
#     ret_ty=TextTy(),
# )
# print('\\complex' + s.compact())
#
# # \lbracket
# s = Signature(
#     ret_ty=WordTy(),
# )
# print('\\lbracket' + s.compact())
