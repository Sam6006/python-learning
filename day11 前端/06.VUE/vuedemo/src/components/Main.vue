<template>
    <div class="main">
      <p>父组件：num={{num}}</p>
        <Son :num="num" @change="update_num" />
    </div>
</template>

<script>
    import Son from "./common/Son";
    export default {
        name: "Main",
        data(){
            return{
                num:0,

            }
        },
        methods:{
            update_num(data){
                this.num=data;
            }
        },
        components:{
            Son,
        }
    }
</script>

<style scoped>

</style>
