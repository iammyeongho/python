// DOM이 로드된 후 실행
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

    // 날짜 선택기 초기화
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

    // 성적 통계 계산
    const calculateStats = () => {
        const scores = Array.from(document.querySelectorAll('.score-value'))
            .map(el => parseFloat(el.textContent))
            .filter(score => !isNaN(score));

        if (scores.length > 0) {
            const sum = scores.reduce((a, b) => a + b, 0);
            const avg = sum / scores.length;
            const max = Math.max(...scores);
            const min = Math.min(...scores);
            const variance = scores.reduce((a, b) => a + Math.pow(b - avg, 2), 0) / scores.length;
            const stdDev = Math.sqrt(variance);

            document.querySelector('.avg-score').textContent = avg.toFixed(2);
            document.querySelector('.max-score').textContent = max.toFixed(2);
            document.querySelector('.min-score').textContent = min.toFixed(2);
            document.querySelector('.std-dev').textContent = stdDev.toFixed(2);
        }
    };

    // 성적 통계가 있는 페이지에서만 실행
    if (document.querySelector('.score-value')) {
        calculateStats();
    }

    // 출석 통계 계산
    const calculateAttendanceStats = () => {
        const statusCounts = {
            present: 0,
            late: 0,
            earlyLeave: 0,
            absent: 0
        };

        document.querySelectorAll('.attendance-status').forEach(el => {
            const status = el.textContent.trim().toLowerCase();
            if (statusCounts.hasOwnProperty(status)) {
                statusCounts[status]++;
            }
        });

        document.querySelector('.present-count').textContent = statusCounts.present;
        document.querySelector('.late-count').textContent = statusCounts.late;
        document.querySelector('.early-leave-count').textContent = statusCounts.earlyLeave;
        document.querySelector('.absent-count').textContent = statusCounts.absent;
    };

    // 출석 통계가 있는 페이지에서만 실행
    if (document.querySelector('.attendance-status')) {
        calculateAttendanceStats();
    }

    // 모달 닫기 버튼 이벤트
    const closeButtons = document.querySelectorAll('[data-dismiss="modal"]');
    closeButtons.forEach(button => {
        button.addEventListener('click', () => {
            const modal = button.closest('.modal');
            if (modal) {
                modal.classList.remove('show');
                modal.style.display = 'none';
                document.body.classList.remove('modal-open');
            }
        });
    });

    // 알림 메시지 자동 숨김
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 500);
        }, 3000);
    });

    // 테이블 정렬 기능
    const sortableTables = document.querySelectorAll('.sortable');
    sortableTables.forEach(table => {
        const headers = table.querySelectorAll('th[data-sort]');
        headers.forEach(header => {
            header.addEventListener('click', () => {
                const column = header.dataset.sort;
                const rows = Array.from(table.querySelectorAll('tbody tr'));
                const direction = header.dataset.direction === 'asc' ? -1 : 1;
                
                rows.sort((a, b) => {
                    const aValue = a.querySelector(`td[data-sort="${column}"]`).textContent;
                    const bValue = b.querySelector(`td[data-sort="${column}"]`).textContent;
                    
                    if (!isNaN(aValue) && !isNaN(bValue)) {
                        return (parseFloat(aValue) - parseFloat(bValue)) * direction;
                    }
                    return aValue.localeCompare(bValue) * direction;
                });

                table.querySelector('tbody').innerHTML = '';
                rows.forEach(row => table.querySelector('tbody').appendChild(row));
                
                headers.forEach(h => h.dataset.direction = '');
                header.dataset.direction = direction === 1 ? 'asc' : 'desc';
            });
        });
    });

    // 반응형 테이블 스크롤
    const responsiveTables = document.querySelectorAll('.table-responsive');
    responsiveTables.forEach(table => {
        let isDown = false;
        let startX;
        let scrollLeft;

        table.addEventListener('mousedown', (e) => {
            isDown = true;
            startX = e.pageX - table.offsetLeft;
            scrollLeft = table.scrollLeft;
        });

        table.addEventListener('mouseleave', () => {
            isDown = false;
        });

        table.addEventListener('mouseup', () => {
            isDown = false;
        });

        table.addEventListener('mousemove', (e) => {
            if (!isDown) return;
            e.preventDefault();
            const x = e.pageX - table.offsetLeft;
            const walk = (x - startX) * 2;
            table.scrollLeft = scrollLeft - walk;
        });
    });
}); 