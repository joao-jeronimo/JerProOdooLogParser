import pprint

def pretty_digest2string(the_digest):
    pypp = pprint.PrettyPrinter(indent=4)
    return pypp.pformat(the_digest)
