fetch("./matches_by_season.json")
    .then(resp => resp.json())
    .then(data => {
        Highcharts.chart('container3', {
            chart: {
              type: 'column'
            },
            title: {
              text: 'Matches played by team by season in IPL'
            },
            xAxis: {
              categories: data.season, 
              title: {
                text: 'Season'
              }
            },
            yAxis: {
              min: 0,
              title: {
                text: 'Total matches played'
              },
              stackLabels: {
                enabled: true,
                style: {
                  fontWeight: 'bold',
                  color: ( // theme
                    Highcharts.defaultOptions.title.style &&
                    Highcharts.defaultOptions.title.style.color
                  ) || 'gray'
                }
              }
            },
            legend: {
              align: 'right',
              x: -30,
              verticalAlign: 'top',
              y: 25,
              floating: true,
              backgroundColor:
                Highcharts.defaultOptions.legend.backgroundColor || 'white',
              borderColor: '#CCC',
              borderWidth: 1,
              shadow: false
            },
            tooltip: {
              headerFormat: '<b>{point.x}</b><br/>',
              pointFormat: '{series.name}: {point.y}<br/>Total: {point.stackTotal}'
            },
            plotOptions: {
              column: {
                stacking: 'normal',
                dataLabels: {
                  enabled: true
                }
              }
            },
            series: [{
              name: 'SH',
              data: data.SH
            }, {
              name: 'RCB',
              data: data.RCB
            }, {
              name: 'MI',
              data: data.MI
            }, {
                name: 'RPS',
                data: data.RPS
            }, {
                name: 'GL',
                data: data.GL
            }, {
                name: 'KKR',
                data: data.KKR
            }, {
                name: 'KXP',
                data: data.KXP
            }, {
                name: 'DD',
                data: data.DD
            }, {
                name: 'CSK',
                data: data.CSK
            }, {
                name: 'RR',
                data: data.RR
            }, {
                name: 'DC',
                data: data.DC
            }, {
                name: 'KTK',
                data: data.KTK
            }, {
                name: 'PW',
                data: data.PW
            }]
        });
    })