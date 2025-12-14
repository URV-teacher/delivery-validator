import json
import argparse
from jsonschema import Draft7Validator


def load_schema(schema_path: str) -> dict:
    """Load the JSON schema from a file."""
    with open(schema_path, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_json_file(file_path: str, schema: dict) -> bool:
    """Validate a JSON file against the given schema."""
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    validator = Draft7Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda e: e.path)

    if errors:
        print(f"Validation failed for {file_path}:")
        for error in errors:
            print(f" - {list(error.path)}: {error.message}")
        return False
    else:
        print(f"{file_path} is valid")
        return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate delivery JSON files.")
    parser.add_argument("--schema", help="Path to the JSON schema (schema.json)")
    parser.add_argument("files", nargs="+", help="Path(s) to JSON file(s) to validate")
    args = parser.parse_args()

    schema = load_schema(args.schema)

    all_valid = True
    for file_path in args.files:
        if not validate_json_file(file_path, schema):
            all_valid = False

    if not all_valid:
        exit(1)

