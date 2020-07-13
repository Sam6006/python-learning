<template>
    <div class="cmm">
        <p>Common的内容</p>
        <h1>{{title}}</h1>
        {{msg}}<br>
      <input type="text" v-model="msg">
        <ul>
          <li v-for="good in  goods_list">{{good.id}}===>{{good.title}}</li>
        </ul>
    </div>
</template>

<script>

    export default {
        name: "Common",
        props:['title', 'msg','goods_list'], //父传子组件数据传递 props
        data(){
            return{

            }
        }
    }
</script>

<style scoped>

</style>
