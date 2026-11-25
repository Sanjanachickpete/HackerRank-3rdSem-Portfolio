def timeConversion(s):
    period = s[-2:]
    time = s[:-2]
    hour, minute, second = time.split(":")
    hour = int(hour)

    if period == "AM":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12

    return f"{hour:02d}:{minute}:{second}"

if __name__ == "__main__":
    print(timeConversion(input().strip()))
