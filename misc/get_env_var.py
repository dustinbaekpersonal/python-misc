import os

if __name__ == "__main__":
    var = os.environ.get("shared_var")

    print(var)