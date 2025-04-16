"""
기본 성능 테스트 예제
이 파일은 웹 애플리케이션의 기본적인 성능을 테스트하는 방법을 보여줍니다.
"""

import time
import statistics
import requests
from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict, Any
import matplotlib.pyplot as plt
import numpy as np

class PerformanceTester:
    """성능 테스트 클래스"""
    
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
    
    def measure_response_time(self, endpoint: str, method: str = 'GET', 
                            data: Dict[str, Any] = None) -> float:
        """단일 요청의 응답 시간을 측정합니다."""
        start_time = time.time()
        
        if method == 'GET':
            response = self.session.get(f"{self.base_url}{endpoint}")
        elif method == 'POST':
            response = self.session.post(f"{self.base_url}{endpoint}", json=data)
        elif method == 'PUT':
            response = self.session.put(f"{self.base_url}{endpoint}", json=data)
        elif method == 'DELETE':
            response = self.session.delete(f"{self.base_url}{endpoint}")
        
        response.raise_for_status()
        return time.time() - start_time
    
    def measure_concurrent_requests(self, endpoint: str, num_requests: int = 100,
                                  method: str = 'GET', data: Dict[str, Any] = None) -> List[float]:
        """동시 요청의 응답 시간을 측정합니다."""
        response_times = []
        
        def make_request():
            try:
                response_time = self.measure_response_time(endpoint, method, data)
                response_times.append(response_time)
            except Exception as e:
                print(f"요청 실패: {e}")
        
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(make_request) for _ in range(num_requests)]
            for future in futures:
                future.result()
        
        return response_times
    
    def analyze_response_times(self, response_times: List[float]) -> Dict[str, float]:
        """응답 시간 데이터를 분석합니다."""
        return {
            '평균': statistics.mean(response_times),
            '중앙값': statistics.median(response_times),
            '최소': min(response_times),
            '최대': max(response_times),
            '표준편차': statistics.stdev(response_times) if len(response_times) > 1 else 0
        }
    
    def plot_response_times(self, response_times: List[float], title: str):
        """응답 시간 분포를 시각화합니다."""
        plt.figure(figsize=(10, 6))
        plt.hist(response_times, bins=20, alpha=0.75)
        plt.title(title)
        plt.xlabel('응답 시간 (초)')
        plt.ylabel('빈도')
        plt.grid(True)
        plt.savefig(f"{title.replace(' ', '_')}.png")
        plt.close()

def main():
    """메인 함수"""
    # 테스트 설정
    base_url = "http://localhost:5000"
    tester = PerformanceTester(base_url)
    
    # 테스트할 엔드포인트 목록
    endpoints = [
        ('/users', 'GET'),
        ('/users/1', 'GET'),
        ('/posts', 'GET'),
        ('/posts/1', 'GET')
    ]
    
    # 각 엔드포인트별 성능 테스트 수행
    for endpoint, method in endpoints:
        print(f"\n{endpoint} 엔드포인트 테스트 중...")
        
        # 동시 요청 테스트
        response_times = tester.measure_concurrent_requests(
            endpoint=endpoint,
            num_requests=100,
            method=method
        )
        
        # 결과 분석
        analysis = tester.analyze_response_times(response_times)
        print(f"\n{endpoint} 분석 결과:")
        for metric, value in analysis.items():
            print(f"{metric}: {value:.4f}초")
        
        # 결과 시각화
        tester.plot_response_times(
            response_times,
            f"{endpoint} 응답 시간 분포"
        )
    
    # 부하 테스트
    print("\n부하 테스트 수행 중...")
    load_test_endpoints = [
        ('/users', 'POST', {'username': 'testuser', 'email': 'test@example.com'}),
        ('/posts', 'POST', {'title': 'Test Post', 'content': 'Test Content'})
    ]
    
    for endpoint, method, data in load_test_endpoints:
        print(f"\n{endpoint} 부하 테스트 중...")
        
        # 점진적으로 부하를 증가시키면서 테스트
        for num_requests in [10, 50, 100, 200]:
            print(f"\n동시 요청 수: {num_requests}")
            
            response_times = tester.measure_concurrent_requests(
                endpoint=endpoint,
                num_requests=num_requests,
                method=method,
                data=data
            )
            
            analysis = tester.analyze_response_times(response_times)
            print("분석 결과:")
            for metric, value in analysis.items():
                print(f"{metric}: {value:.4f}초")
            
            # 응답 시간이 1초를 초과하면 경고
            if analysis['평균'] > 1.0:
                print("경고: 평균 응답 시간이 1초를 초과했습니다!")

if __name__ == '__main__':
    main() 