import datetime
import winsound
def alarm(Timing):
    altime=str(datetime.datetime.now().strptime(Timing,"%I:%M %P"))
    altime=altime[11,-3]

    Horeal=altime[:2]
    Horeal=int(Horeal)
    Mireal=altime[3:5]
    Mireal=int(Mireal)
    print(f"Alarm set for{Timing}")

    while True:
        if Horeal==datetime.datetime.now().hour:
            print("Alarm is running")
            winsound.PlaySound('abc',winsound.SND_LOOP)
        elif Mireal<datetime.datetime.now().minute:
            break
if __name__=='__main__':
    alarm('21:11 PM')