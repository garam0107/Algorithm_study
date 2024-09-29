import sys
sys.stdin = open('input.txt')

n = int(input())
m = int(input())
vote = list(map(int, input().split()))

candidates = {}
for i in range(m):
    # 사진 올라가는 경우 +1
    if candidates.get(vote[i]):
        candidates[vote[i]] += 1
    # 사진 새로 올려야할때
    else:
        # 만약 이미 사진자리 꽉 찼을 때
        if len(candidates) == n:
            min = m
            # (삭제할) 작은 값 찾음
            for idx in candidates:
                if candidates[idx] < min:
                    min = candidates[idx]
                    remove = idx
            # 딕셔너리에서도 삭제
            del (candidates[remove])

        # 사진 틀에 추가
        candidates[vote[i]] = 1

    # 오래된 순서를 값으로 처리
    for j in candidates:
        candidates[j] -= 0.00001

ans = sorted(candidates)
print(*ans)