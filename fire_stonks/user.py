############### TEST WAVE 1 (5 tests) PASSED #### #CORRECT
############### TEST WAVE 3 (4 tests) PASSED #### #CORRECT
############### TEST WAVE 4 (5 tests) PASSED #### #CORRECT

### test 1.1 PASSED ### test 1.2 PASSED ### #U
### test 4.1 PASSED ### #C
### NEW add username ###
class User:
    def __init__(self, stonk_picks = None, influence_count = 0): # NEW add username
        if stonk_picks == None:
            self.stonk_picks = []
        else:
            self.stonk_picks = stonk_picks
        self.influence_count = int(0)
        # self.username = username ### NEW write test for username and how it interacts with Duediligence class/subclasses

### test 1.3 PASSED ### #U
    def add(self, stonk):
        self.stonk_picks.append(stonk)
        return stonk

### test 1.4 PASSED ### test 1.5 PASSED ### #U
    def remove(self, bad_stonk):
        if self.stonk_picks == []:
            return None
        elif bad_stonk not in self.stonk_picks:
            return False
        else:
            for remove_stonk in self.stonk_picks:
                if bad_stonk == remove_stonk:
                    self.stonk_picks.remove(remove_stonk)
                    return remove_stonk

### test 3.2 PASSED ### 3.3 PASSED ### 3.4 PASSED ### #U
### test 4.3 PASSED ### test 4.4 PASSED ### #C
    def copy_stonk(self, influencer, nice_stonk):
        if nice_stonk not in influencer.stonk_picks:
            return False
        else:
            if self.stonk_picks == []:
                self.stonk_picks.append(nice_stonk)
                influencer.influence_count += 1 ### test 4.3 ###
                nice_stonk.copy_count += 1 ### test 4.4 ###                
                return True
            else:
                for compare_stonk in self.stonk_picks:
                    if nice_stonk.ticker not in compare_stonk.ticker:
                        self.stonk_picks.append(nice_stonk)
                        influencer.influence_count += 1 ### test 4.3 ###
                        nice_stonk.copy_count += 1 ### test 4.4 ###                
                        return True
                    else:

                        for stonk_update in self.stonk_picks:
                            if stonk_update.ticker == nice_stonk.ticker:
                                self.add_dd(influencer, nice_stonk) ### test 4.5 ###    
                                influencer.influence_count += 1 ### test 4.3 ###
                                nice_stonk.copy_count += 1 ### test 4.4 ###
                                return True        


### test 4.5 PASSED ###   
    def add_dd(self, influencer, nice_stonk):
        """ 
        helper function that adds unique research from another users stonk pick
        to the primary user's stonk research
        """
        if self.stonk_picks == []:
                return None
        else:
            for stonk_to_update in self.stonk_picks:
                if nice_stonk.ticker != stonk_to_update.ticker:
                    self.stonk_picks.append(nice_stonk)

                elif nice_stonk.ticker == stonk_to_update.ticker:
                    update_dd = stonk_to_update.research    
                    
                    for compare in update_dd:
                        for nice_dd in nice_stonk.research:
                            print(f"nice_dd.resource : {nice_dd.resource}")
                            print(f"compare.resource list? : {compare.resource}")
                            if nice_dd.resource != compare.resource:
                                update_dd.append(nice_dd)
                return stonk_to_update

