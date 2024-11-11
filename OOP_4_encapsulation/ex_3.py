class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        is_long_enough = len(value) >= 8
        contains_upper_letter = any([el for el in value if el.isupper()])
        contains_digit = any([el for el in value if el.isdigit()])

        if not is_long_enough or not contains_upper_letter or not contains_digit:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        return (f'You have a profile with username: "{self.__username}" '
                f'and password: {"*" * len(self.__password)}')


correct_profile = Profile("Username", "Passw0rd")
correct_profile.password = "asd"
print(correct_profile)
print(correct_profile.password)
