import cx_Freeze

executables = [cx_Freeze.Executable("Abducted.py)"]

cx_Freeze.setup(
        name = "Abducted",
        options={"build_exe": {"packages":["pygame"],
                                                 "included_files":["Girl drawing Larger.pgn", "Character - GirlV2.png"]}},
        executables = executables
        )
