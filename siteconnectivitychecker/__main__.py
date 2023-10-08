import sys
import pathlib
from typing import List 
from siteconnectivitychecker.cli import display_check_result, read_user_cli_args
from siteconnectivitychecker.checker import site_is_online

def _get_websites_urls(user_args) -> List[str]:  
    urls = user_args.urls
    if user_args.input_file:
        urls += _read_urls_from_file(user_args.input_file)
    return urls

def _read_urls_from_file(file: str) -> List[str]:  
    file_path = pathlib.Path(file)

    if file_path.is_file():
        with file_path.open() as urls_file:
            urls = [url.strip() for url in urls_file]

            if urls:
                return urls
            else:
                print(f"Error: empty input file, {file}", file=sys.stderr)
    else:
        print("Error: input file not found", file=sys.stderr)

    return []

def _synchronous_check(urls: List[str]) -> None:  
    for url in urls:
        error = ""
        try:
            result = site_is_online(url)
        except Exception as e:
            result = False
            error = str(e)
        display_check_result(result, url, error)

def main() -> None:  
    user_args = read_user_cli_args()
    urls = _get_websites_urls(user_args)

    if not urls:
        print("Error: no URLs to check", file=sys.stderr)
        sys.exit(1)

    _synchronous_check(urls)

if __name__ == "__main__":
    main()
