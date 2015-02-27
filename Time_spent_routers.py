#How long does the data spend at the routers?

#Information given in question

total_time = 75 # milisenconds traceroute, round trip Birmingham -> Sundsvall
one_way_distance = 2500.0 #Km, Birmingham -> Sundsvall
optic_speed = 200000 # Km/s
ms_per_second = 1000 # conversion from ms to seconds [ms/sec]

#Calculations
time_on_the_wire =2 * one_way_distance /optic_speed * ms_per_second
print time_on_the_wire
total_time_at_routers = total_time - time_on_the_wire
print total_time_at_routers