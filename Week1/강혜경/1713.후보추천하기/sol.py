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
                # 작은 값이 여러개 일 때
                elif candidates[idx] == min:
                    # 순서
                    for j in range(i):
                        # 있던값이 순서가 먼저일 때
                        if vote[j] == remove:
                            break
                        # 새로운값이 순서가 먼저일 때
                        if vote[j] == idx:
                            min = candidates[idx]
                            remove = idx
                            break
            # 다음 순서따질때도 안걸리도록 -1 처리
            for _ in range(min):
                vote[vote.index(remove)] = -1
            # 후보에서도 제거(딕셔너리)
            del (candidates[remove])
        # 사진에 추가
        candidates[vote[i]] = 1
result = sorted(candidates)
print(*result)