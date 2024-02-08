How to start with Poetry:
Refer to: https://python-poetry.org/docs/

Basic commands:
`poetry new project-name`
`poetry init`
`poetry add pandas`
`poetry run python your_script.py`
`poetry run pytest`
`poetry shell`
`poetry install`

Advantage of using poetry:
1. Poetry automatically combines pip and virtualenv, so we don't need to create nor activate per project venvs.
2. Poetry will store its dependencies under home directory ${cache-dir}/virtualenvs per project, so it's globally accessible but still isolated from system installed python.
3. Poetry makes it very easy to build and publish package using `poetry build && poetry publish`.
4. By creating poetry.lock, it ensures more robust package dependency. Lesser of "It works on my machine!".
5. `poetry add` automatically updates pyproject.toml and poetry.lock

Disadvantage of using poetry:
1. It's not PEP621 compliant
2. To run python program, need to use command `poetry run python your_script.py`
3. Orelse you can activate venv `poetry shell`, but this defeats original advantage of no need for activating venv
4. Better to use alias for `poetry run python` to `poet` for instance.
5. you now have an extra build-time and / or runtime dependency you have to install on the system prior to installing your dependencies. 
For example, the stock python docker image doesn't contain poetry, so before you can bring your code in and install it you first have to install poetry in it.
6. poetry solves deps across all your dev dependencies, extras, and what have you. With too many dependencies, you can run into unresolvable dependency conflicts, especially for larger or more bloated projects.