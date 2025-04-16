"""
부하 테스트 예제
이 파일은 웹 애플리케이션의 부하 테스트를 수행하는 방법을 보여줍니다.
"""

import time
import statistics
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict, Any, Tuple
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

class LoadTester:
    """부하 테스트 클래스"""
    
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
    
    def run_load_test(self, endpoint: str, method: str = 'GET',
                     data: Dict[str, Any] = None, num_users: int = 100,
                     requests_per_user: int = 10, ramp_up_time: int = 10) -> Dict[str, Any]:
        """부하 테스트를 실행합니다."""
        start_time = time.time()
        results = {
            'response_times': [],
            'success_count': 0,
            'failure_count': 0,
            'errors': []
        }
        
        def user_behavior(user_id: int):
            """사용자 시나리오를 시뮬레이션합니다."""
            user_results = []
            
            # 로그인
            try:
                login_time = self.measure_response_time(
                    '/login',
                    'POST',
                    {'email': f'user{user_id}@example.com', 'password': 'password123'}
                )
                user_results.append(('login', login_time))
            except Exception as e:
                results['failure_count'] += 1
                results['errors'].append(f'User {user_id} login failed: {str(e)}')
                return user_results
            
            # 게시글 목록 조회
            try:
                list_time = self.measure_response_time('/posts', 'GET')
                user_results.append(('list_posts', list_time))
            except Exception as e:
                results['failure_count'] += 1
                results['errors'].append(f'User {user_id} list posts failed: {str(e)}')
            
            # 게시글 작성
            try:
                create_time = self.measure_response_time(
                    '/posts',
                    'POST',
                    {'title': f'Test Post {user_id}', 'content': 'Test Content'}
                )
                user_results.append(('create_post', create_time))
            except Exception as e:
                results['failure_count'] += 1
                results['errors'].append(f'User {user_id} create post failed: {str(e)}')
            
            return user_results
        
        # 사용자 시뮬레이션 실행
        with ThreadPoolExecutor(max_workers=num_users) as executor:
            # 램프업 시간 동안 사용자를 점진적으로 추가
            users_per_second = num_users / ramp_up_time
            futures = []
            
            for i in range(num_users):
                # 램프업 시간에 맞춰 사용자 추가
                if i > 0:
                    time.sleep(1 / users_per_second)
                
                future = executor.submit(user_behavior, i)
                futures.append(future)
            
            # 결과 수집
            for future in as_completed(futures):
                user_results = future.result()
                for operation, response_time in user_results:
                    results['response_times'].append(response_time)
                    results['success_count'] += 1
        
        # 테스트 결과 분석
        results['total_time'] = time.time() - start_time
        results['throughput'] = results['success_count'] / results['total_time']
        
        if results['response_times']:
            results['avg_response_time'] = statistics.mean(results['response_times'])
            results['p95_response_time'] = np.percentile(results['response_times'], 95)
            results['p99_response_time'] = np.percentile(results['response_times'], 99)
        
        return results
    
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
    
    def plot_results(self, results: Dict[str, Any], test_name: str):
        """테스트 결과를 시각화합니다."""
        # 응답 시간 분포
        plt.figure(figsize=(15, 5))
        
        plt.subplot(1, 2, 1)
        plt.hist(results['response_times'], bins=20, alpha=0.75)
        plt.title('응답 시간 분포')
        plt.xlabel('응답 시간 (초)')
        plt.ylabel('빈도')
        plt.grid(True)
        
        # 성공/실패 비율
        plt.subplot(1, 2, 2)
        success_rate = results['success_count'] / (results['success_count'] + results['failure_count'])
        plt.pie([success_rate, 1 - success_rate],
                labels=['성공', '실패'],
                autopct='%1.1f%%',
                colors=['green', 'red'])
        plt.title('요청 성공률')
        
        plt.suptitle(f'{test_name} - 부하 테스트 결과')
        plt.tight_layout()
        plt.savefig(f"{test_name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
        plt.close()

def main():
    """메인 함수"""
    # 테스트 설정
    base_url = "http://localhost:5000"
    tester = LoadTester(base_url)
    
    # 테스트 시나리오
    scenarios = [
        {
            'name': '기본 부하 테스트',
            'num_users': 100,
            'requests_per_user': 10,
            'ramp_up_time': 10
        },
        {
            'name': '중간 부하 테스트',
            'num_users': 200,
            'requests_per_user': 20,
            'ramp_up_time': 20
        },
        {
            'name': '고부하 테스트',
            'num_users': 500,
            'requests_per_user': 30,
            'ramp_up_time': 30
        }
    ]
    
    # 각 시나리오별 테스트 수행
    for scenario in scenarios:
        print(f"\n{scenario['name']} 시작...")
        
        results = tester.run_load_test(
            endpoint='/posts',
            num_users=scenario['num_users'],
            requests_per_user=scenario['requests_per_user'],
            ramp_up_time=scenario['ramp_up_time']
        )
        
        # 결과 출력
        print(f"\n{scenario['name']} 결과:")
        print(f"총 실행 시간: {results['total_time']:.2f}초")
        print(f"처리량: {results['throughput']:.2f} 요청/초")
        print(f"성공한 요청: {results['success_count']}")
        print(f"실패한 요청: {results['failure_count']}")
        print(f"평균 응답 시간: {results['avg_response_time']:.4f}초")
        print(f"95번째 백분위수 응답 시간: {results['p95_response_time']:.4f}초")
        print(f"99번째 백분위수 응답 시간: {results['p99_response_time']:.4f}초")
        
        # 오류 출력
        if results['errors']:
            print("\n발생한 오류:")
            for error in results['errors'][:5]:  # 처음 5개 오류만 출력
                print(f"- {error}")
            if len(results['errors']) > 5:
                print(f"... 그리고 {len(results['errors']) - 5}개의 추가 오류")
        
        # 결과 시각화
        tester.plot_results(results, scenario['name'])

if __name__ == '__main__':
    main() 