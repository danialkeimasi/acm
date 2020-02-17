import sys

inp_str = sys.stdin.read()


inp_str = inp_str.replace('\n', '')
inp_str = inp_str.replace('<', ' ')
inp_str = inp_str.replace('>', ' ')

inp_list = inp_str.split()

stack = []
answers = []
for i in inp_list:
    if i == 'table':
        stack.append(0)

    elif i == '/table':
        answers.append(stack.pop())

    elif i == 'td':
        stack[-1] += 1

print(' '.join(sorted(map(str, answers))))
