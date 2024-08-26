import random

random_num = random.randint(1,10);
user_num = -1
guess = 0;
print(random_num)

while(user_num != random_num):
    guess+=1;
    user_num = int(input("Enter a random number between(1 to 10): "))
    if random_num > user_num:
        print("Higher number please")
    elif(random_num < user_num): 
        print("Lower number please")
    else:
        print(f"Great..!! Your guess is correct🎉🥳 in {guess} attempt")