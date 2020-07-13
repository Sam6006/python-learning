<template>
  <div class="index">
      {{message}}<br>
    <input type="text" v-model="message">
      <!-- 父传子   -->
    <Common title="Hello" :msg="message"  :goods_list="goods_list"/>


  </div>
</template>

<script>
    import Common from "./common/Common";
    export default {
        name: "Index",
        data(){
            return{
                message:'Hello Vue',
                goods_list:[
                    {"id":1, "title": "图书标题1"},
                    {"id":2, "title": "图书标题2"},
                    {"id":3, "title": "图书标题3"},
                    {"id":4, "title": "图书标题4"},
                ]
            }
        },
        methods:{

        },
        components:{
            Common,
        }
    }
</script>

<style scoped>

</style>
