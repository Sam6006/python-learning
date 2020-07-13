//导入vue 和vue-router组件
import Vue from "vue";
import Router from "vue-router";

//@表示一个路由，是src的所在路径

import Index from "@/components/Index";
import Main from "@/components/Main";
import Home from "@/components/Home";
import List from "@/components/List";
import Detail from "@/components/Detail";
import Table from "@/components/Table";



//注册vue-router到vue中
Vue.use(Router);

//编写路由列表
export default new Router({
  mode:"history", //路由模式， hash默认，把rul地址拼接到域名的#后面， history,使用html5的历史管理来切换路由地址
  routes:[
    {
      path: "/index",
      component:Index,
      name: "Index",
    },
    {
      path: "/main",
      component:Main,
      name: "Main",
    },
    {
      path: "/",
      component:Home,
      name: "Home",
    },
    {
      path: "/list/:page", //给目标地址添加page变量到url中
      component:List,
      name: "List",
    },
    {
      path: "/detail",
      component: Detail,
      name: "Detail",
    },
    {
      path: "/table",
      component: Table,
      name: "Table",
    },

  ]
})
