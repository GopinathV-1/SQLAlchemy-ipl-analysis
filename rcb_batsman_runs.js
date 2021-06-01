fetch("./rcb_batsman_runs.json")
    .then(resp => resp.json())
    .then(data => {
        Highcharts.chart('container1', {
            chart: {
              type: 'column'
            },
            title: {
              text: 'Total runs scored by RCB batsman in IPL'
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
                text: 'Batsman name'
              }
            },
            yAxis: {
              min: 0,
              title: {
                text: 'Runs scored'
              }
            },
            legend: {
              enabled: false
            },
            tooltip: {
              pointFormat: 'Total runs : <b>{point.y:.0f}</b>'
            },
            series: [{
              name: 'Team name',
              data: data.rcb_batsman_runs,
              dataLabels: {
                verticalAlign: 'top',
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