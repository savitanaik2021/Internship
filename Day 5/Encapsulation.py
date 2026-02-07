
class InstagramAccount:
    def __init__(self, account_name, password):
        # Public variable
        self.account_name = account_name

        # Protected variable
        self._private_reels = []

        # Private variable
        self.__archived_reels = []

        # Private password
        self.__password = password

    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)
        print("Private reel added:", reel_name)

    def display_private_reels(self, is_follower):
        if is_follower:
            print("Private Reels:", self._private_reels)
        else:
            print("Access Denied! Only followers can view private reels")

    def add_archived_reel(self, reel_name):
        self.__archived_reels.append(reel_name)
        print("Archived reel added:", reel_name)

    def display_archived_reels(self, password):
        if password == self.__password:
            print("Archived Reels:", self.__archived_reels)
        else:
            print("Access Denied! Only account holder can view archived reels")

    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels
        else:
            return "Wrong password! Access denied"

    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password updated successfully")
        else:
            print("Wrong old password")

insta = InstagramAccount("savita_naik", "1234")

insta.add_private_reel("dance Reel")
insta.add_private_reel("Food Reel")

insta.add_archived_reel("Old Dance Reel")
insta.add_archived_reel("College Memories")

print()

insta.display_private_reels(True)     
insta.display_private_reels(False)    

print()

insta.display_archived_reels("1234")  
insta.display_archived_reels("0000")  
print()

insta.set_password("1234", "5678")
insta.display_archived_reels("5678")
