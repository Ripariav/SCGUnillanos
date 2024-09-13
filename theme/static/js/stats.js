// Gráfico de barras (tareas completadas por día)
var barChart = echarts.init(document.getElementById('barChart'));
var barOption = {
  title: { text: 'Tareas Completadas (Semana)', left: 'center' },
  xAxis: {
    type: 'category',
    data: ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
  },
  yAxis: { type: 'value' },
  series: [{
    data: [5, 3, 8, 2, 7, 4, 6],  // Datos de ejemplo
    type: 'bar'
  }]
};
barChart.setOption(barOption);

// Gráfico de líneas (evolución mensual)
var lineChart = echarts.init(document.getElementById('lineChart'));
var lineOption = {
  title: { text: 'Evolución de Tareas (Mes)', left: 'center' },
  xAxis: { type: 'category', data: ['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4'] },
  yAxis: { type: 'value' },
  series: [{
    data: [12, 18, 10, 22],  // Datos de ejemplo
    type: 'line'
  }]
};
lineChart.setOption(lineOption);

// Gráfico circular (estado de las tareas)
var pieChart = echarts.init(document.getElementById('pieChart'));
var pieOption = {
  title: { text: 'Estado de las Tareas', left: 'center' },
  series: [{
    type: 'pie',
    data: [
      { value: 40, name: 'Pendiente' },
      { value: 30, name: 'En progreso' },
      { value: 30, name: 'Completado' }
    ]
  }]
};
pieChart.setOption(pieOption);