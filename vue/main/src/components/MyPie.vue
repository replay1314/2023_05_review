<template>
  <div class="chart">

  </div>

</template>

<script>
export default {
  name: "MyPie",
  props: ['word', 'id', 'title'],
  data() {
    return {
      chart: null,
    }
  },
  mounted() {
    this.$axios.get(this.word).then(response => {
      let data = response.data.data
      let pie_data = []
      Object.keys(data).map((key) => {
        pie_data.push({name: key, value: data[key]})
      })
      let chart = document.getElementsByClassName('chart')[this.id];
      this.chart = echarts.init(chart)
      let options = {
        title: {text: this.title},
        label: {
          show: true,
          formatter: '{b} : {c}',
          fontSize: 12,
        },
        series: [{
          type: 'pie',
          data: pie_data
        }],
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