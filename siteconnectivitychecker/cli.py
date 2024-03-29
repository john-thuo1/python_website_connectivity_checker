import argparse
def read_user_cli_args():
    """handle the cli arguments and options"""
    parser = argparse.ArgumentParser(
        prog="SiteConnectivityChecker",
        description = "Check if websites are online")

    
    parser.add_argument(
        "-u",
        '--urls',
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="enter one or more website URLs",


    )
    parser.add_argument(
        "-f",
        "--inout-file",
        metavar="FILE",
        type=str,
        default="",
        help="read URLs from a file",
    )


    return parser.parse_args()

def display_check_result(result, url, error=""):
    """Display the result of a connectivity check. """
    print(f'The status of "{url}" is:', end=" ")
    if result:
        print('"Online!"👍👍')
    else:
        print(f'"Offline?"✌️ \n Error: {error}"')