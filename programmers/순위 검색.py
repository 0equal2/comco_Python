###프로그래머스
###2021 KAKAO BLIND RECRUITMENT
###순위검색

from collections import defaultdict
from itertools import combinations

def solution(info, query):
    answer = []
    
    #1. 지원자 정보 parsing
    applicant=defaultdict(list)
    
    for x in info:
        x=x.split()
        keylist=x[:-1]
        score=int(x[-1])
        
        #1-1. 점수를 제외한 4가지 조건이 '-'일수도 있는 16가지 구하기
        for i in range(5):
            for c in combinations(keylist,i):
                key=''.join(c)
                
                applicant[key].append(score)
                
    
    #2. applicant의 key에 따른 value 정렬 (점수 정렬)
    for key in applicant.keys():
        applicant[key].sort()
        
    
    
    #3. 조건 parsing
    
    for x in query:
        q=[]
        x=x.split(' ')
        
        #3-1. and, - 제외하기 (필요조건으로만 key생성)
        for y in x:
            if y!='and' and y!='-':
                q.append(y)
                
        key=''.join(q[:-1])
        score=int(q[-1])
        
        #3-2. 이분탐색으로 조건에 해당하는 지원자 수 구하기
        count=0
        
        if key in applicant.keys(): #해당 조건의 지원자가 있는지 확인 
            value=applicant[key]
            start,end=0,len(value)
            while start<=end and start<len(value):
                mid=(start+end)//2
                
                if value[mid]<score:
                    start=mid+1
                else:
                    end=mid-1
                    
            count=len(value)-start
                    
        
        answer.append(count)
        
    return answer
