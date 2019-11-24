input = ["+3E", "+1A", "-1A", "+4F", "+1A", "-3E", "+3E"]
room_booking_cnt={}

for action in input:
	if action[0] == "-":
		continue
	#el = el.replace("+", "")
	room = action[1:]
	if room not in room_booking_cnt:
		room_booking_cnt[room] = 1
	else:
		room_booking_cnt[room] += 1

counter =0
room_max_book =""

#for el in sorted(room_booking_cnt.keys()): --> This was n*log(n) complexity. modified.
for room in room_booking_cnt.keys():
	if room_booking_cnt[room] >= counter:
		room_max_book = room if (room_booking_cnt[room] > counter or room < room_max_book) else room_max_book
		counter = room_booking_cnt[room]

print(room_max_book)
