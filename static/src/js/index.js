
var ctx = document.getElementById('statusChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['ONLINE', 'OFFLINE'],
            datasets: [{
                data: [
                    {{ online_count }},
                    {{ offline_count }}
                ],
                backgroundColor: [
                    'rgba(0, 191, 255, 0.7)',
                    'rgba(255, 0, 0, 0.7)',
                ],
                borderColor: [
                    'rgba(0, 191, 255, 0.7)',
                    'rgba(255, 0, 0, 0.7)',
                ],
                borderWidth: 1
            }]
        },
        options: {
            cutout: '80%',
        }
    });