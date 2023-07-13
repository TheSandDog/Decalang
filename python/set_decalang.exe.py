import os
import winreg

def set_default_program(file_extension, program_path):
    # Open the "HKEY_CLASSES_ROOT" key in the registry
    with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, '', 0, winreg.KEY_SET_VALUE) as hkcr_key:
        # Create a new key for the file extension
        with winreg.CreateKey(hkcr_key, file_extension) as ext_key:
            # Set the default value of the extension key to the program description
            winreg.SetValue(ext_key, None, winreg.REG_SZ, program_path)

        # Create a new key for the program file type
        with winreg.CreateKey(hkcr_key, program_path) as prog_key:
            # Create a subkey for the "shell" key
            with winreg.CreateKey(prog_key, 'shell') as shell_key:
                # Create a subkey for the "open" key
                with winreg.CreateKey(shell_key, 'open') as open_key:
                    # Create a subkey for the "command" key
                    with winreg.CreateKey(open_key, 'command') as command_key:
                        # Set the default value of the command key to the program executable path
                        winreg.SetValue(command_key, None, winreg.REG_SZ, f'"{program_path}" "%1"')

def find_decalang_exe(directory):
    for root, dirs, files in os.walk(directory):
        if "decalang.exe" in files:
            return os.path.join(root, "decalang.exe")
    return None

# Set the file extension and program path
file_extension = '.dl'
program_name = 'decalang.exe'

# Find the location of the "decalang.exe" file
decalang_exe_path = find_decalang_exe(os.path.abspath(os.sep))

if decalang_exe_path:
    print(f"Found decalang.exe at: {decalang_exe_path}")

    # Set the default program for the file extension
    set_default_program(file_extension, program_name)
    set_default_program(".deca", program_name)
    set_default_program(".decalang", program_name)
    print(f"Set {file_extension} to open with {program_name}.")
else:
    print("decalang.exe not found.")
