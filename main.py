class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)

    print("Details of new students:")

    def change_name(self, change_name):
        self.change_name = change_name
        print("The student new name is: ", change_name)

    def change_age(self, change_age):
        self.change_age = change_age
        print("The student new age is: ", change_age)

    def add_track(self, add_track):
        self.track = add_track
        print("The student new track is: ", add_track)

    def add_score(self, add_score):
        self.score = add_score
        print("The student new score is: ", add_score)
        



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()