# Advent of Code 2021 Day 1
# Richard Begley
# December 1, 2021
# Count how many time the depth increases

depth = []
count = 0
idx = 0
with open("Dec1Inputpart1.txt", "r") as depths:
    for depthvalue in depths:
        depthvalue = int(depthvalue.strip())
        depth.append(depthvalue)
        depthlistlength = len(depth)

for x in range(depthlistlength):

    if idx < depthlistlength - 1:
        # print(depth[idx])
        # print(depth[idx + 1])
        depth1 = depth[idx]
        depth2 = depth[idx + 1]
        if depth1 < depth2:
            count += 1
        else:
            pass
        idx += 1
    else:
        print(count)
