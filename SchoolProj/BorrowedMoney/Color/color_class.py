from colorama.ansi import AnsiFore
from colorama import just_fix_windows_console


class color(AnsiFore):


    def __init__(self) -> None:
        just_fix_windows_console()

    def color(color_name, text):
        return f"\033[{color_name}m\033[1m{text}\033[0m"

if __name__ == "__main__":
    print(color.color(color.LIGHTBLACK_EX, "hello"))