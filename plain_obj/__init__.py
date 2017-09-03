from keyword import iskeyword
from collections import OrderedDict


def new_type(type_name, field_names):
    if isinstance(field_names, str):
        # names separated by whitespace and/or commas
        field_names = field_names.replace(',', ' ').split()
    check_name(type_name)
    seen_fields = set()
    for name in field_names:
        check_name(name)
        if name in seen_fields:
            raise ValueError('Encountered duplicate field name: %r' % name)
        seen_fields.add(name)
    return type(
        type_name,
        (PlainBase,),
        {
            '__slots__': field_names,
            '__init__': make_constructor(field_names)
        }
    )


class PlainBase(object):

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return all(i == j for i, j in zip(self, other))

    def __iter__(self):
        for name in self.__slots__:
            yield getattr(self, name)

    def __repr__(self):
        values = tuple(self)
        return self.__class__.__name__ + repr(values)

    def to_dict(self):
        return OrderedDict(zip(self.__slots__, self))


def make_constructor(fields):
    assignments = '\n'.join(['    self.{0} = {0}'.format(f) for f in fields])
    parameter_lists = ', '.join(fields)
    source = 'def __init__(self, %s):\n%s' % (parameter_lists, assignments)
    namespace = {}
    exec(source, None, namespace)
    return namespace['__init__']


def check_name(name):
    if not all(c.isalnum() or c == '_' for c in name):
        raise ValueError('Type names and field names can only contain alphanumeric characters and underscores: %r' % name)
    if iskeyword(name):
        raise ValueError('Type names and field names cannot be a keyword: %r' % name)
    if name[0].isdigit():
        raise ValueError('Type names and field names cannot start with a number: %r' % name)
