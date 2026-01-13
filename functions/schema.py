from google import genai
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself).",
            ),
        },
    ),
)
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Returns the first 10000 lines of content of a file, as long as it is within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file you want read, relative to working directory",
            ),
        },
    ),
)
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writing to files, existing and new, potentially overwriting their contents.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file you want write or overwrite, relative to working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Entire content of the file you are writing. If you are creating a new file, this will be all the content in it. If you are writing an already existing file, this will replace the content currently in it"
            ),
        },
    ),
)
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs code from .py type files.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the python code file you wish to run, relative to working directory"
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description=(
                    "Arguments to be passed on the the code you wish to run, in the form of a array of strings."
                    "Omit this parameter or use an empty array if no arguments are needed."
		),
                items=types.Schema(type=types.Type.STRING)
            ),
        },
    ),
)
