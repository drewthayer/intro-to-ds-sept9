# FlashCard class
import time

class FlashCard:
    
    def __init__(self, 
                 front='', 
                 back=''):
        self.front = front
        self.back = back
        self.date_created = int(time.time())
        self.last_seen = int(time.time())
        self.last_success = None
        self.last_miss = None
        self.success_count = 0
        self.miss_count = 0
        self.word_bag = self.build_word_bag()
        self.learned = False

    def __repr__(self):
        return f'''
        self.front: {self.front}
        self.back: {self.back}
        self.date_created: {self.date_created}
        self.last_seen: {self.last_seen}
        self.last_success: {self.last_success}
        self.last_miss: {self.last_miss}
        self.success_count: {self.success_count}
        self.miss_count: {self.miss_count}
        self.word_bag: {self.word_bag}
        '''

    def view_front(self):
        print(self.front)
    
    def view_back(self):
        print(self.back)

    def edit_front(self, new_front):
        self.front = new_front
    
    def edit_back(self, new_back):
        self.back = new_back

    def build_word_bag(self):
        return self.front.split(' ') + self.back.split(' ')

    def success(self):
        self.success_count += 1
        self.last_seen = int(time.time())
        self.last_success = int(time.time())

    def miss(self):
        self.miss_count += 1
        self.last_seen = int(time.time())
        self.last_miss = int(time.time())


front = 'How do you get a unix timestamp in Python?'
back = 'import time\ntime.time()'
card1 = FlashCard(front, back)

print(card1)

card1.view_front()
card1.view_back()
card1.miss()

card1.edit_front('How do you get a unix timestamp in Python you n00b?')

card1.view_front()
card1.view_back()

card1.success()


print(card1)