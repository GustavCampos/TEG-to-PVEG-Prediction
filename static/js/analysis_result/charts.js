document.addEventListener('DOMContentLoaded', function() {
    const chartProportionwindow = 16 / 9;
    const chartWidth = window.screen.width * 0.8;
    const chartHeight = chartWidth / chartProportionwindow;

    const hourlyTempPoutCanvas = document.getElementById("hourly-temp-pout-chart");
    hourlyTempPoutCanvas.width = chartWidth;
    hourlyTempPoutCanvas.height = chartHeight;

    const hourlyData = JSON.parse(sessionStorage['hourlyData']);
    const hourlyPout = hourlyData['wh_output'];
    const hourlyTemp = hourlyData['cell_temperature'];
    const xLabels = [...Array(hourlyPout.length).keys()];

    const startDate = new Date(sessionStorage['startDate']);
    const docLang = document.querySelector("html").lang;


    const hourlyTempPoutChart = new Chart(hourlyTempPoutCanvas, {
        type: 'line',
        data: {
            labels: xLabels,
            datasets: [
                {
                    label: 'Temperatura da Célula (°C)',
                    data: hourlyTemp,
                    fill: false,
                    borderColor: 'rgb(255, 99, 132)',
                    tension: 0.1,
                    yAxisID: 'temp'
                },
                {
                    label: 'Energia Gerada (W)',
                    data: hourlyPout,
                    fill: false,
                    borderColor: 'rgb(75, 192, 192)',
                    tension: 0.1,
                    yAxisID: 'pout'
                }
            ]
        },
        options: {
            responsive: true,
            interaction: {
                mode: 'index',
                intersect: false,
            },
            stacked: false,
            plugins: {
                title: {
                  display: true,
                  text: 'Temperatura da Célula e Energia Gerada por Hora'
                },
                tooltip: {
                    callbacks: {
                        title: function(context) {
                            const hoursToAdd = parseFloat(context[0].label);
                            const hourMultiplier = 60 * 60 * 1000;

                            const newDate = new Date(startDate.getTime() + (hoursToAdd * hourMultiplier));
                            return newDate.toUTCString();
                        },
                        label: function(context) {                            
                            const label = context.dataset.label || '';
                            const value = context.raw;
                            const locale = docLang || 'en-US';

                            return `${label}: ${value.toLocaleString(locale, {
                                minimumFractionDigits: 2,
                                maximumFractionDigits: 2,
                            })}`;
                        }
                    }
                },
            },
            maintainAspectRatio: false,
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Hora a Partir do Início da Simulação'
                    }
                },
                pout: {
                    type: 'linear',
                    display: true,
                    position: 'left',
                    title: {
                        display: true,
                        text: 'Energia Gerada (W)'
                    }
                },
                temp: {
                    type: 'linear',
                    display: true,
                    position: 'right',
                    title: {
                        display: true,
                        text: 'Temperatura da Célula (°C)'
                    },

                    // grid line settings
                    grid: {
                        drawOnChartArea: false, // only want the grid lines for one axis to show up
                
                    }
                }
            }
        }
    });
});