#Function that intakes the file information and writes the correct output to the output file.
def joint_dead_load_lists():
    #The first file, DeadLoadofMembers.txt, contains the name of each member followed by its paired self weight.
    file_1 = open("DeadLoadofMembers.txt", "r")
    Dead_Load_Dict = {}
    #This for loop puts the name of every member as a key in a dictionary, with its respective self weight as the stored value.
    for line in file_1:
        temp = line.split()
        Dead_Load_Dict[temp[0]] = float(temp[1])
    #Adding a key called "N/A" for when a joint is connected to less than 5 members.
    Dead_Load_Dict["N/A"] = 0
    file_1.close()
    #The next file, JointsandOWSJ.txt, contains the name of each joint followed by all the connected members and then by the dead load of the OWSJ if any. For example, the A joint file line looks like: A AB AP N/A N/A N/A 0. A is only connected to two members: AB and AP and is not affected by the OWSJ dead load.
    file_2 = open("JointsandOWSJ.txt", "r")
    Joint_List = []
    for line in file_2:
        Joint_List += [line.split()]
    file_2.close()
    per_joint_weight = []
    #this for loop adds each joint and its respective factored dead load of OWSJ and self weight to a list.
    for item in Joint_List:
        per_joint_weight += [[item[0]] + [factored_dead_load_math(Dead_Load_Dict, item[1], item[2], item[3], item[4], item[5], float(item[6]))]]
    #all the informationfrom the per_joint_weight list is being written to the output file in the format of joint name followed by factored dead load of OWSJ and self weight.
    file_3 = open("Output.txt", "w")
    for pair in per_joint_weight:
        for item in pair:
            file_3.write(str(item) + " ")
        file_3.write("\n")
    file_3.close()
    
#Function that calculates the dead load of self weight of members on each joint by applying a generalized equation that can be applied to all joints        
def factored_dead_load_math(Dead_Loads: dict, member_1: str, member_2: str, member_3: str, member_4: str, member_5: str, OWSJ: float) -> float:
    #The factored OWSJ dead load is only applied if the OWSJ value in the JointsandOWSJ.txt is not 0. As long as that file is formatted correctly, only the upper joints of the truss will include the factored OWSJ dead load, as dictated by the outline.
    return round(1.25 * OWSJ + 1.25 * (Dead_Loads[member_1] / 2 + Dead_Loads[member_2] / 2 + Dead_Loads[member_3] / 2 + Dead_Loads[member_4] / 2 + Dead_Loads[member_5] / 2), 3)
