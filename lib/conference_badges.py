def badge_maker(name=''):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
   badges = []
   for name in names:
        badges.append(f'Hello, my name is {name}.')
   return badges

def assign_rooms(names):
    rooms = []
    room_no = range (1,9) 
    for room, name in zip(room_no, names):
        rooms.append(f"Hello, {name}! You'll be assigned to room {room}!")
    return rooms

def printer(names):
    badges = batch_badge_creator(names)
    for badge in badges:
        print(badge)
    room_assignments = assign_rooms(names)
    for assignment in room_assignments:
        print(assignment)



