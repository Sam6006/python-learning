import Vue from "vue"
import VueX from "vuex"

Vue.use(Vuex);


export default new VueX.store({
  //this.$store.state.name
  state:{
    name: "sam"
  }
})
