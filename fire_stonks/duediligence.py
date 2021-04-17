############### TEST WAVE 2 (5 tests) PASSED #### #CORRECT
############### TEST WAVE 3 (4 tests) PASSED #### #CORRECT

# the instances/objects of the DueDiligence class will be components of a Stonk class' object 
# - stonk objects can "have many" DueDiligence objects in their research list

### test 2.3 PASSED ### #U
class DueDiligence:
    def __init__(self, title = "", author = "", resource = ""):
        self.title = title
        self.author = author
        self.resource = resource

### test 3.1 PASSED ### stringify #U
    def __str__(self):
        return "This resource has information about a stonk pick"
# use str() to call this method and convert item to the str^
# this method turns an item instance into the string ""