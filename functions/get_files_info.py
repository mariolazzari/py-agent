import os


def get_files_info(working_directory, directory="."):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_target_dir = os.path.abspath(os.path.join(working_directory, directory))

        if not abs_target_dir.startswith(abs_working_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(abs_target_dir):
            return f'Error: "{directory}" is not a directory'

        entries = os.listdir(abs_target_dir)
        result = []

        for entry in entries:
            entry_path = os.path.join(abs_target_dir, entry)
            is_dir = os.path.isdir(entry_path)
            size = os.path.getsize(entry_path)

            result.append(f"- {entry}: file_size={size} bytes, is_dir={is_dir}")

        return "\n".join(result)

    except Exception as e:
        return f"Error: {e}"


schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": (
            "Lists files in a specified directory relative to the working "
            "directory, providing file size and directory status"
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": (
                        "Directory path to list files from, relative to the "
                        "working directory (default is the working directory itself)"
                    ),
                },
            },
        },
    },
}
