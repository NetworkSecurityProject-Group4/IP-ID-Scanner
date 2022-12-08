import matplotlib.pyplot as plt

results = open('results_1M.txt', 'r')
local_global = 0
random_odd = 0
constant = 0
curr_id = None
nums = []
for line in results:
    args = line.strip().split(" id ")
    source_ip = args[0]
    if curr_id is None:
        curr_id = source_ip
    seq_num = args[1]
    if curr_id != source_ip:
        if nums: # if list is not empty
            same = nums.count(nums[0]) == len(nums)
            increasing = all(i < j for i, j in zip(nums, nums[1:]))
            if same:
                constant += 1
            if increasing:
                local_global += 1
            else:
                random_odd += 1
        nums.clear()
        curr_id = source_ip
        nums.append(int(seq_num))
    else:
        nums.append(int(seq_num))

# for last ip
if nums: # if list is not empty
    same = nums.count(nums[0]) == len(nums)
    increasing = all(i < j for i, j in zip(nums, nums[1:]))
    if same:
        constant += 1
    if increasing:
        local_global += 1
    else:
        random_odd += 1

total = constant + local_global + random_odd
print(str(round((constant/total)*100,2)) + "% Constant")
print(str(round((local_global/total)*100,2)) + "% Local/Global")
print(str(round((random_odd/total)*100,2)) + "% Random/Odd")

xvals = ['Constant', 'Local/Global', 'Random/Odd']
yvals = [constant, local_global, random_odd]

colors = ['green', 'blue', 'red']
plt.bar(xvals, yvals, color=colors)
plt.title('IP-ID Behavior of 1,000,000 IP Scan', fontsize=14)
plt.xlabel('Sequences', fontsize=14)
plt.ylabel('Number of IPs', fontsize=14)
plt.grid(True)
plt.savefig('graph_1M.png')
results.close()