from prompt_toolkit import PromptSession
from .detail import exit

def multiline_input():
    session = PromptSession(multiline=True)
    lines = []
    while True:
        try:
            line = session.prompt("")
            if line.strip().lower() in exit:
                break
            lines.append(line)
        except KeyboardInterrupt:
            return str("\n".join(lines))
        except EOFError:
            print("\nInput ended unexpectedly.")
            return ""

    return str("\n".join(lines))

def fix_console_fonts():
    from ctypes import windll as win, byref as by, c_ulong as ul
    from os import name as device

    if device == 'nt':
        windows = win.kernel32
        handle = windows.GetStdHandle(-11)
        mode = ul()
        
        # Retrieve the current console mode
        if windows.GetConsoleMode(handle, by(mode)):
            # Enable virtual terminal processing (ANSI support)
            ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
            windows.SetConsoleMode(handle, mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING)
