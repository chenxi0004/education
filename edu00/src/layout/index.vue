

<template>
  <div class="app-wrapper">
    <el-container>
      <el-aside width="200px" class="sidebar-container"><Menu/></el-aside>
      <el-container>
        <el-header><Header/></el-header>
        <el-main><Tabs/><router-view/></el-main>
        <el-footer><Footer/></el-footer>
      </el-container>
    </el-container>
  </div>
</template>

<script setup>
import Menu from "@/layout/menu"
import Footer from "@/layout/footer"
import Header from "@/layout/header";
import Tabs from "@/layout/tabs"
</script>

<style scoped>
.app-wrapper{
  position: relative;
  width: 100%;
  height: 100%;
}
.sidebar-container{
  background-color: #CCEDFF;
  height: 100%;
}
.el-container{
  height: 100%;
}
.el-header{
  padding-left:0px ;
  padding-right:0px ;
}
:deep(ul.el-menu){
  boder-right-width:0px
}
</style>