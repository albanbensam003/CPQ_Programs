#Reverse an Array
# input = [11,12,13,14,15]
# new_input = []
# for data in range(len(input)-1,-1,-1):
#     new_input.append(input[data])
# print(new_input)

#Second larget in array

input = [10, 20, 4, 45, 99]
input.sort(reverse=True)
#print(input[1])

input = [10, 20, 4, 45, 99]
new_list = []

second_highest = highest = float("-inf")
for score in input:
    if score > highest:
        second_highest = highest
        highest = score
    elif score >  second_highest and score != highest:
        second_highest = score
print("Second largest:", second_highest)