# -*- coding: utf-8 -*-
#
# GPL License and Copyright Notice ============================================
#
#   This file is part of Zoia, a language for writing fiction.
#   Copyright (C) 2021-2023 Infernio
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# =============================================================================
"""This module houses tests related to validation of Zoia code."""
from test.base import ATestParser

import pytest

from ast_nodes import CommandNode, ZoiaFileNode
from exception import ValidationError
from validation import Signature, Default, AnyTy, ATy, Varargs, NoneTy, \
    VARARGS_STD, VARARGS_EITHER_OR, VARARGS_KWD, WordTy, IntTy, PureTextTy, \
    ContentTy, FloatTy, HeaderKindTy, TagTy, TextTy

# Signature syntax tests begin here
class _ATestSigSyntax:
    """Base class for signature syntax tests. Provides a method for creating
    signatures based on class attributes mirroring those of Signature."""
    _std_only: dict = {}
    _either_or: dict = {}
    _kwd_only: dict = {}
    _varargs: Varargs | None = None
    _ret_ty: ATy = NoneTy()

    def _mk_sig(self):
        """Creates a new Signature based on the class attributes of this test
        class, initializes its default values and returns it."""
        ret_sig = Signature(std_only=self._std_only, either_or=self._either_or,
                            kwd_only=self._kwd_only, varargs=self._varargs,
                            ret_ty=self._ret_ty)
        ret_sig.init_default_values()
        return ret_sig

class _ATestSigSyntaxPass(_ATestSigSyntax):
    """Base class for passing signature syntax tests."""
    def test_sig_syntax_passes(self):
        """Tests that the signature is created successfully, without raising a
        syntax error."""
        self._mk_sig()

class _ATestSigSyntaxFail(_ATestSigSyntax):
    """Base class for failing signature syntax tests."""
    _exp_error: str

    def test_sig_syntax_fails(self):
        """Tests that creation of the signature fails without a syntax error
        with an error message matching _exp_error."""
        with pytest.raises(SyntaxError) as exc_info:
            self._mk_sig()
        assert str(exc_info.value) == self._exp_error

# Passing signature syntax tests begin here
class TestSigSyntaxStdVarargs(_ATestSigSyntaxPass):
    """Std-only varargs accompanied by only std-only parameters are
    accepted."""
    _std_only = {
        'foo': AnyTy(),
    }
    _varargs = Varargs(VARARGS_STD, AnyTy())

class TestSigSyntaxEitherVarargs(_ATestSigSyntaxPass):
    """Either-or varargs accompanied by std-only and either-or parameters are
    accepted."""
    _std_only = {
        'foo': AnyTy(),
    }
    _either_or = {
        'bar': AnyTy(),
    }
    _varargs = Varargs(VARARGS_EITHER_OR, AnyTy())

class TestSigSyntaxKwdVarargs(_ATestSigSyntaxPass):
    """Kwd-only varargs accompanied by std-only, either-or and kwd-only
    parameters are accepted."""
    _std_only = {
        'foo': AnyTy(),
    }
    _either_or = {
        'bar': AnyTy(),
    }
    _kwd_only = {
        'qux': AnyTy(),
    }
    _varargs = Varargs(VARARGS_KWD, AnyTy())

# Failing signature syntax tests begin here
class TestSigSyntaxNonDefaultAfterDefault(_ATestSigSyntaxFail):
    """A non-Default parameter may not follow a Default parameter."""
    _std_only = {
        'foo': Default(AnyTy(), 'bar'),
        'qux': AnyTy(),
    }
    _exp_error = ('A Signature may not have non-Default validators after a '
                  'Default validator')

class TestSigSyntaxDuplicateName(_ATestSigSyntaxFail):
    """Parameter names may not be duplicated across parameter kinds (within a
    single parameter kind the fact that we're dealing with a dict already takes
    care of that problem)."""
    _std_only = {
        'foo': AnyTy(),
    }
    _either_or = {
        'foo': AnyTy(),
    }
    _exp_error = "Duplicate parameter name 'foo'"

class TestSigSyntaxInvalidVarargsType(_ATestSigSyntaxFail):
    """The 'varargs' parameter only takes a Varargs object."""
    _varargs = AnyTy()
    _exp_error = "'varargs' kwarg must have Varargs type"

class TestSigSyntaxStdVarargsEitherOr(_ATestSigSyntaxFail):
    """Varargs may not have std-only kind when either-or parameters are
    present."""
    _either_or = {
        'foo': AnyTy(),
    }
    _varargs = Varargs(VARARGS_STD, AnyTy())
    _exp_error = ('Std-only varargs are not allowed when either-or validators '
                  'are present')

class TestSigSyntaxStdVarargsKwdOnly(_ATestSigSyntaxFail):
    """Varargs may not have std-only kind when kwd-only parameters are
    present."""
    _kwd_only = {
        'foo': AnyTy(),
    }
    _varargs = Varargs(VARARGS_STD, AnyTy())
    _exp_error = ('Std-only varargs are not allowed when kwd-only validators '
                  'are present')

class TestSigSyntaxEitherVarargsKwdOnly(_ATestSigSyntaxFail):
    """Varargs may not have either-or kind when kwd-only parameters are
    present."""
    _kwd_only = {
        'foo': AnyTy(),
    }
    _varargs = Varargs(VARARGS_EITHER_OR, AnyTy())
    _exp_error = ('Either-or varargs are not allowed when kwd-only validators '
                  'are present')

def test_sig_syntax_varargs_default():
    """Varargs may not have Default values."""
    with pytest.raises(SyntaxError) as exc_info:
        # noinspection PyTypeChecker
        Varargs(VARARGS_STD, Default(AnyTy(), 'foo'))
    assert str(exc_info.value) == 'Varargs may not have Default values'

def test_sig_syntax_validate_default():
    """If (type) validation of a default value fails, a syntax error should be
    raised."""
    with pytest.raises(SyntaxError) as exc_info:
        Default(WordTy(), 'two words').init_default_value()
    assert str(exc_info.value) == ('Failed to validate a Signature default '
                                   'value')

# Signature validation tests begin here
class _ATestSigVal(ATestParser):
    """Base class for signature validation tests."""
    _signature: Signature

    def _validate_signature(self):
        """Validates this class' command's argument against this class'
        signature."""
        self._signature.init_default_values()
        test_node = self._parse_src().lines[1].elements.elements[0]
        if not isinstance(test_node, CommandNode):
            pytest.fail('_test_src must contain a single command')
        self._signature.validate_args(test_node)

class _ATestSigValPass(_ATestSigVal):
    """Base class for passing signature validation tests."""
    def test_sig_passes(self):
        """Tests that validation succeeds for this class' signature and
        source."""
        self._validate_signature()

class _ATestSigValFail(_ATestSigVal):
    """Base class for failing signature validation tests."""
    _exp_error: str

    def test_sig_fails(self):
        """Tests that validation fails for this class' signature and source."""
        with pytest.raises(ValidationError) as exc_info:
            self._validate_signature()
        assert self._exp_error in str(exc_info.value)

# Passing signature validation tests begin here
class TestSigValEitherOr1(_ATestSigValPass):
    """Either-or parameters can be filled by standard arguments."""
    _signature = Signature(
        either_or={
            'a': AnyTy(),
            'b': AnyTy()
        }
    )
    _test_src = '\\foo[apple; banana]'

class TestSigValEitherOr2(TestSigValEitherOr1):
    """Either-or parameters can be filled by keyword arguments."""
    _test_src = '\\foo[a = apple; b = banana]'

class TestSigValEitherOr3(TestSigValEitherOr1):
    """Either-or parameters can be filled by mixed arguments."""
    _test_src = '\\foo[apple; b = banana]'

class TestSigValVarargsStdOnly(_ATestSigValPass):
    """A signature with std-only varargs may accept any number of standard
    arguments."""
    _signature = Signature(
        varargs=Varargs(VARARGS_STD, AnyTy()),
    )
    _test_src = '\\foo[a; b; c; d; e; f; g]'

class TestSigValVarargsEitherOr1(_ATestSigValPass):
    """A signature with either-only varargs may accept any number of standard
    arguments."""
    _signature = Signature(
        varargs=Varargs(VARARGS_EITHER_OR, AnyTy()),
    )
    _test_src = '\\foo[a; b; c; d; e; f; g]'

class TestSigValVarargsEitherOr2(_ATestSigValPass):
    """A signature with either-only varargs may accept any number of keyword
    arguments."""
    _signature = Signature(
        varargs=Varargs(VARARGS_EITHER_OR, AnyTy()),
    )
    _test_src = '\\foo[a = 1; b = 2; c = 3; d = 4; e = 5; f = 6; g = 7]'

class TestSigValVarargsEitherOr3(_ATestSigValPass):
    """A signature with either-only varargs may accept any number of mixed
    arguments."""
    _signature = Signature(
        varargs=Varargs(VARARGS_EITHER_OR, AnyTy()),
    )
    _test_src = '\\foo[a; b; c; d; e = 5; f = 6; g = 7]'

class TestSigValDefault(_ATestSigValPass):
    """Parameters with default values are optional and hence this command may
    be called without any arguments."""
    _signature = Signature(
        std_only={
            'a': Default(AnyTy(), 'apple'),
        },
        either_or={
            'b': Default(AnyTy(), 'banana'),
        },
        kwd_only={
            'c': Default(AnyTy(), 'citrus'),
        }
    )
    _test_src = '\\foo|'

class TestSigValFloat(_ATestSigValPass):
    """All three kinds of floats (standard, exponent and constant) should be
    accepted."""
    _signature = Signature(
        varargs=Varargs(VARARGS_STD, FloatTy()),
    )
    _test_src = '\\foo[1.0; 2.1; 1.3e2; 2e3; nan; NaN; inf; Inf]'

class TestSigValInt(_ATestSigValPass):
    """All four kinds of ints (decimal, hexadecimal, octal and binary)
    should be accepted."""
    _signature = Signature(
        varargs=Varargs(VARARGS_STD, IntTy()),
    )
    _test_src = ('\\foo[1; 01; 999_999; 0xF; 0X013B; 0xAAA_BBB; 0O07; 0o123; '
                 '0o777_777; 0b1; 0B010110; 0b111_000]')

class TestSigValTag(_ATestSigValPass):
    """A regular tag without commas should not be rejected."""
    _signature = Signature(
        std_only={
            'a': TagTy(),
        }
    )
    _test_src = ('\\foo[This is a tag - you can use it to specify various '
                 'metadata for a story]')

# Failing signature validation tests begin here
class TestSigValNoStds1(_ATestSigValFail):
    """A signature without any arguments should reject standard arguments."""
    _signature = Signature()
    _test_src = '\\foo[a]'
    _exp_error = '\\foo does not accept standard arguments'

class TestSigValNoStds2(TestSigValNoStds1):
    """A signature without any std-only arguments should reject standard
    arguments."""
    _signature = Signature(
        kwd_only={
            'b': AnyTy(),
        }
    )

class TestSigValNoKwds1(_ATestSigValFail):
    """A signature without any arguments should reject keyword arguments."""
    _signature = Signature()
    _test_src = '\\foo[a = b]'
    _exp_error = '\\foo does not accept keyword arguments'

class TestSigValNoKwds2(TestSigValNoKwds1):
    """A signature without any kwd-only arguments should reject keyword
    arguments."""
    _signature = Signature(
        std_only={
            'b': AnyTy(),
        }
    )

class TestSigValStdAfterKwd(_ATestSigValFail):
    """Standard arguments may not occur after keyword arguments."""
    _signature = Signature(
        std_only={
            'a': AnyTy(),
        },
        kwd_only={
            'b': AnyTy(),
        }
    )
    _test_src = '\\foo[b = bar; a]'
    _exp_error = 'Standard arguments may not be placed after keyword arguments'

class TestSigValKwdTwice(_ATestSigValFail):
    """Keyword arguments may only be specified once."""
    _signature = Signature(
        kwd_only={
            'fruit': AnyTy(),
        }
    )
    _test_src = '\\foo[fruit = pear; fruit = apple]'
    _exp_error = "Keyword argument 'fruit' specified twice"

class TestSigValTooManyStd(_ATestSigValFail):
    """If there are a limited number of std-accepting parameters (i.e. no
    compatible varargs), then specifying too many is illegal."""
    _signature = Signature(
        std_only={
            'a': AnyTy(),
            'b': AnyTy(),
        }
    )
    _test_src = '\\foo[apple; banana; citrus]'
    _exp_error = ('All 2 parameters that accept standard arguments have been '
                  'filled')

class TestSigValTooManyKwd(_ATestSigValFail):
    """If there are a limited number of kwd-accepting parameters (i.e. no
    compatible varargs), then specifying too many is illegal."""
    _signature = Signature(
        kwd_only={
            'a': AnyTy(),
            'b': AnyTy(),
        }
    )
    _test_src = '\\foo[a = apple; b = banana; c = citrus]'
    _exp_error = ('All 2 parameters that accept keyword arguments have been '
                  'filled')

class TestSigValMissingOneRequired(_ATestSigValFail):
    """If a single required argument is missing, an error should be shown."""
    _signature = Signature(
        std_only={
            'a': AnyTy(),
        }
    )
    _test_src = '\\foo|'
    _exp_error = "The required argument 'a' is missing"

class TestSigValMissingMultipleRequired(_ATestSigValFail):
    """If multiple required arguments areis missing, an error should be
    shown."""
    _signature = Signature(
        std_only={
            'a': AnyTy(),
            'b': AnyTy(),
            'c': AnyTy(),
        }
    )
    _test_src = '\\foo[apple]'
    _exp_error = "The required arguments 'b' and 'c' are missing"

class TestSigValUnknownCommand(_ATestSigValFail):
    """Unknown commands should be rejected."""
    _signature = Signature()
    _test_src = '\\foo|'
    _exp_error = "Unknown command '\\foo'"

    def _parse_src(self, test_src: str = None,
                   skip_validation: bool = True) -> ZoiaFileNode:
        # We want to validate here to recognize the unknown command
        return super()._parse_src(test_src, skip_validation=False)

class TestSigValNoneInContent(_ATestSigValFail):
    """Parameters of type Content should not accept None-returning commands."""
    _signature = Signature(
        std_only={
            'a': ContentTy(),
        }
    )
    _test_src = '\\foo[\\def_alias[A; B]]'
    _exp_error = ('Parameters of type Content only accept Content, but '
                  '\\def_alias returns None')

class TestSigValContentInText(_ATestSigValFail):
    """Parameters of type Text should only accept text fragments and commands
    that return Text."""
    _signature = Signature(
        std_only={
            'a': TextTy(),
        }
    )
    _test_src = '\\foo[*bar*]'
    _exp_error = ('Parameters of type Text only accept text fragments and '
                  'commands with a return type of Text (or one of its '
                  'subtypes)')

# TODO Add a test that a non-Text command is not accepted by a Text argument

class TestSigValInvalidFloat1(_ATestSigValFail):
    """The Python-style '1.' floats should be rejected by Float parameters."""
    _signature = Signature(
        std_only={
            'a': FloatTy(),
        }
    )
    _test_src = '\\foo[1.]'
    _exp_error = ('Parameters of type Float only accept valid floats, which '
                  '1. is not')

class TestSigValInvalidFloat2(TestSigValInvalidFloat1):
    """The Python-style '.0' floats should be rejected by Float parameters."""
    _test_src = '\\foo[.0]'
    _exp_error = ('Parameters of type Float only accept valid floats, which '
                  '.0 is not')

class TestSigValInvalidFloat3(TestSigValInvalidFloat1):
    """Random non-float words should be rejected by Float parameters."""
    _test_src = '\\foo[bla_bla_bla]'
    _exp_error = ('Parameters of type Float only accept valid floats, which '
                  'bla_bla_bla is not')

class TestSigValInvalidFloat4(TestSigValInvalidFloat1):
    """Ints should be rejected by Float parameters."""
    _test_src = '\\foo[123]'
    _exp_error = ('Parameters of type Float only accept valid floats, which '
                  '123 is not')

class TestSigValInvalidHeaderKind(_ATestSigValFail):
    """Random words should be rejected by HeaderKind parameters."""
    _signature = Signature(
        std_only={
            'hkt': HeaderKindTy(),
        },
    )
    _test_src = '\\foo[notakind]'
    _exp_error = 'Parameters of type HeaderKind only accept valid header kinds'

class TestSigValInvalidInt(_ATestSigValFail):
    """Random non-integer words should be rejected by Int parameters."""
    _signature = Signature(
        std_only={
            'a': IntTy(),
        }
    )
    _test_src = '\\foo[bla_bla_bla]'
    _exp_error = ('Parameters of type Int only accept valid integers, which '
                  'bla_bla_bla is not')

class TestSigValInvalidIntFloat(TestSigValInvalidInt):
    """Floats should be rejected by Int parameters."""
    _test_src = '\\foo[1.0]'
    _exp_error = ('Parameters of type Int only accept valid integers, which '
                  '1.0 is not')

class TestSigValInvalidIntDec(TestSigValInvalidInt):
    """Characters outside the decimal range should be rejected by Int
    parameters."""
    _test_src = '\\foo[0123456789A]'
    _exp_error = ('Parameters of type Int only accept valid integers, which '
                  '0123456789A is not')

class TestSigValInvalidIntHex(TestSigValInvalidInt):
    """Characters outside the hexadecimal range should be rejected by Int
    parameters."""
    _test_src = '\\foo[0x0123456789ABCDEFG]'
    _exp_error = ('Parameters of type Int only accept valid integers, which '
                  '0x0123456789ABCDEFG is not')

class TestSigValInvalidIntOct(TestSigValInvalidInt):
    """Characters outside the octal range should be rejected by Int
    parameters."""
    _test_src = '\\foo[0o012345678]'
    _exp_error = ('Parameters of type Int only accept valid integers, which '
                  '0o012345678 is not')

class TestSigValInvalidIntBin(TestSigValInvalidInt):
    """Characters outside the binary range should be rejected by Int
    parameters."""
    _test_src = '\\foo[0b012]'
    _exp_error = ('Parameters of type Int only accept valid integers, which '
                  '0b012 is not')

class TestSigValInvalidTag(_ATestSigValFail):
    """Parameters of type Tag may not include commas."""
    _signature = Signature(
        std_only={
            'a': TagTy(),
        }
    )
    _test_src = ('\\foo[This is a tag, which is used for detailing story '
                 'contents, characters, etc.]')
    _exp_error = 'Parameters of type Tag may not include commas'

class TestSigValTextAlias(_ATestSigValFail):
    """Parameters of type PureText may not contain non-text fragments, e.g.
    aliases."""
    _signature = Signature(
        std_only={
            'a': PureTextTy(),
        }
    )
    _test_src = '\\foo[This is @text]'
    _exp_error = ('Parameters of type PureText only accept text fragments '
                  'and commands with a return type of Text (or one of its '
                  'subtypes)')

# TODO Add a test that ensures PureText does not accept commands with a
#  Text-derived return type either

class TestSigValWordOneExtra(_ATestSigValFail):
    """Parameters of type Word should reject two words."""
    _signature = Signature(
        std_only={
            'a': WordTy(),
        }
    )
    _test_src = '\\foo[two words]'
    _exp_error = ("Parameters of type Word only accept single words - 'words' "
                  "is extraneous")

class TestSigValWordTwoExtra(TestSigValWordOneExtra):
    """Parameters of type Word should reject three words."""
    _test_src = '\\foo[three words here]'
    _exp_error = ("Parameters of type Word only accept single words - 'words' "
                  "and 'here' are extraneous")

# Compact representation tests begin here
class _ATestSigCR:
    """Base class for compact representation tests."""
    _signature: Signature
    _exp_repr: str

    def test_sig_compact_repr(self):
        """Asserts that the compact representation returned by compact()
        matches the expected one."""
        self._signature.init_default_values()
        assert self._signature.compact() == self._exp_repr

class TestSigCRNoArgs(_ATestSigCR):
    """A simple signature with no parameter and None as return type."""
    _signature = Signature()
    _exp_repr = '| -> None'

class TestSigCREx1(_ATestSigCR):
    """The first example from the original GitHub issue for creating
    signatures (#19), updated to match the final syntax."""
    _signature = Signature(
        either_or={
            'key': WordTy(),
            'val': AnyTy(),
        },
    )
    _exp_repr = '\n'.join([
        '[',
        '    key: Word;',
        '    val: Any;',
        '] -> None',
    ])

class TestSigCREx2(_ATestSigCR):
    """The second example from the original GitHub issue for creating
    signatures (#19), updated to match the final syntax."""
    _signature = Signature(
        std_only={
            'ty': HeaderKindTy(),
        },
        varargs=Varargs(VARARGS_EITHER_OR, AnyTy()),
    )
    _exp_repr = '\n'.join([
        '[',
        '    ~ ty: HeaderKind;',
        '    Any*;',
        '] -> None',
    ])

class TestSigCREx3(_ATestSigCR):
    """The third example from the original GitHub issue for creating
    signatures (#19), updated to match the final syntax."""
    _signature = Signature(
        varargs=Varargs(VARARGS_STD, IntTy()),
        ret_ty=IntTy(),
    )
    _exp_repr = '\n'.join([
        '[',
        '    ~ Int*;',
        '] -> Int',
    ])

class TestSigCREx4(_ATestSigCR):
    """The fourth example from the original GitHub issue for creating
    signatures (#19), updated to match the final syntax. Doubles as a stress
    test since it uses every compact representation feature."""
    _signature = Signature(
        std_only={
            'a1': IntTy(),
            'a2': WordTy(),
            'a3': Default(TextTy(), 'bla bla bla'),
        },
        either_or={
            'b1': Default(IntTy(), '0'),
            'b2': Default(WordTy(), 'foo'),
            'b3': Default(PureTextTy(), 'two words'),
        },
        kwd_only={
            'c1': Default(FloatTy(), '3.14'),
            'c2': Default(WordTy(), 'onetwothree'),
            'c3': Default(PureTextTy(), 'bar qux'),
        },
        varargs=Varargs(VARARGS_KWD, TextTy()),
        ret_ty=TextTy(),
    )
    _exp_repr = '\n'.join([
        '[',
        '    ~ a1: Int;',
        '    ~ a2: Word;',
        '    ~ a3: Text = bla bla bla;',
        '    b1: Int = 0;',
        '    b2: Word = foo;',
        '    b3: PureText = two words;',
        '    $ c1: Float = 3.14;',
        '    $ c2: Word = onetwothree;',
        '    $ c3: PureText = bar qux;',
        '    $ Text*;',
        '] -> Text',
    ])
