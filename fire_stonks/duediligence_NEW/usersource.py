############### NEW ###############
from fire_stonks.duediligence import DueDiligence

### NEW ###
# Has an attribute category that is "User Source"
class UserSource(DueDiligence):
    def __init__(self, username): ### NEW need to write/connect to test for username
        super().__init__("User Source")
        self.username = username ### NEW need to write/connect to test for username
    def __str__(self):
        return "The content was created by a firestonks user."
        ### NEW need to include a specified {username} credit in the string ###
#stringify method returns "The content was created by a firestonks user."

### NEW - ensure the resource maintains the correct connection ...
# ...to the original {username} who created the content ** even if copied by another user.
#
