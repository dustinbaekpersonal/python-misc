from pprint import pprint


nested_dict = {
    "username": "DustinBaek",
    "info": {
        "first": "Dustin",
        "last": "Baek",
        "address": {
            "postcode": "W6 7JF",
            "foo": "bar"
        }
    },
}

def flatten_json(my_dict: dict, existing_dict: dict):
    for k, v in my_dict.items():
        if not isinstance(v, dict):
            existing_dict[k] = v
        else:
            flatten_json(v, existing_dict)
    return existing_dict

res = flatten_json(nested_dict, {})

print(res)

