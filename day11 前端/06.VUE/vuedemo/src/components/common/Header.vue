<template>
    <div class="header">
      {{message}}
      <div class="mnu">
<!--          <a href="/index">index页面</a>-->
<!--          <a href="/main">Main页面</a>-->
        <router-link to="/index" >index页面</router-link>
        <router-link to="/main">Main页面</router-link>
        <router-link to="/list/3">跳转到列表页面</router-link>
        <router-link to="/list/3?id=3">跳转到列表页面</router-link>
        <router-link :to="{path:'/list/3', query:{id:100,username:'小明'}}">跳转到列表页面</router-link>

<!-- router-link标签只支持站内无刷新更换页面,但是如果要跳转到网站外部,例如别的网站时,还是得用a标签来完成. -->
        <a href="http://www.baidu.com">baidu</a>
        </div>
      {{title}}
    </div>
</template>

<script>
    export default {
        name: "Header",
        data(){
            return{
                message:'头部子组件的代码',
                title:'',
            }
        },
        created() {
            this.title=this.$settings.web_title;

        }
    }
</script>

<style scoped>

</style>
