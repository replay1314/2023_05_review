<template>
  <div class="chart">

  </div>

</template>

<script>
export default {
  name: "MyBar",
  props: ['word', 'id', 'title'],
  data() {
    return {
      chart: null,
    }
  },
  mounted() {
    this.$axios.get(this.word).then(response => {
      let data = response.data.data
      let chart = document.getElementsByClassName('chart')[this.id];
      this.chart = echarts.init(chart)
      let options = {
        title: {text: this.title},
        dataZoom: {
          type: 'inside'
        },
        tooltip: {
          trigger: 'axis',
          formatter: function (params) {
            return params[0].name + '<br>次数：' + params[0].data;
          }
        },
        xAxis: {data: Object.keys(data).splice(0, 10)},
        yAxis: {},
        series: [{
          type: 'bar',
          data: Object.values(data).splice(0, 10)
        }]
      }
      this.chart.setOption(options)
    }).catch(error => {
      console.log(error)
    })
  },
}
</script>


<style scoped>
.chart {
  width: 100%;
  height: 100%;
}

</style>