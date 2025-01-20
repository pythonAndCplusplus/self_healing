error_fixes = {
    "ArithmeticError"      : "Check mathematical operations for invalid calculations.",
    "AssertionError"       : "Verify that all assert statements use conditions that evaluate to True.",
    "AttributeError"       : "Ensure the object has the attribute you are trying to access.",
    "BufferError"          : "Handle buffer-related operations carefully; check for capacity or API misuse.",
    "EOFError"             : "Ensure input operations do not exceed available data or handle EOF properly.",
    "Exception"            : "General base class for exceptions; handle specific subclasses for better clarity.",
    "FileExistsError"      : "Check if the file already exists before creating it.",
    "FileNotFoundError"    : "Ensure the file path exists and is spelled correctly.",
    "FloatingPointError"   : "Avoid invalid floating-point operations; use appropriate precision settings.",
    "GeneratorExit"        : "Avoid yielding after a generator is closed.",
    "ImportError"          : "Ensure the module exists and is installed correctly.",
    "ModuleNotFoundError"  : "Check the spelling and installation of the module.",
    "IndentationError"     : "Ensure consistent and proper indentation in your code.",
    "IndexError"           : "Check that indices are within the range of the list, tuple, or sequence.",
    "KeyError"             : "Verify that the key exists in the dictionary before accessing it.",
    "KeyboardInterrupt"    : "Handle user interruptions gracefully, typically with a try-except block.",
    "LookupError"          : "Handle subclass-specific errors like IndexError or KeyError properly.",
    "MemoryError"          : "Optimize memory usage or allocate more resources.",
    "NameError"            : "Ensure all variables and functions are defined before use.",
    "NotADirectoryError"   : "Ensure the path you are working with is a directory.",
    "NotImplementedError"  : "Implement missing abstract methods or functionality.",
    "OSError"              : "Check operating system operations for file or directory issues.",
    "OverflowError"        : "Use smaller numbers or check for overflows in mathematical operations.",
    "PermissionError"      : "Verify you have the necessary permissions to access a resource.",
    "ProcessLookupError"   : "Ensure the process ID exists before referencing it.",
    "RecursionError"       : "Avoid excessive recursion by using iteration or increasing the recursion limit.",
    "ReferenceError"       : "Ensure objects referenced by weak references still exist.",
    "RuntimeError"         : "Review the program logic for unexpected runtime issues.",
    "StopAsyncIteration"   : "Ensure proper termination of asynchronous iterators.",
    "StopIteration"        : "Check for termination conditions in iterators.",
    "SyntaxError"          : "Fix syntax issues in your code (e.g., missing colons or parentheses).",
    "TabError"             : "Use either spaces or tabs consistently, not both.",
    "SystemError"          : "Fix internal Python interpreter issues or update Python.",
    "SystemExit"           : "Gracefully handle program exits when using sys.exit().",
    "TimeoutError"         : "Increase the timeout duration or handle slow operations.",
    "TypeError"            : "Ensure operations involve compatible data types.",
    "UnboundLocalError"    : "Define variables before using them inside functions.",
    "UnicodeError"         : "Handle encoding or decoding issues properly.",
    "UnicodeDecodeError"   : "Use the correct encoding for decoding.",
    "UnicodeEncodeError"   : "Use the correct encoding for encoding strings.",
    "UnicodeTranslateError": "Handle invalid characters during translation properly.",
    "ValueError"           : "Ensure values passed to functions or operations are valid.",
    "ZeroDivisionError"    : "Avoid dividing numbers by zero."
}

detailed_error_fixes = {
    "ArithmeticError": """
Check mathematical operations for invalid calculations:
- Verify that division or modulus operations do not involve division by zero.
- Ensure that calculations with large numbers are within the range of valid values.
- Handle special cases in mathematical functions (e.g., square roots of negative numbers).
- Use exception handling to catch and process errors gracefully.
""",

    "AssertionError": """
Verify that all assert statements use conditions that evaluate to True:
- Review the logic of the condition in the assert statement.
- Make sure the inputs meet the assumptions required for the assertion.
- Provide helpful error messages in the assertion for debugging.
- Replace assertions with proper error handling in production code if needed.
""",

    "AttributeError": """
Ensure the object has the attribute you are trying to access:
- Check the spelling of the attribute name.
- Confirm that the object is of the correct type.
- Use hasattr() to verify the existence of an attribute before accessing it.
- Review the object's initialization to ensure all expected attributes are set.
""",

    "BufferError": """
Handle buffer-related operations carefully:
- Check if the buffer size is sufficient for the operation.
- Avoid exceeding buffer capacity during data reads or writes.
- Use appropriate APIs for buffer management in multithreaded environments.
- Handle partial reads or writes gracefully.
""",

    "EOFError": """
Ensure input operations do not exceed available data:
- Validate input data sources before performing read operations.
- Check for EOF conditions explicitly in file or stream handling loops.
- Provide fallback or default values when reaching the end of input.
- Use try-except blocks to handle EOFError gracefully.
""",

    "Exception": """
Handle exceptions effectively:
- Use specific exception subclasses to address known issues.
- Log unexpected exceptions to diagnose and fix problems.
- Avoid overly broad except clauses (e.g., 'except:') unless necessary.
- Provide helpful error messages or recovery mechanisms for users.
""",

    "FileExistsError": """
Check if the file already exists before creating it:
- Use os.path.exists() or pathlib.Path.exists() to verify existence.
- Open files in appropriate modes (e.g., 'x' mode to create only if absent).
- Provide a unique filename or backup existing files if overwriting is needed.
- Use exception handling to notify the user of the conflict.
""",

    "FileNotFoundError": """
Ensure the file path exists and is spelled correctly:
- Verify the correctness of the file path and its case sensitivity.
- Check that the file resides in the expected directory.
- Use os.path.exists() to verify file existence before accessing it.
- Inform the user about missing files and provide clear recovery steps.
""",

    "FloatingPointError": """
Avoid invalid floating-point operations:
- Set up error handling using numpy or similar libraries for precision operations.
- Avoid calculations that result in NaN or infinity by validating inputs.
- Check for numerical stability in algorithms that rely on floating-point math.
- Use decimal.Decimal for high-precision calculations.
""",

    "GeneratorExit": """
Avoid yielding after a generator is closed:
- Ensure that all pending operations are completed before returning from a generator.
- Use finally blocks within generators to handle cleanup properly.
- Avoid explicit calls to .close() unless necessary.
- Design generators to handle closure gracefully.
""",

    "ImportError": """
Ensure the module exists and is installed correctly:
- Verify that the module is installed using pip or another package manager.
- Check the module's name for spelling errors.
- Review PYTHONPATH and system paths to ensure they include the module's location.
- Ensure compatibility between Python versions and the module.
""",

    "ModuleNotFoundError": """
Check the spelling and installation of the module:
- Use pip show <module_name> to verify installation.
- Confirm that the module is compatible with your Python version.
- Add the module's location to PYTHONPATH if necessary.
- Reinstall the module if it appears to be corrupted or missing.
""",

    "IndentationError": """
Ensure consistent and proper indentation:
- Use spaces or tabs consistently across your codebase.
- Configure your editor to display and enforce consistent indentation.
- Check for accidental mix of spaces and tabs using tools like pylint.
- Fix block structures to align with Python's indentation rules.
""",

    "IndexError": """
Avoid accessing elements outside the bounds of a list or sequence:
- Check the length of the sequence before accessing elements.
- Use len() to determine the valid range of indices.
- Handle empty sequences gracefully by verifying their size.
- Implement try-except blocks to catch and resolve IndexError.
""",

    "KeyError": """
Avoid accessing nonexistent keys in a dictionary:
- Use the get() method to retrieve values with a default if the key is absent.
- Check if the key exists using the in operator before accessing it.
- Handle missing keys by providing fallback logic in your code.
- Ensure dictionary keys are correctly initialized and updated as needed.
""",

    "KeyboardInterrupt": """
Handle user-initiated interruptions gracefully:
- Wrap main loops or operations in try-except blocks to catch KeyboardInterrupt.
- Provide a clear and friendly message when the program is interrupted.
- Save any progress or data before exiting if necessary.
- Use signal handling to manage interruptions more flexibly if required.
""",

    "LookupError": """
Handle invalid lookups in dictionaries, lists, or other sequences:
- Verify that the key or index exists before performing the lookup.
- Use try-except blocks to catch and handle lookup errors.
- Provide informative messages or fallback options for missing data.
- Use get() methods or similar safe access mechanisms for lookups.
""",

    "MemoryError": """
Avoid excessive memory usage in your program:
- Optimize data structures and algorithms to reduce memory consumption.
- Process large datasets in chunks or streams instead of loading them entirely into memory.
- Monitor memory usage using tools like tracemalloc or resource modules.
- Upgrade hardware or increase memory limits if required for large workloads.
""",

    "NameError": """
Ensure all variables are defined before using them:
- Check the spelling of variable and function names.
- Verify that variables are initialized properly before referencing them.
- Use global or nonlocal declarations for variables used across scopes.
- Review the program's flow to identify potential scoping issues.
""",

    "NotImplementedError": """
Ensure that all abstract methods are implemented in subclasses:
- Define concrete implementations of required methods in derived classes.
- Raise NotImplementedError only for unimplemented placeholder methods.
- Use ABCs (Abstract Base Classes) to enforce implementation contracts.
- Document unimplemented methods and provide guidance for future implementation.
""",

    "OSError": """
Handle operating system-level errors carefully:
- Check file paths, permissions, and availability of required resources.
- Use try-except blocks to catch and process OSError.
- Review system logs or error codes for detailed diagnostics.
- Provide fallback mechanisms or recovery options for critical operations.
""",

    "OverflowError": """
Avoid calculations that exceed numeric limits:
- Use libraries like decimal or numpy for handling large numbers safely.
- Check inputs to ensure they fall within valid ranges for operations.
- Consider using alternative algorithms or data representations for high-precision calculations.
- Handle exceptions and provide informative messages when overflow occurs.
""",

    "RecursionError": """
Prevent excessive recursion depth:
- Use iterative solutions instead of recursion for deep or complex problems.
- Set recursion limits using sys.setrecursionlimit() cautiously.
- Debug and fix logical errors causing unbounded recursion.
- Use memoization or caching techniques to optimize recursive algorithms.
""",

    "ReferenceError": """
Ensure that references to weakly-referenced objects remain valid:
- Avoid accessing weak references after their targets have been garbage collected.
- Use strong references for critical objects that must persist.
- Validate weak references before dereferencing them.
- Design your program to handle object lifecycle and garbage collection effectively.
""",

    "RuntimeError": """
Identify and resolve unexpected runtime issues:
- Analyze stack traces and error messages for clues about the root cause.
- Use logging to capture context and state information during failures.
- Test your code thoroughly to identify edge cases and timing issues.
- Implement error handling for known runtime scenarios to improve robustness.
""",

    "StopIteration": """
Handle end-of-iteration scenarios correctly:
- Ensure generators or iterators provide expected sequences of values.
- Avoid manually raising StopIteration within generator functions.
- Use for-loops or other iteration constructs to handle sequences automatically.
- Catch StopIteration explicitly when iterating over custom objects.
""",

    "SyntaxError": """
Correct syntax errors in your code:
- Review the line and surrounding context reported in the error message.
- Ensure all brackets, parentheses, and quotes are properly matched and closed.
- Avoid mixing Python syntax with syntax from other languages or versions.
- Use linters and IDEs to detect and highlight syntax issues before execution.
""",

    "SystemError": """
Address low-level issues causing system errors:
- Debug the program to identify unexpected state or interactions.
- Verify compatibility with system libraries and Python runtime versions.
- Ensure proper usage of third-party modules and their APIs.
- Report system-level errors to maintainers or support teams for resolution.
""",

    "TypeError": """
Ensure operations use compatible types:
- Check the types of inputs before performing operations or method calls.
- Use isinstance() or type() to validate and convert types as needed.
- Avoid passing incompatible arguments to functions or methods.
- Document and enforce type expectations for functions and APIs.
""",

    "UnboundLocalError": """
Avoid referencing uninitialized local variables:
- Initialize all local variables before using them in functions or loops.
- Use nonlocal or global declarations for variables shared across scopes.
- Review the program's flow to ensure variables are defined in all execution paths.
- Handle conditional cases where variables may not be assigned before use.
""",

    "ValueError": """
Handle invalid values passed to operations or functions:
- Validate input values before using them in calculations or logic.
- Use try-except blocks to catch and manage ValueError.
- Provide clear error messages or fallback options for invalid inputs.
- Test your code with a variety of valid and invalid values to ensure robustness.
""",

    "ZeroDivisionError": """
Prevent division by zero in calculations:
- Check denominators to ensure they are not zero before performing division.
- Use try-except blocks to catch and handle ZeroDivisionError.
- Provide default values or alternative calculations for zero-denominator cases.
- Implement input validation to prevent invalid calculations.
"""
}