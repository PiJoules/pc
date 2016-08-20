#-*- coding: utf-8 -*-

from utils import SlotDefinedClass


class Type(SlotDefinedClass):
    """
    Types of variables available in pc space.

    Be sure to consult http://cdecl.org/ later for c types.
    """
    __slots__ = ()


class FunctionType(Type):
    __slots__ = ("return_type", "arg_types")


class VariableType(Type):
    __slots__ = ()


class VoidType(VariableType):
    __slots__ = ()


class CharacterType(VariableType):
    __slots__ = ()


class IntegerType(VariableType):
    __slots__ = ()


class PointerType(VariableType):
    __slots__ = ("element_type", "depth")


class StringType(PointerType):
    __slots__ = ()

    """A String is a char pointer."""
    def __init__(self):
        self.element_type = CharacterType
        self.depth = 1


class VariableArgumentType(Type):
    __slots__ = ()


TYPE_TABLE = {
    "void": VoidType,
    "char": CharacterType,
    "int": IntegerType,
    "...": VariableArgumentType,
}


class Module(Type):
    __slots__ = ("name", "body")


def word_to_type(word):
    """
    Convert a Word token to a Type.

    Types start with some characters followed by optional *s for pointers.
    Exceptions are ellipsis.
    TODO: Add support for literal static arrays.
    """
    assert word

    cut = 1
    while word[:cut] not in TYPE_TABLE:
        cut += 1
        if cut > len(word):
            raise RuntimeError("No type for word '{}'".format(word))

    base, rest = word[:cut], word[cut:]
    base_type = TYPE_TABLE[base]()
    pointer_count = 0
    while rest:
        c, rest = rest[0], rest[1:]
        assert c == "*"
        pointer_count += 1
    if pointer_count:
        return PointerType(element_type=base_type, depth=pointer_count)
    else:
        return base_type

