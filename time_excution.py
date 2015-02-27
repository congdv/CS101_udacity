import time

def time_excution(code):
	start_time = time.clock()
	result     = eval(code)
	run_time   = time.clock() - start_time
	return result, run_time
def spin_loop(n):
	i = 0
	while i < n:
		i = i + 1
print time_excution("spin_loop(10**9)")