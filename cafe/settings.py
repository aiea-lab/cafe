generate_feedback_enabled = True
_generate_feedback_called = False

def set_generate_feedback_enabled(value):
    if not isinstance(value, bool):
        raise ValueError(f"Expected value to be a bool, found '{type(value)}'.")

    global generate_feedback_enabled
    generate_feedback_enabled = value

def is_generate_feedback_enabled():
    return generate_feedback_enabled

def set_generate_feedback_called(value):
    if not isinstance(value, bool):
        raise ValueError(f"Expected value to be a bool, found '{type(value)}'.")

    global _generate_feedback_called
    _generate_feedback_called = value

def is_generate_feedback_called():
    return _generate_feedback_called
