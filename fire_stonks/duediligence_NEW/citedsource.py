############### NEW ###############
from fire_stonks.duediligence import DueDiligence

### NEW ###
# Has an attribute category that is "Cited Source"
class CitedSource(DueDiligence):
    def __init__(self):
        super().__init__("Cited Source")

    def __str__(self):
        return "This content was discovered through research."
# stringify method returns "This content was discovered through research."