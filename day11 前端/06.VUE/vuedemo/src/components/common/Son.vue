<template>
  <div class="son">
    <p>子组件: num={{num}}</p>
    <input type="text" v-model="num">

  </div>

</template>

<script>
    export default {
        name: "Son",
        data(){

        },
        props:['num'],
        watch:{
            num(){
                //当num发生改变时，通知父组件
                this.$emit('change',this.num);
                return ;
            }
        }
    }
</script>

<style scoped>
.son{
  background-color: #eee;
}
</style>
