"""Quite popular OOP interview question."""
import logging
import random


logging.basicConfig(level=logging.INFO)

class WeightedRandomItem:
    """Define a class that has two different methods.

    1. keeps track of each incoming items
    2. depending on how many items, return each item by its probability.
    
    *** Additional Condition ***
    What if keep_track method is called 1k times, but return_item is called 1 million times?
    """
    def __init__(self):
        self.tracker : dict = {}
        self.norm_tracker: dict = {}
        
    def keep_track(self, item: str):
        """Keep track of tracker with incoming items.
        
        E.g.
        input items: 
        apple
        banana
        apple
        orange
        
        {
            apple: 2,
            banana: 1,
            orange: 1,
        }
        
        """
        self.tracker[item] = self.tracker.get(item, 0) + 1
        
        total_items = sum(v for v in self.tracker.values())
        upper_bound = 0.0
        for k, v in self.tracker.items():
            norm_val = v / total_items
            upper_bound += norm_val
            self.norm_tracker[k] = upper_bound
            

    def return_item(self):
        """Return each item proportional to its value.
        
        val = random.random() e.g. 0.8
        
        apple: 0 ~ 0.5
        banana: 0.5 ~ 0.75
        orange: 0.75 ~ 1
        """        
        random_val = random.random()
        logging.info(f"Random uniform value is {random_val}")
        for k, v in self.norm_tracker.items():
            logging.info(f"{k} has {v} as upper bound.")
            if random_val <= v:
                return k
                
        
if __name__ == "__main__":
    asdf = WeightedRandomItem()
    asdf.keep_track("apple")
    asdf.keep_track("apple")
    asdf.keep_track("banana")
    asdf.keep_track("orange")
    
    logging.info(asdf.tracker)
    logging.info(asdf.norm_tracker)
    
    logging.info(asdf.return_item())