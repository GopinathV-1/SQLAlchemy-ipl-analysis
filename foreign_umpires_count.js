fetch("./foreign_umpires_count.json")
    .then(resp => resp.json())
    .then(data => {
        Highcharts.chart('container2', {
            chart: {
              type: 'column'
            },
            title: {
              text: 'Foreign umpires count in IPL'
            },
            subtitle: {
              text: 'Source:<a href="https://en.wikipedia.org/wiki/Indian_Premier_League">Wikipedia</a>'
            },
            xAxis: {
              type: 'category',
              labels: {
                rotation: -45,
                style: {
                  fontSize: '13px',
                  fontFamily: 'Verdana, sans-serif'
                }
              },
              title: {
                text: 'Umpires country'
              }
            },
            yAxis: {
              min: 0,
              title: {
                text: 'Count'
              }
            },
            legend: {
              enabled: false
            },
            tooltip: {
              pointFormat: 'Total count : <b>{point.y:.0f}</b>'
            },
            series: [{
              name: 'Team name',
              data: data.foreign_umpires_count,
              dataLabels: {
                enabled: true,
                rotation: -90,
                color: '#FFFFFF',
                align: 'right',
                format: '{point.y:.0f}', 
                y: 10, // 10 pixels down from the top
                style: {
                  fontSize: '13px',
                  fontFamily: 'Verdana, sans-serif'
                }
              }
            }]
          });
        })