from .runner import SelfHealingRunner
from .data.values import reset_font, want_run_code, issue_not_found, found, issue, error, font
from .data.functions import fix_console_fonts, multiline_input
from .data.detail import yes
fix_console_fonts()

def get_error(code, file, line, details):
        bug = ""
        print(f"{font.white}please enter {error}{font.white}, when done, enter{font.white} '{font.red}exit{font.white}' at {font.blue}new line")
        reset_font()
        bug = multiline_input()
        if not bug:
            print(issue_not_found)
            reset_font()
            user_answer = input()
            if user_answer.lower() in yes:
                get_error(code, file, line, details)
            else:
                print(want_run_code)
                reset_font()
                user_answer = input()
                if user_answer.lower() in yes:
                    check_code(code, file, line, True)
                else:
                    print(f"{font.yellow}no {issue} {found}{font.white}.")
        else:
            debuger = SelfHealingRunner(code, bug, details)
            debuger.heal_code()

def debug_code(code="", path="", bug="", file= False, line= True):
    if not code and path:
        with open(path, "r") as file:
            code = file.read()
    elif not code and not path:
        print(f"{font.white}enter code or path, then {font.green}enter{font.white} '{font.red}exit{font.white}' at new line")
        user_answer = multiline_input()
        if user_answer == r"^[A-Z]:\\\\.+\.py":
            path = user_answer
            with open(path, "r") as file:
                code = file.read()
        else:
            code = user_answer
    details = {"file": file, "line": line}
    print(f"{font.blue}debuging started", end="\r")
    if not bug:
        print(issue_not_found)
        reset_font()
        user_answer = input()
        if user_answer.lower() in yes:
            get_error(code, file, line, details)
        else:
            print(want_run_code)
            reset_font()
            user_answer = input()
            if user_answer.lower() in yes:
                check_code(code, file, line, True)
            else:
                print(f"{font.yellow}no {issue} {found}.")
    else:
        debuger = SelfHealingRunner(code, bug, details)
        debuger.heal_code()


def check_code(code="", path="", file= False, line= True, debug=False):
    if not code and path:
        with open(path, "r") as file:
            code = file.read()
    elif not code and not path:
        print(f"{font.white}enter code or path, then {font.green}enter{font.white} '{font.red}exit{font.white}' at new line")
        user_answer = multiline_input()
        if user_answer == r'^[A-Z]:[\\, \\\\].+\.py':
            path = user_answer
            with open(path, "r") as file:
                code = file.read()
        else:
            code = str(user_answer)
    runner = SelfHealingRunner(code)
    results = runner.run()
    if results["error"]:
        print(f"{font.red}Status{font.white}:{font.yellow}{results["status"]}\n{font.red}Output{font.white}:{font.yellow}\n{results["message"]}")
        if not debug:
            print(f"{font.white}would you like help {font.white}to {font.yellow}fix {error}?")
            reset_font()
            user_answer = input()
            if user_answer.lower() in yes:
                debug_code(code=code, bug=results["message"], file=file, line=line)
        else:
            debug_code(code, results["message"], file, line)
    else:
        print(f"{font.blue}Status{font.white}:{font.green}{results["status"]}\n{font.blue}Output{font.white}:{font.green}\n{results["message"]}")
        reset_font()

