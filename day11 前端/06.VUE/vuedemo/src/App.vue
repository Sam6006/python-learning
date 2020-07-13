<template>
  <div id="app">
    <!--  router-view 是安装了vue-router以后提供的，会根据不同的url地址发生变化时，自动到路由列表中查找对应的组件显示内容出来  -->
    <router-view></router-view>
  </div>
</template>

<script>


export default {
  name: 'App',
  components: {


  }
}
</script>


<style>
  body{
    padding: 0;
    margin: 0;
  }

</style>
