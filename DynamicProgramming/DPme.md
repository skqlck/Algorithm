### B11055와 B11055_1의 차이점

* B11055
  
  DP를 A의 idx에 맞춰서 설정하기 때문에 현재 idx에 대하여
  
  DP값을 갱신하려면 i < j & A[i] < A[j] 인 j 중에서 DP[j]가 최대인 값을
  
  이용하여 DP[i] = max(DP[j_s]+A[i],DP[i])

*  B11055_1
  
  A의 원소 값(=a)들이 DP의 idx로 설정
  
  DP값 갱신을 A의 원소를 앞에서부터(==부분 수열 만드는 조건) 순회하면서
  
  DP[a] = max(DP[:a]) + a

* 차이점
  
  * _1은 A의 원소들끼리 크기 비교를 하지 않는다.
    
    => DP[:a]는 a보다 작은 값이 부분 수열의 마지막인 것들의 DP값들
  
  * _1이 실행시간이 더 짧은데, 이는 테스트케이스 따라 다름
    
    ex) A = [999,1000] 의 경우
    
    _1은 DP[999]를 갱신하기 위해 DP[0]부터 DP[998]까지 최대값을 구해야하지만, B11055는 이를 읽지 않는다.
    
    