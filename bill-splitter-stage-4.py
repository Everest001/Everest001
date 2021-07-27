# write your code here
# write your code here
import random
print("Enter the number of friends joining (including you):")
friends_number = int(input())
if friends_number <= 0:
    print('No one is joining for the party')
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friends_name = {}
    for i in range(friends_number):
        friends_name[input()] = 0
    
    print("Enter the total bill value:")
    total_bill = int(input())

    print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:")
    lucky_feature = input()
    if lucky_feature == "Yes":
        lucky_friend = random.choice(list(friends_name.keys()))
        print(lucky_friend)
        shared_bill = round((total_bill/(friends_number-1)),2)
        friends_name.pop(lucky_friend)
        friends_dict = dict.fromkeys(friends_name, shared_bill)
        friends_dict [lucky_friend] = 0
        print(friends_dict)
    else:
        print("No one is going to be lucky")
        shared_bill = round((total_bill/(friends_number)),2)
        friends_dict = dict.fromkeys(friends_name, shared_bill)
        print(friends_dict)