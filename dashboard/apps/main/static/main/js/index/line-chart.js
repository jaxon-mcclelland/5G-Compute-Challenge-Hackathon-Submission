document.addEventListener("DOMContentLoaded", function() {
    // Bar chart
    
    // console.log(getTableData())
    function buildTemperatureChart(temperature){
        var temperature = new Chart(document.getElementById("temperature"), {
            type: "line",
            data: {
                labels: tableData.time,
                datasets: [{
                    label: "Temperature",
                    fill: true,
                    backgroundColor: "transparent",
                    borderColor: window.theme.primary,
                    data: tableData.temperature,
                }]
            },
            options: {
                maintainAspectRatio: false,
                legend: {
                    display: false
                },
                scales: {
                    yAxes: [{
                        gridLines: {
                            display: false
                        },
                        stacked: false,
                        ticks: {
                            stepSize: 20
                        }
                    }],
                    xAxes: [{
                        stacked: false,
                        gridLines: {
                            color: "transparent"
                        }
                    }]
                }
            }
        });
    }
    function buildHumidityChart(temperature){
        var temperature = new Chart(document.getElementById("humidity"), {
            type: "line",
            data: {
                labels: tableData.time,
                datasets: [{
                    label: "Humidity",
                    fill: true,
                    backgroundColor: "transparent",
                    borderColor: window.theme.primary,
                    data: tableData.humidity,
                }]
            },
            options: {
                maintainAspectRatio: false,
                legend: {
                    display: false
                },
                scales: {
                    yAxes: [{
                        gridLines: {
                            display: false
                        },
                        stacked: false,
                        ticks: {
                            stepSize: 20
                        }
                    }],
                    xAxes: [{
                        stacked: false,
                        gridLines: {
                            color: "transparent"
                        }
                    }]
                }
            }
        });
    }
    function buildPressureChart(temperature){
        var temperature = new Chart(document.getElementById("pressure"), {
            type: "line",
            data: {
                labels: tableData.time,
                datasets: [{
                    label: "Pressure",
                    fill: true,
                    backgroundColor: "transparent",
                    borderColor: window.theme.primary,
                    data: tableData.pressure,
                }]
            },
            options: {
                maintainAspectRatio: false,
                legend: {
                    display: false
                },
                scales: {
                    yAxes: [{
                        gridLines: {
                            display: false
                        },
                        stacked: false,
                        ticks: {
                            stepSize: 20
                        }
                    }],
                    xAxes: [{
                        stacked: false,
                        gridLines: {
                            color: "transparent"
                        }
                    }]
                }
            }
        });
    }
    function buildMAGChart(temperature){
        var temperature = new Chart(document.getElementById("mag"), {
            type: "line",
            data: {
                labels: tableData.time,
                datasets: [{
                    label: "MAG X",
                    fill: true,
                    backgroundColor: "transparent",
                    borderColor: window.theme.primary,
                    data: tableData.magx,
                },
                {
                    label: "MAG Y",
                    fill: true,
                    backgroundColor: "transparent",
                    borderColor: window.theme.primary,
                    data: tableData.magy,
                },
                {
                    label: "MAG Z",
                    fill: true,
                    backgroundColor: "transparent",
                    borderColor: window.theme.primary,
                    data: tableData.magz,
                }]
            },
            options: {
                maintainAspectRatio: false,
                legend: {
                    display: false
                },
                scales: {
                    yAxes: [{
                        gridLines: {
                            display: false
                        },
                        stacked: false,
                        ticks: {
                            stepSize: 20
                        }
                    }],
                    xAxes: [{
                        stacked: false,
                        gridLines: {
                            color: "transparent"
                        }
                    }]
                }
            }
        });
    }

    
    var tableData;     
    var url = "/data";

    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
    if (xhr.readyState == 4) {
        tableData = JSON.parse(xhr.response);
        console.log(tableData)
        buildTemperatureChart(tableData)
        buildHumidityChart(tableData)
        buildPressureChart(tableData)
        buildMAGChart(tableData)
    }};
    xhr.open("GET", url);
    xhr.send();   
    
});