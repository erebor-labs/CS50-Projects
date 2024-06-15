import datetime

def main():
    get_time = input("What time is it? ")
    convertted_time = convert(get_time)
    
    if convertted_time >= 7 and convertted_time <= 8:
        print("breakfast time")
    elif convertted_time >= 12 and convertted_time <= 13:
        print("lunch time")
    elif convertted_time >= 18 and convertted_time <= 19:
        print("dinner time")
    
    

def convert(time):
    hours, minutes = map(int, time.split(":"))
    total_hours = hours + minutes / 60.0
    return total_hours

if __name__ == "__main__":
    main()
