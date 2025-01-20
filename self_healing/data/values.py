class font:
    red         =  "\x1b[91m"
    green       =  "\x1b[92m"
    yellow      =  "\x1b[93m"
    blue        =  "\x1b[94m"
    white       =  "\x1b[97m"
    normal      =  "\x1b[0m"
    bold        =  "\x1b[1m"

error = f"{font.red}error{font.white}({font.red}s{font.white})"
found = f"{font.yellow}found"
issue = f"{font.red}issue"
issue_not_found = f"{font.yellow}no {issue} {found}{font.white}. do you have {error}?"
want_run_code = f"{font.white}would you like to {font.green}run{font.yellow} code {font.white}to {font.red}get {error}?"

def reset_font():
    print(f"{font.white}", end="")