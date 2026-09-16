const status=document.getElementById('status');
let chart;
if(typeof Chart!=='undefined')chart=new Chart(document.getElementById('chart'),{type:'line',data:{labels:[],datasets:[{label:'Temperature (°C)',data:[],borderColor:'#2859d9',yAxisID:'temperature',tension:.2},{label:'Humidity (%)',data:[],borderColor:'#16815d',yAxisID:'humidity',tension:.2}]},options:{animation:false,scales:{temperature:{position:'left'},humidity:{position:'right',grid:{drawOnChartArea:false}}}}});
const stream=new EventSource('/stream');
stream.onopen=()=>status.textContent='Live · one sample per second';
stream.onerror=()=>status.textContent='Disconnected. Retrying automatically…';
stream.onmessage=event=>{
  const data=JSON.parse(event.data);
  document.getElementById('temperature').textContent=`${data.temperature.toFixed(2)} °C`;
  document.getElementById('humidity').textContent=`${data.humidity.toFixed(2)} %`;
  document.getElementById('latest').textContent=`Last sample: ${new Date(data.timestamp).toLocaleTimeString()}`;
  if(chart){chart.data.labels.push(new Date(data.timestamp).toLocaleTimeString());chart.data.datasets[0].data.push(data.temperature);chart.data.datasets[1].data.push(data.humidity);if(chart.data.labels.length>60){chart.data.labels.shift();chart.data.datasets.forEach(dataset=>dataset.data.shift());}chart.update();}
};
