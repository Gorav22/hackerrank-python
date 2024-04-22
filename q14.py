# Enter your code here. Read input from STDIN. Print output to STDOUT
n, x = map(int, input().split())
subject = [list(map(float, input().split())) for _ in range(x)]
[print(j) for j in [sum(i)/x for i in zip(*subject)]]
