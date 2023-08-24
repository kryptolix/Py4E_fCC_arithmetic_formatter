def arithmetic_arranger(problems, output=False):
  import re
  import operator

  #define operators you wanna use
  allowed_operators = {
    "+": operator.add,
    "-": operator.sub,
  }

  arr_problemslist = [""] * 4
  i = 1

  # Check for input Errors
  if len(problems) > 5:
    return "Error: Too many problems."
  for problem in problems:

    spl = problem.split()
    if spl[1] == "/" or spl[1] == "*":
      return "Error: Operator must be '+' or '-'."
    if len(spl[0]) > 4 or len(spl[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
    if re.search('[^0-9]', spl[0]) or re.search('[^0-9]', spl[2]):
      return "Error: Numbers must only contain digits."

# Calculation and Output
    res = spl.index(max(spl, key=len))
    lenres = len(spl[res]) + 2

    arr_problemslist[0] += spl[0].rjust(lenres)
    arr_problemslist[1] += spl[1] + spl[2].rjust(lenres - 1)
    arr_problemslist[2] += "-" * lenres
    if output == True:
      arr_problemslist[3] += str(allowed_operators[spl[1]](int(
        spl[0]), int(spl[2]))).rjust(lenres)
# Concatenate Strings
    if i < len(problems):
      for item in range(len(arr_problemslist)):
        arr_problemslist[item] += "    "
    i += 1

  if output == False:
    del arr_problemslist[-1]


# Build final string
  arranged_problems = "\n".join(str(element) for element in arr_problemslist)
  return arranged_problems
