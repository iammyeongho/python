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

    // 날짜 입력 필드 초기화
    const dateInputs = document.querySelectorAll('input[type="date"]');
    dateInputs.forEach(input => {
        if (!input.value) {
            const today = new Date();
            const year = today.getFullYear();
            const month = String(today.getMonth() + 1).padStart(2, '0');
            const day = String(today.getDate()).padStart(2, '0');
            input.value = `${year}-${month}-${day}`;
        }
    });

    // 작업 통계 계산
    function calculateTaskStats() {
        const tasks = document.querySelectorAll('.task-row');
        const totalTasks = tasks.length;
        const completedTasks = document.querySelectorAll('.task-status-done').length;
        const inProgressTasks = document.querySelectorAll('.task-status-in_progress').length;
        const todoTasks = document.querySelectorAll('.task-status-todo').length;

        const stats = {
            total: totalTasks,
            completed: completedTasks,
            inProgress: inProgressTasks,
            todo: todoTasks,
            completionRate: totalTasks > 0 ? (completedTasks / totalTasks * 100).toFixed(1) : 0
        };

        return stats;
    }

    // 통계 업데이트
    function updateStats() {
        const stats = calculateTaskStats();
        const statsElement = document.getElementById('task-stats');
        if (statsElement) {
            statsElement.innerHTML = `
                <div class="mb-3">
                    <h6>전체 작업</h6>
                    <p>${stats.total}개</p>
                </div>
                <div class="mb-3">
                    <h6>완료된 작업</h6>
                    <p>${stats.completed}개</p>
                </div>
                <div class="mb-3">
                    <h6>진행 중인 작업</h6>
                    <p>${stats.inProgress}개</p>
                </div>
                <div class="mb-3">
                    <h6>할 일</h6>
                    <p>${stats.todo}개</p>
                </div>
                <div>
                    <h6>완료율</h6>
                    <p>${stats.completionRate}%</p>
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

    // 테이블 정렬 기능
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