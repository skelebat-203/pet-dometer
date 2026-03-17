'''Pet state, status, etc.'''
from typing import Annotated

class Pet:
    MOOD_LIST = ["mad", "upset", "fine", "happy", "excited"]
    MAX_PROGRESS_CHANGE: Annotated[float, "Max up / down progress change"] = 0.10
    UNITS_PER_RANK = 200
    CUSHION: Annotated[float, "Smooths out progress we add a 'Cushion' whne you move up/down a rank"] = 0.05
    PET_STARTING_PROGRESS: Annotated[int, "When a new pet instance is created set progress to 0"] = 0
    #
    #  Consider adding a modifier for each mood level
    #
    def __init__(self):
        self.resource: Annotated[int, "used to note how many resources the pet has received today"] = 0
        self.mood_index: Annotated[int, "this is how the pet feels about you"] = 2
        self.progress: Annotated[int, "his notes the progress to the next mood level, updates contuniously"] = Pet.PET_STARTING_PROGRESS 
        self.resources_received_today: Annotated[int, "logs resources received today; resets each day"] = 0
    

    def test_output(self, change:int):
        print(f"{change} resources")
        print(f"Mood Index: \n Original: {temp_mood_index}\tNew: {pet.mood_index} '{pet.get_current_mood()}'")
        print(f"Progress: \n Original: {temp_progresss}\tNew: {pet.progress}")
        print(f"Current resources: \n Original: {temp_resources}\tNew: {pet.resource}")
        print(f"Resources today: \n Original: {temp_resources_received_today}\tNew: {pet.resources_received_today}")

    # Getters
    def get_current_mood(self):
        '''get pet mood'''
        return self.MOOD_LIST[self.mood_index]
    def get_progress(self):
        '''get progress to new mood'''
        return self.progress
    def get_resources_received_today(self):
        '''get current resources added today'''
        return self.get_resources_received_today

    # Setters
    def set_mood(self, mood:int):
        self.mood_index = mood
    def set_progress(self, progress:int):
        self.progress = progress
    def set_resources_received_today(self, resources_received_today:int):
        self.resources_received_today = resources_received_today
    def set_resource(self, resource:int):
        self.resource = resource

    #hooks
    def new_day(self):
        '''Reset `resources_received_today` to 0
        
        Called by file that tracks date/time.'''
        self.resources_received_today = 0

    #Other Methods
    def add_resources(self, n_resources:int):
        '''Add resources to pet. Updates values:
            - resources_received_today
            - resource
            - mood_index
            - progress
        '''
        self.set_resources_received_today(self.resources_received_today + n_resources)
        self.set_resource(self.resource + n_resources)

        temp_prog = self.get_progress() + n_resources
        
        if (n_resources + self.resource) > self.UNITS_PER_RANK: # increase mood / update progress
            self.set_mood(self.mood_index + 1)
            
            # Update progress
            if temp_prog % self.UNITS_PER_RANK == 0: 
                self.set_progress(int(self.UNITS_PER_RANK * self.CUSHION))
            else: self.set_progress(self.progress + n_resources - self.UNITS_PER_RANK)
            
        else:  # nomood change / update progress
            self.set_progress(self.progress + n_resources)

        print("\nADD RESOURCES")
        self.test_output(n_resources)
    
    def remove_resources(self, n_resources:int):
        '''Remove resources to pet. Updates values:
            - resources_received_today
            - resource
            - mood_index
            - progress
        '''
        self.set_resources_received_today(self.resources_received_today + n_resources)
        self.set_resource(self.resource + n_resources)

        temp_prog = self.get_progress() + n_resources
        
        if (n_resources + self.resource) < 0:  # decrease mood / update progress
            self.set_mood(self.mood_index - 1)

            # Update progress
            if temp_prog % self.UNITS_PER_RANK == 0: 
                self.set_progress(int(self.UNITS_PER_RANK * (1-self.CUSHION)))
            else: self.set_progress(self.progress + n_resources + self.UNITS_PER_RANK)
            
        else:  # nomood change / update progress
            self.set_progress(self.progress + n_resources)

        print("\nREMOVE RESOURCES")
        self.test_output(n_resources)


pet = Pet()

# test logic
temp_mood_index = pet.mood_index
temp_progresss = pet.progress
temp_resources = pet.resource
temp_resources_received_today = pet.resources_received_today

add = 140
# pet.add_resources(add)
remove = -90
pet.remove_resources(remove)

