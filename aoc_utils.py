import requests


def get_puzzle_string(day, path_to_cookie="D:\Python\AdventOfCoding\session_cookie.txt"):
    try:
        with open(path_to_cookie, "r") as f:
            c = f.read()
    except FileNotFoundError:
        print("cookie file not found")
        return ""

    cookies = {"session": c}

    req = requests.get(f"https://adventofcode.com/2023/day/{day}/input", cookies=cookies)
    # removing the last \n
    return req.text[:-1]
