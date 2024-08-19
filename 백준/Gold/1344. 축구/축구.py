a=int(input())
b=int(input())

prime = [2,3,5,7,11,13,17]
dp_a = [0] * 19
dp_a[0] = 100
dp_b = [0] * 19
dp_b[0] = 100

goal_a=a/100
n_goal_a=(100-a)/100
goal_b=b/100
n_goal_b=(100-b)/100

for i in range(18):
    for i in range(i, -1, -1):
        if dp_a[i] != 0:
            dp_a[i+1] += dp_a[i] * goal_a
            dp_a[i] = dp_a[i] * n_goal_a
        if dp_b[i] != 0:
            dp_b[i+1] += dp_b[i] * goal_b
            dp_b[i] = dp_b[i] * n_goal_b

a_r = 0
b_r = 0
for i in prime:
    a_r+=dp_a[i]
    b_r+=dp_b[i]


print(1-(100-a_r)*(100-b_r)*0.0001)
