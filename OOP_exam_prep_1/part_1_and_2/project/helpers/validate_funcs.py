def validate_location(value):
    value = value.strip()

    if len(value) != 3 or not value.isalnum():
        raise ValueError("Store location must be 3 chars long!")