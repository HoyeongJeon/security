# 왜 시저암호가 안전하지 않음? 왜 permutation을 활용한 암호가 안전한가,,,,,,, 
import cProfile

# 치환암호 key를 만들 수 있는 경우의 수는 26! (English)
def faculty(n):
    if n <= 1:
        return 1
    else:
        return faculty(n-1)*n
    
for i in range(10):
    print(faculty(i))
    
#모든 경우의 수를 다 세는 데(brute force) 걸리는 시간
def counter(n):
    cnt = 0
    for i in range(n):
        cnt += 1
    return cnt

cProfile.run("counter(faculty(12))")