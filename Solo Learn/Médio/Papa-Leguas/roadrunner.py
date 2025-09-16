def roadrunner_safety(distance_to_safety, roadrunner_speed, coyote_speed):
    distance_between = 15
    time_to_safe = distance_to_safety / roadrunner_speed
    time_to_catch = (distance_to_safety + distance_between) / coyote_speed 
    
    # return time_to_catch
    
    if time_to_safe < time_to_catch:
        return "Meep Meep"
    else:
        return "Yum"
    

# Input
try:
    distance = int(input())
    roadrunner_speed = int(input())
    coyote_speed = int(input())
    
    # Output
    print(roadrunner_safety(distance, roadrunner_speed, coyote_speed))
except ValueError:
    print("Please enter integer values only.")