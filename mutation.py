def mutate_string(string, position, character):
    new=string[:position]+character+string[position+1:]
    return new