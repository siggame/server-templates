def type_for(variable):
    if variable.type == int:
        return 'int'
    if variable.type == bool:
        return 'bool'
    if variable.type == float:
        return 'float'
    if variable.type == str:
        return 'unicode'
    return repr(variable.type.name)
