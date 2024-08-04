def format_message(message):
    if isinstance(message,Exception):
        return "{}: {}".format(
            message.__class__.__name__, message
        )
    return message