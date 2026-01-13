import os

def get_files_info(working_directory, directory="."):
	working_dir_abs = os.path.abspath(working_directory)
	path = os.path.normpath(os.path.join(working_dir_abs, directory))
	if not os.path.commonpath([path, working_dir_abs]) == working_dir_abs:
		return f"Error: Cannot list {directory} as it is outside the permitted working directory"
	if not os.path.isdir(path):
                return f"Error: {directory} is not a directory"
	results = ""
	for file in os.listdir(path):
		results += f"- {file}: file_size={os.path.getsize(os.path.join(path, file))}, is_dir={os.path.isdir(os.path.join(path, file))}"
	return results
