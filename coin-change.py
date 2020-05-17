# ATM Bills Dispenser
# A version of the change making algorithm
# optimize for least number of coins possible

def min(x, y):
  if x < y:
    return x
  return y

def greedy(total, denoms):
  bills = {}
  rem = total
  for denom in denoms:
    while rem - denom >= 0:
      rem = rem - denom
      if denom in bills:
         bills[denom] += 1
      else:
         bills[denom] = 1

  if (rem > 0):
    print(total, "greedy algorithm does not have a solution.")
  else:
    print(total, bills)

def dp(total, denoms):
  # define solutions array of subproblems to be an array containing values larger than the number we're looking for
  sols = [total + 1] * (total + 1)
  # container for our solution
  bills = {}

  for index, sub_prob in enumerate(sols):
    if (index == 0):
       sols[index] = 0
    else:
      for denom in denoms:
        if denom <= index:
          res = index - denom
          sol = sols[res] + 1
          sols[index] = min(sol, sols[index])

  sol_cnt = sols[len(sols) - 1]
  if (sol_cnt > total):
    print(total, "no solution for this problem")
  else:
    sum = total
    denom_i = 0
    while sum > 0:
      denom = denoms[denom_i]
      if (sum - denom < 0) or (sols[sum - denom] + 1 > sol_cnt):
        # skip this denom as it is either too big or  does not lead to minimum solution 
        denom_i += 1
      else:
        if denom in bills:
          bills[denom] += 1
        else:
          bills[denom] = 1
        sum = sum - denom
    print(total, bills)


# tests
sg_denoms = [100, 50, 10, 5, 2, 1]
print("\n\ntests for denomination set: ", sg_denoms)
greedy(102, sg_denoms)
dp(102, sg_denoms)
greedy(15, sg_denoms)
dp(15, sg_denoms)
greedy(17, sg_denoms)
dp(17, sg_denoms)
greedy(53, sg_denoms)
dp(53, sg_denoms)
greedy(11, sg_denoms)
dp(11, sg_denoms)


sg_denoms = [5, 2, 1]
print("\n\ntests for denomination set: ", sg_denoms)
greedy(13, sg_denoms)
dp(13, sg_denoms)
greedy(6, sg_denoms)
dp(6, sg_denoms)

sg_denoms = [3]
print("\n\ntests for denomination set: ", sg_denoms)
greedy(13, sg_denoms)
dp(13, sg_denoms)
greedy(6, sg_denoms)
dp(6, sg_denoms)


