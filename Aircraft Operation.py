
# coding: utf-8

# In[1]:

def main_logic(each,dep_city,arr_city):
    dep_time = 360
    arr_time = 0
    travel_time = 0
    ground_time = 0 
    i = 0
    while dep_time >= 360 and dep_time < 1320:
        if(dep_time < 1320 - ground_time- travel_time):
            if (dep_city[i] == "DAL" and arr_city[i] == "AUS") or (dep_city[i] == "AUS" and arr_city[i] == "DAL"):
                if(arr_city == "AUS"):
                    ground_time = 30
                else:
                    ground_time = 25
                    travel_time = 50
                    arr_time = dep_time + travel_time
                    dep_tim_1 = (str(int(dep_time / 60)).zfill(2) + str(dep_time % 60).zfill(2))
                    arrival_tim_1 = (str(int(arr_time / 60)).zfill(2) + str(arr_time % 60).zfill(2))
                    print(each,dep_city[i],arr_city[i],dep_tim_1,arrival_tim_1)
                    dep_time = arr_time + ground_time
                    if dep_city[2] == "DAL":
                        i = 0
                    else:
                        i = i + 1
        else:
            break
        if(dep_time < 1320 - ground_time - travel_time):
            if (dep_city[i] == "AUS" and arr_city[i] == "HOU") or (dep_city[i] == "HOU" and arr_city[i] == "AUS"):
                if(arr_city == "HOU"):
                    ground_time = 25
                else:
                    ground_time = 35
                    travel_time = 45
                    arr_time = dep_time + travel_time
                    dep_tim_1 = (str(int(dep_time / 60)).zfill(2) + str(dep_time % 60).zfill(2))
                    arrival_tim_1 = (str(int(arr_time / 60)).zfill(2) + str(arr_time % 60).zfill(2))
                    print(each,dep_city[i],arr_city[i],dep_tim_1,arrival_tim_1)
                    dep_time = arr_time + ground_time
                    if dep_city[2] == "AUS":
                        i = 0
                    else:
                        i = i + 1
        else:
            break
        if(dep_time < 1320 - ground_time - travel_time):
            if (dep_city[i] == "HOU" and arr_city[i] == "DAL") or (dep_city[i] == "DAL" and arr_city[i] == "HOU"):
                if(arr_city == "DAL"):
                    ground_time = 35
                else:
                    ground_time = 30
                    travel_time = 65
                    arr_time = dep_time + travel_time
                    dep_tim_1 = (str(int(dep_time / 60)).zfill(2) + str(dep_time % 60).zfill(2))
                    arrival_tim_1 = (str(int(arr_time / 60)).zfill(2) + str(arr_time % 60).zfill(2))
                    print(each,dep_city[i],arr_city[i],dep_tim_1,arrival_tim_1)
                    dep_time = arr_time + ground_time
                    if dep_city[2] == "HOU":
                        i = 0
                    else:
                        i = i + 1
        else:
            break



# In[3]:

city = ['AUS','HOU','DAL']
flights = ["T1","T2","T3","T4","T5","T6"]
Terminals = [1,2,3]
if Terminals[0] == 1 and Terminals[1] == 2 and Terminals[2] == 3:
    for each in flights:
        if each == "T1" or each == "T2" or each == "T3":
            j = 0
            arr_city = [city[j+1],city[j+2],city[j]]
            dep_city = [city[j],city[j+1],city[j+2]]
            city = [city[j+1],city[j+2],city[j]]
            main_logic(each,dep_city,arr_city)
        second_order = ["HOU","DAL"]
if each == "T4" or each == "T5" or each == "T6":
    x = "HOU"
    y = "DAL"
    dep_time = 360
    arr_time = 0
    A = "DAL"
    B = "HOU"
    dep_time_1 = 360
    arr_time_1 = 0
    s = ["T4","T5","T6","T4","T5","T6","T4","T5","T6","T4","T5","T6","T4","T5","T6","T4","T5","T6","T4","T5","T6","T4","T5","T6"]
    i = 0
    while dep_time >= 360 and dep_time <= 1200:
        if (x == "HOU" and y == "DAL") :
            travel_time = 65
            ground_time = 30
        arr_time = dep_time + travel_time
        dep_tim_2 = (str(int(dep_time / 60)).zfill(2) + str(dep_time % 60).zfill(2))
        arrival_tim_2 = (str(int(arr_time / 60)).zfill(2) + str(arr_time % 60).zfill(2))
        print(s[i],x,y,dep_tim_2,arrival_tim_2)
        i =i+1
        dep_time = dep_time + travel_time + ground_time
        if (A == "DAL" and B == "HOU") :
            travel_time = 65
            ground_time = 35
        arr_time_1 = dep_time_1 + travel_time
        dep_tim_3 = (str(int(dep_time_1 / 60)).zfill(2) + str(dep_time_1 % 60).zfill(2))
        arrival_tim_3 = (str(int(arr_time_1 / 60)).zfill(2) + str(arr_time_1 % 60).zfill(2))
        print(s[i],A,B,dep_tim_3,arrival_tim_3)
        i = i + 1
        dep_time_1 = dep_time_1 + travel_time + ground_time

