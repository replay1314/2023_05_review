<template>
  <div id="app">
    <h1 style="">豆瓣电影Top100数据分析</h1>
<!--    <div class="op">-->
<!--      后续更新-->
<!--    </div>-->
    <div class="box box1">
      <MyBar word="country" id="0" title="国家top10"/>
    </div>
    <div class="box box2">
      <MyLine word="year" id="1" title="年趋势图"/>
    </div>
    <div class="box box3">
      <MyPie word="type" id="2" title="类型分布图"/>
    </div>
    <div class="box box4">
      <MyBar word="author" id="3" title="导演top10"/>
    </div>
  </div>
</template>

<script>
import MyLine from "@/components/MyLine";
import MyPie from "@/components/MyPie";
import MyBar from "@/components/MyBar";

export default {
  name: 'App',
  components: {
    MyLine, MyPie, MyBar
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  position: relative;
}

.op {
  width: 200px;
  height: 50px;
  border: 1px solid black;
  position: absolute;
  right: 10px;
  top: 40px;
}

.box {
  width: 800px;
  height: 400px;
}

.box1 {
  border: 1px solid black;
  position: absolute;
  left: 100px;
  top: 100px;
}

.box2 {
  border: 1px solid black;
  position: absolute;
  left: 1000px;
  top: 100px;
}

.box3 {
  border: 1px solid black;
  position: absolute;
  left: 100px;
  top: 520px;
}

.box4 {
  border: 1px solid black;
  position: absolute;
  left: 1000px;
  top: 520px;
}
</style>
