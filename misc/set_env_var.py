import os

if __name__ == "__main__":
    os.environ["shared_var"] = "10"
    var = os.environ.get("shared_var")

    print(var)