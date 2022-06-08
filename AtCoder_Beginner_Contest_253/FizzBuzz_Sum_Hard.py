from math import gcd

def calc(max_1,x):
  n = max_1 // x
  a_1,d = x,x
  return n * (2 * a_1 + (n - 1) * d) // 2


num_list = list(map(int, input().split()))
lcm = (num_list[1] * num_list[2]) // gcd(num_list[1], num_list[2])
ans = calc(num_list[0],1) - calc(num_list[0],num_list[1]) - calc(num_list[0],num_list[2]) + calc(num_list[0],lcm)
print(ans)