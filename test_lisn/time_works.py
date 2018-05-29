sgons = "\nСколько разворотов в издании? "
sgons += "\nEnter '0' to end the program. "
time_works = ""
while time_works != 0:
    time_s = input(sgons)
    time_w = int(time_s) * 4
    time_works = int(time_w) / 60
    print(time_works)
