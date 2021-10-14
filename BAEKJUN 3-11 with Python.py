N, X = map(int, input().split()) #정수 두 개를 입력하세요
A = list(map(int, input().split())) #정수 N개로 이루어진 수열 A

for i in range(N): #N개가 될 때까지
    if X > A[i]: #A 수열에 들어간 수가 X 값보다 작다면
        print(A[i], end = " ")
