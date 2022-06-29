import random

class Ship:
    def __init__(self):
        self.tasks_list = ["clean", "destroy", "vote", 
        "check", "reseach", "play", "cry"]

    def give_task(self):
        selected_task = random.choice(self.tasks_list)
        return selected_task
    
    