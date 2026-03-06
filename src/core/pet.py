'''Pet state, status, etc.'''

class Pet:
    MOOD_LIST = ["excited", "happy", "fine", "upset", "mad"]
    MAX_PROGRESS_CHANGE = 0.10 # Max up / down progress change 
    #
    #  Consider adding a modifier for each mood level
    #
    default_progress = 0
    def __init__(self):
        self.resource = 0 # used to note how many resources the pet has received today
        self.mood_index = 2 # this is how the pet feels about you
        self.progress = Pet.default_progress # this notes the progress to the next mood level, updates contuniously
        self.resources_received_today = 0 # logs resources received today; resets each day
    
    '''Getters / Setters'''
    def get_current_mood(self):
        '''get pet mood'''
        return MOOD_LIST[self.mood_index]
    def get_current_progress(self):
        '''get progress to new mood'''
        return self.progress

    def set_gift_resources(self, n_resources:int):
        '''player gift resources to pet
        return: resources
        '''
        
        self.resources_received_today = n_resources
        self.resource = self.resource + n_resources

        temp_prog = self.progress + n_resources

        if (n_resources + self.resource) > 100: 
            print("\ngo up")
            self.mood_index = self.mood_index + 1

            if temp_prog % 100 == 0: self.progress = 5
            else: self.progress = self.progress + n_resources - 100

        elif (n_resources + self.resource) < 0: 
            print("\ndrop")
            self.mood_index = self.mood_index - 1

            if temp_prog % 100 == 0: self.progress = 95
            else: self.progress = self.progress + n_resources + 100
            
        else: 
            print("\nstay")
            self.progress = self.progress + n_resources

        return self.resource, self.mood_index, self.resources_received_today

    def set_walk_resources(self, n_resource:int):
        '''Accept resources
        return: resources
        '''
        return self.resource + n_resource

    #hooks
    def new_day(self):
        self.resources_received_today = 0

pet = Pet()

# test logic
temp_mood_index = pet.mood_index
temp_progresss = pet.progress
temp_resources = pet.resource
temp_resources_received_today = pet.resources_received_today

pet.set_gift_resources(45)

print(f"-50 resources")
print(f"Mood Index: \n Original: {temp_mood_index}\tNew: {pet.mood_index}")
print(f"Progress: \n Original: {temp_progresss}\tNew: {pet.progress}")
print(f"Current resources: \n Original: {temp_resources}\tNew: {pet.resource}")
print(f"Resources today: \n Original: {temp_resources_received_today}\tNew: {pet.resources_received_today}")

pet.mood_index = temp_mood_index
pet.progress = temp_progresss
pet.resource = temp_resources
pet.resources_received_today = temp_resources_received_today