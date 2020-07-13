<template>
    <div class="box">
      <button @click="get_data">执行ajax</button>
      <ul v-for="item in weather.data.forecast">
        <li>{{item.date}}==={{item.high}}==={{item.low}}</li>
      </ul>
    </div>
</template>

<script>
    export default {
        name: "Detail",
        data(){
            return{
                city: '深圳',
                weather:{
                    data:{
                        forecast:[]
                    }
                },

            }
        },
        methods:{
            get_data(){
                //获取指定地区城市的天气
                this.$axios.get(`http://wthrcdn.etouch.cn/weather_mini?city=${this.city}`).then(response=>{
                    this.weather = response.data;
                    console.log(response.data)
                }).catch(error=>{
                    console.log(error.response)

                })

            }
        }
    }
</script>

<style scoped>

</style>
