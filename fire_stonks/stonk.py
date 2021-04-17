############### TEST WAVE 2 (5 tests) PASSED #### #CORRECT
############### TEST WAVE 3 (4 tests) PASSED #### #CORRECT

############### NEW TEST TBD (? tests) ###############
# the instances/objects of the Stonk class will be components of a User class' object 
# - user objects can "have many" Stonk objects in the stonk_picks list

class Stonk:
    def __init__(self, ticker = "", research = None, copy_count = 0, prediction = None): #buy/sell dates
### test 2.1 PASSED ### #U
        self.ticker = ticker
### test 2.2 PASSED ### #U
        if research == None:
            self.research = []
        else:
            self.research = research
### test 4.2 PASSED ### #C
        self.copy_count = copy_count
### NEW --untested-- ### Likely refactor Prediction into a class
# make sure all predictions are a int --
        if prediction is None:
            self.prediction = int(0)
        else:
            self.prediction = int(prediction)

### test 2.4 PASSED ### test 2.5 PASSED ### #U
    def get_by_author(self, author):
        dd_by_author_list = []
        for dd in self.research:
            if author == dd.author: # syntax that refers to an item object by its category "str" 
                dd_by_author_list.append(dd)
        return dd_by_author_list

### test 3.1 ### stringify
    def __str__(self):
        return f"User selected {self.ticker} as a winning Stonk"
# use str() to call this method and convert item to the str^
# this method turns an item instance into the string ""

### NEW --untested-- ### Likely refactor Prediction into a class
    def prediction_description(self): 
        prediction_description = ""
        if prediction < 1 or prediction > 4:
            return None

        elif prediction == 1:
            prediction_description = "Short Play"
        elif prediction == 2:
            prediction_description = "Long Play"
        elif prediction == 3:
            prediction_description = "Short and Long Play"
        elif prediction == 4:
            prediction_description = "A complex play..."
        return str(prediction_description)

