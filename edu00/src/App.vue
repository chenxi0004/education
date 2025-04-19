<template>
<!--  <nav>-->
<!--    <router-link to="/">Home</router-link> |-->
<!--    <router-link to="/about">About</router-link>-->
<!--  </nav>-->
  <router-view/>
</template>
<script setup>
import {watch} from "vue";
import {useRoute} from "vue-router";
import store from "@/store";
const route=useRoute()
watch(route,(to,from)=>{
  console.log(to.name,to.path)
  if(to.name=='个人中心'){
    let obj={
      name:to.name,
      path:to.path
    }
    store.commit('ADD_TABS',obj)
  }
},{deep:true,immediate:true})
</script>
<style>
html,body,#app{
  height: 100%;
}
.app-container{
  padding: 20px;
}


</style>
<!--#app {-->
<!--  font-family: Avenir, Helvetica, Arial, sans-serif;-->
<!--  -webkit-font-smoothing: antialiased;-->
<!--  -moz-osx-font-smoothing: grayscale;-->
<!--  text-align: center;-->
<!--  color: #2c3e50;-->
<!--}-->

<!--nav {-->
<!--  padding: 30px;-->
<!--}-->

<!--nav a {-->
<!--  font-weight: bold;-->
<!--  color: #2c3e50;-->
<!--}-->

<!--nav a.router-link-exact-active {-->
<!--  color: #42b983;-->
<!--}-->