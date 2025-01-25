class UserProcessor:
    def userInfoCollect(self, name, age):
        print("Collecting user info")
        user_data = {
            "username": name,
            "user_age": age
        }
        with open("user_data.txt", "a") as f:
            f.write(f"Name: {name}, Age: {age}\n")

        if age < 18:
            print("Underage user detected.")

        return user_data