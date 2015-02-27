distance = 2500 # km between Palo Alto and Cambridge
c = 200000 # km/s (approximate speed of light)
time = 0.075 # 100 ms = 0.1s

light_time = float(distance) / c*1000
print light_time
print time / light_time
print 2**10 * 8