document.addEventListener('DOMContentLoaded', function() {
    // 폼 유효성 검사
    const forms = document.querySelectorAll('.needs-validation');
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });

    // 게시글 통계 계산
    function calculatePostStats() {
        const posts = document.querySelectorAll('.post-card');
        const totalPosts = posts.length;
        const recentPosts = Array.from(posts).filter(post => {
            const date = new Date(post.dataset.createdAt);
            const now = new Date();
            const diffDays = Math.floor((now - date) / (1000 * 60 * 60 * 24));
            return diffDays <= 7;
        }).length;

        const stats = {
            total: totalPosts,
            recent: recentPosts,
            recentPercentage: totalPosts > 0 ? (recentPosts / totalPosts * 100).toFixed(1) : 0
        };

        return stats;
    }

    // 통계 업데이트
    function updateStats() {
        const stats = calculatePostStats();
        const statsElement = document.getElementById('post-stats');
        if (statsElement) {
            statsElement.innerHTML = `
                <div class="mb-3">
                    <h6>전체 게시글</h6>
                    <p>${stats.total}개</p>
                </div>
                <div class="mb-3">
                    <h6>최근 7일 게시글</h6>
                    <p>${stats.recent}개</p>
                </div>
                <div>
                    <h6>최근 게시글 비율</h6>
                    <p>${stats.recentPercentage}%</p>
                </div>
            `;
        }
    }

    // 모달 닫기 버튼 이벤트
    const closeButtons = document.querySelectorAll('[data-bs-dismiss="modal"]');
    closeButtons.forEach(button => {
        button.addEventListener('click', () => {
            const modal = button.closest('.modal');
            if (modal) {
                const modalInstance = bootstrap.Modal.getInstance(modal);
                if (modalInstance) {
                    modalInstance.hide();
                }
            }
        });
    });

    // 알림 메시지 자동 숨김
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // 게시글 정렬 기능
    const sortableTables = document.querySelectorAll('.sortable');
    sortableTables.forEach(table => {
        const headers = table.querySelectorAll('th[data-sort]');
        headers.forEach(header => {
            header.addEventListener('click', () => {
                const column = header.dataset.sort;
                const direction = header.dataset.direction === 'asc' ? 'desc' : 'asc';
                header.dataset.direction = direction;

                const tbody = table.querySelector('tbody');
                const rows = Array.from(tbody.querySelectorAll('tr'));

                rows.sort((a, b) => {
                    const aValue = a.querySelector(`td[data-${column}]`).dataset[column];
                    const bValue = b.querySelector(`td[data-${column}]`).dataset[column];

                    if (direction === 'asc') {
                        return aValue > bValue ? 1 : -1;
                    } else {
                        return aValue < bValue ? 1 : -1;
                    }
                });

                tbody.innerHTML = '';
                rows.forEach(row => tbody.appendChild(row));
            });
        });
    });

    // 초기 통계 업데이트
    updateStats();
}); 