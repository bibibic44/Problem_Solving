def solution(s):
    answer = 1

    for i in range(len(s)):
        tmp_odd = 1
        # 길이가 홀수인 좌우 대칭(팰린드롬) 확인
        for j in range(1, i+1):
            if 0 <= i - j and i + j < len(s) and s[i - j] == s[i + j]:
                    tmp_odd += 2
            # 좌우 대칭이 아니면 바로 break 한다.
            else:
                break
        # 길이가 짝수인 좌우 대칭 확인
        tmp_even = 0
        for j in range(0, i+1):
            if 0 <= i - j and i + j + 1 < len(s) and s[i - j] == s[i + j + 1]:
                tmp_even += 2
            else:
                break
        answer = max(answer, tmp_odd, tmp_even)

    return answer
