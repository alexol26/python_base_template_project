"""Work with cli arguments

Functions:
    get_args() - return cli arguments
    is_valid_cli_args() - check to valid. Return boolean !!!Edit this func!!!

Docs about argparse: https://docs.python.org/3/library/argparse.html
"""

import argparse


# --------------------------------------------------
def get_args() -> dict:
    """Get command-line arguments

    Returns:
        dict:

    Example:
        ret['sorted']
    """
    description = "Python Base Template Project"
    parser = argparse.ArgumentParser(description=description)

    # parser.add_argument("item", metavar="str", nargs="+", help="Item(s) to bring")

    parser.add_argument(
        "-f", "--flag", action="store_true", help="Work as boolean flag"
    )
    args = vars(parser.parse_args())

    return args if is_valid_cli_args(args) else False
    # if is_valid_cli_args(args):
    #     return args


# --------------------------------------------------
def is_valid_cli_args(args: list) -> bool:
    """Check is args valid.
    Function is template. You have to write your own logic.

    Args:
        args (list): _description_

    Returns:
        bool: Returns True if args valid.
    """
    return True
