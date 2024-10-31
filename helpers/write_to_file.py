import json
from yaspin import yaspin


def write_to_file(filename: str, data):
    with yaspin(text="", color="yellow") as spinner:
        with open(filename, "w", encoding="utf-8") as f:
            try:
                json.dump(data, f, ensure_ascii=False, indent=4)
            except TypeError:
                spinner.fail(f"Error writing file.")
                return -1
            else:
                spinner.ok(f"💾 The file {filename} was successfully written")
                return 0

