<template>
    <div class="list">
        <p>列表页</p>
    </div>
</template>

<script>
    export default {
        name: "List",
        created() {
            //接受参数
            console.log(this.$route.params.page);
            console.log(this.$route.params.id);

            //接收查询字符串参数
            console.log(this.$route.query.id);
            console.log(this.$route.query.username)

            //跳转页面到  /index
            //this.$router.push('/index'); //跳转到指定页面
            //this.$router.go(-1);

            //location.href='外网地址'
        }
    }
</script>

<style scoped>

</style>
