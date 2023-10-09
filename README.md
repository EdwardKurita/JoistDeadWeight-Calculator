# JoistDeadWeight-Calculator

Project for ECOR 1046, Summer 2023

Description:

This code takes in two text file inputs. The first one is a list of members and its self weight. The next file contains a list of joints with all the members that are connected to that joint, along with any external forces on the joint itself. The main program reads in the information from these files, seperates them into their respective lists/dictionaries. The program then creates an output file and runs a formula using the dead weight of adjacent members to calculate the total dead weight at each joint. Each joint and its respective dead weight is then added to the output file, line by line.
