<template>
    <div class="home">

        <Header></Header>
        {{message}}
        <span v-html="img" @click="show"></span>
        <button @click="num++">+</button>
        <input type="text" v-model="num">
        <button @click="num--">-</button>
        <Footer></Footer>
    </div>
</template>

<script>
    //引入子组件
    import Header from "./common/Header";
    import Footer from "./common/Footer";

    export default {
        name: "Home",
        data(){
            return{
                message:"Home组件",
                img:"<img src='/static/image/logo.png'>",
                num:0,
            }
        },
        methods:{
            show(){
                this.message='';
                console.log(this.$settings.web_title)
            }
        },
        //组件嵌套
        components:{
            Header,
            Footer,
        }
    }
</script>

//这里是组件中的注释部分
//scoped 表示当前stlye标签里编写的样式， 属性于局部样式
//它只能被当前组件中template的内容调用识别，不能级其他的组件使用
<style scoped>

</style>
