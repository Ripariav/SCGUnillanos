document.addEventListener('DOMContentLoaded', function() {
    // Verifica que los elementos existan
    console.log(document.getElementById('bar-chart')); // Debería mostrar el elemento
    console.log(document.getElementById('line-chart')); // Debería mostrar el elemento
    console.log(document.getElementById('pie-chart')); // Debería mostrar el elemento

    // Obtén los datos del contexto de Django
    var barData = JSON.parse(document.getElementById('bar-data').textContent);
    var lineData = JSON.parse(document.getElementById('line-data').textContent);
    var pieData = JSON.parse(document.getElementById('pie-data').textContent);
  
    console.log('Bar Data:', barData); // Verifica los datos de barras
    console.log('Line Data:', lineData); // Verifica los datos de líneas
    console.log('Pie Data:', pieData); // Verifica los datos de pastel
  
    // Configuración y renderizado del gráfico de barras
    var barChart = echarts.init(document.getElementById('bar-chart'));
    var barOption = {
      title: {
        text: 'Contratos por Tipo'
      },
      xAxis: {
        type: 'category',
        data: barData.labels
      },
      yAxis: {
        type: 'value'
      },
      series: [{
        data: barData.data,
        type: 'bar'
      }]
    };
    barChart.setOption(barOption);
  
    // Configuración y renderizado del gráfico de líneas
    var lineChart = echarts.init(document.getElementById('line-chart'));
    var lineOption = {
      title: {
        text: 'Contratos Completados por Día'
      },
      xAxis: {
        type: 'category',
        data: lineData.labels
      },
      yAxis: {
        type: 'value'
      },
      series: [{
        data: lineData.completed,
        type: 'line'
      }]
    };
    lineChart.setOption(lineOption);
  
    // Configuración y renderizado del gráfico de pastel
    var pieChart = echarts.init(document.getElementById('pie-chart'));
    var pieOption = {
      tooltip: {
        trigger: 'item'
      },
      legend: {
        orient: 'vertical',
        left: 'left'
      },
      series: [{
        name: 'Estado de Contratos',
        type: 'pie',
        radius: '50%',
        data: pieData,
        emphasis: {
          itemStyle: {
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowColor: 'rgba(0, 0, 0, 0.5)'
          }
        }
      }]
    };
    pieChart.setOption(pieOption);
});
