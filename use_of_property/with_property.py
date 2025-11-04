from collections.abc import Iterable


class AboutMe:
    """Introduction of Dustin Baek."""

    def __init__(self):
        self.__company: str = "Deloitte"
        self.__position: str = "Machine Learning Engineer"
        self._workspace: dict[str, str] = {
            "company": self.__company,
            "position": self.__position,
        }
        self.__interested_positions: set[str] = {
            "Software Engineer",
            "Data Engineer",
            "Machine Learning Engineer",
            "Python Developer",
        }
        self._programming: list[str] = ["Python", "SQL", "Bash"]

    def __repr__(self):
        """Show who I am."""
        return f"Hi! I'm Dustin working as {self._workspace.get("position")}" +\
               f"at {self._workspace.get("company")}."

    @property
    def workspace(self) -> list[str, str]:
        """Get workspace details."""
        return self._workspace

    @workspace.setter
    def workspace(self, value: Iterable[bool, str, str]):
        """Update workspace details if conditions met."""
        try:
            career_growth, new_company, new_role = value
        except ValueError as e:
            raise ValueError(
                "To set workspace you need to pass in iterable of three elements."
            ) from e
        else:
            if career_growth and new_role in self.__interested_positions:
                self._workspace["company"] = new_company
                self._workspace["position"] = new_role
            elif career_growth and new_role not in self.__interested_positions:
                raise ValueError(
                    "I want to become better "
                    + " or ".join(s for s in self.__interested_positions)
                )
            else:
                raise ValueError("Sorry maybe not position suitable for me.")

    @property
    def programming(self) -> list[str]:
        """Get current programming skils."""
        return self._programming

    @programming.setter
    def programming(self, language: str):
        """Willing to learn any language!"""
        if isinstance(language, str):
            self._programming.append(language)

    @property
    def education(self) -> str:
        """No setter since it wouldn't change."""
        degree: str = "MEng Information and Computer Engineering"
        where: str = "University of Cambridge"
        when: str = "10.2018 - 06.2022"
        return " | ".join([degree, where, when])

    @property
    def location(self) -> tuple[float, float]:
        """I prefer to work in london for now."""
        return 51.493879, -0.218356


if __name__ == "__main__":
    person = AboutMe()
    print(person)
    print(person.workspace, end="\n\n")

    person.workspace = [True, "Maniyar", "Python Developer"]
    print(person)
    print(person.workspace)

    person.programming = "Java"
    print(person.programming)

    print(person._AboutMe__company)