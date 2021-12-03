# Advent of Code 2021 Day 2
# Richard Begley
# December 2, 2021
# determin the location of the submarine.

horizontal = 0
depth = 0
inputlist = []
aim = 0


def main():

    getdata()
    part1(horizontal, depth, inputlist)
    part2(horizontal, depth, inputlist, aim)


def getdata():

    pass


def part1(horizontal, depth, inputlist):
    with open("Dec2Input.txt", "r") as directions:

        for subpath in directions:
            inputlist = subpath.strip().split(" ")
            # print (f'{inputlist[0]}   {inputlist[1]}')
            if inputlist[0] == "forward":
                horizontal += int(inputlist[1])
            elif inputlist[0] == "down":
                depth += int(inputlist[1])
            elif inputlist[0] == "up":
                depth -= int(inputlist[1])

        solution = horizontal * depth
        print(f" Horizontal position = {horizontal}")
        print(f" depth position = {depth}")
        print(f"solution is {solution}")


def part2(horizontal, depth, inputlist, aim):

    with open("Dec2Input.txt", "r") as directions:

        for subpath in directions:
            inputlist = subpath.strip().split(" ")
            if inputlist[0] == "forward":
                depth += (aim * int(inputlist[1]))
                horizontal += int(inputlist[1])
                #print (f'{horizontal} {aim} {depth}')
            elif inputlist[0] == "down":
                aim += int(inputlist[1])
            elif inputlist[0] == "up":
                aim -= int(inputlist[1])
            else:
                print ('error')
    
        solution = horizontal * depth
        print (f' Aim is {aim}')
        print(f" Horizontal position = {horizontal}")
        print(f" depth position = {depth}")
        print(f"solution is {solution}")            

if __name__ == "__main__":
    main()
