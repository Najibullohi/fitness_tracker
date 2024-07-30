storage_data ={}

def accept_package (pocket):
    if check_correct_data(pocket):
        time,steps = pocket
        storage_data(time,steps)
        return storage_data
def check_correct_data(pocket):
    if len(pocket)!=2 :
        return False
    time , steps = pocket
    if not time or steps is None:
        return False
    return True 
def store_data(time, spteps):
    storage_data[time] = spteps 
def display_summary(time, steps):
    total_steps = sum(storage_data.values())
    distance = total_steps * 76.2
    calories_burned = total_steps * 0.05
    print("\nTime: {}.\nNumber of steps today: {}.\nDistance was{:.2f} km.\nYou burned {:.2f} kcal.".format(time,total_steps, distance, calories_burned))
    
    if distance >= 6.5:
        print("Great result: Goal reached.")
    elif distance >=3.9:
        print ("Not bad It was a productive day")
    elif distance >=2:
        print("We will catch up tomorrow")
    else:
        print("Lying down is also useful. The main thing is participation, not victory")  

accept_package(('09:36:02', 15000))  
accept_package(('10:00:00', 5000)) 