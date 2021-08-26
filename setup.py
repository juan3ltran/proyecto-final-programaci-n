import cx_Freeze

executables = [cx_Freeze.Executable("main.py",
                                     shortcut_name="Tiro parabólico",
                                     shortcut_dir="DesktopFolder")]
                                
cx_Freeze.setup(
    name="Tiro parabólico",
    options={"build_exe":{"packages":["pygame"],
                          "include_files":["images","sound"]}},
    executables = executables
    )
