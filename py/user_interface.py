

def strtoboolstr(val):
    """Convert a string representation of truth to true (1) or false (0).
    True values are 'y', 'yes', 't', 'true', 'on', and '1'; false values
    are 'n', 'no', 'f', 'false', 'off', and '0'.  Raises ValueError if
    'val' is anything else.
    """
    val = val.lower()
    if val in ('y', 'yes', 't', 'true', 'on', '1'):
        return str(1)
    elif val in ('n', 'no', 'f', 'false', 'off', '0'):
        return str(0)
    else:
        raise ValueError("invalid truth value %r" % (val,))

def collect_answer_str():
    """ask 3 questions and collection a str

    Parameters
    ----------
    None

    Returns
    -------
    str
    """
    root_question = "Do you care about Metacritic? "
    next_question = "Are you a big fan of game consoles such as PlayStation, Xbox and Nintendo? "
    leaf_question = "Do you prefer to be a single player? "
    ans1 = strtoboolstr(input(root_question))
    ans2 = strtoboolstr(input(next_question))
    ans3 = strtoboolstr(input(leaf_question))
    ans_str = ans1+ans2+ans3
    return ans_str



