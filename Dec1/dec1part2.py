# Advent of Code 2021 Day 1
# Richard Begley
# December 1, 2021
#

depth = []
count = 0
idx = 0
with open("Dec1Inputpart1.txt", "r") as depths:
    for depthvalue in depths:
        depthvalue = int(depthvalue.strip())
        depth.append(depthvalue)
        depthlistlength = len(depth)

for x in range(depthlistlength):

    if idx < depthlistlength - 3:
        depthsum1 = depth[idx] + depth[idx + 1] + depth[idx + 2]
        depthsum2 = depth[idx + 1] + depth[idx + 2] + depth[idx + 3]
        if depthsum1 < depthsum2:
            count += 1
        else:
            pass
        idx += 1
    else:
        print(count)
