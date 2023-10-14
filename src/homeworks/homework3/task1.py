def curry_explicit(function, arity):
    def args_control(saved_args):
        if len(saved_args) == arity:
            return function(*saved_args)

        def get_new_arg(new_arg):
            return args_control([*saved_args, new_arg])

        return get_new_arg

    if arity > 1:
        args_storage = []
        return args_control(args_storage)

    if arity == 0 or arity == 1:
        return function

    raise ValueError("arity must be greater than or equal to zero")


def uncurry_explicit(function, arity):
    def fake_function(*args):
        args_count = len(args)
        if args_count != arity:
            raise TypeError(
                f"curried function takes {arity} positional arguments but {args_count} were given"
            )
        arg_inserter = function
        for i in range(args_count):
            arg_inserter = arg_inserter(args[i])
        return arg_inserter

    if arity > 1:
        return fake_function

    if arity == 0 or arity == 1:
        return function

    raise ValueError("arity must be greater than or equal to zero")
