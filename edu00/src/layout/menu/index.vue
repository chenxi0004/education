<!--<script setup>-->
<!--</script>-->

<!--<template>-->
<!--<el-menu-->
<!--        active-text-color="#ffd04b"-->
<!--        background-color="#2d3a4b"-->
<!--        class="el-menu-vertical-demo"-->
<!--        text-color="#fff"-->
<!--        router-->
<!--        :default-active="'/index'"-->
<!--      >-->
<!--        <el-sub-menu index="1">-->
<!--          <template #title>-->
<!--            <el-icon><location /></el-icon>-->
<!--            <span>Navigator One</span>-->
<!--          </template>-->
<!--          <el-menu-item-group title="Group One">-->
<!--            <el-menu-item index="1-1">item one</el-menu-item>-->
<!--            <el-menu-item index="1-2">item two</el-menu-item>-->
<!--          </el-menu-item-group>-->
<!--          <el-menu-item-group title="Group Two">-->
<!--            <el-menu-item index="1-3">item three</el-menu-item>-->
<!--          </el-menu-item-group>-->
<!--          <el-sub-menu index="1-4">-->
<!--            <template #title>item four</template>-->
<!--            <el-menu-item index="1-4-1">item one</el-menu-item>-->
<!--          </el-sub-menu>-->
<!--        </el-sub-menu>-->
<!--        <el-menu-item index="2">-->
<!--          <el-icon><icon-menu /></el-icon>-->
<!--          <span>Navigator Two</span>-->
<!--        </el-menu-item>-->
<!--        <el-menu-item index="3" disabled>-->
<!--          <el-icon><document /></el-icon>-->
<!--          <span>Navigator Three</span>-->
<!--        </el-menu-item>-->
<!--        <el-menu-item index="4">-->
<!--          <el-icon><setting /></el-icon>-->
<!--          <span>Navigator Four</span>-->
<!--        </el-menu-item>-->
<!--      </el-menu>-->
<!--</template>-->

<!--<style lang="scss" scoped>-->
<!--</style>-->
<script setup>
import store from "@/store";
import {HomeFilled} from '@element-plus/icons-vue'
const menuList=JSON.parse(sessionStorage.getItem("menuList"))
const openTab=(item)=>{
  store.commit('ADD_TABS',item)
}
</script>

<template>
<el-menu
        active-text-color="#409eff"
        background-color="#f5f5f5"
        class="el-menu-vertical-demo"
        text-color="#333"
        router
        :default-active="'/index'"
      >


        <el-menu-item index="/index" @click="openTab({name:'首页',path:'/index'})">
          <el-icon>
            <HomeFilled/>
          </el-icon>
          <span>首页</span>
        </el-menu-item>

        <el-sub-menu :index="menu.path" v-for="menu in menuList">
          <template #title>
            <el-icon>
              <svg-icon :icon-class="menu.icon" />
            </el-icon>
            {{menu.name}}
          </template>
          <el-menu-item :index="item.path" v-for="item in menu.children" @click="openTab(item)">
            <el-icon>
              <svg-icon :icon-class="item.icon"/>
            </el-icon>
            {{item.name}}
          </el-menu-item>
        </el-sub-menu>
      </el-menu>
</template>

<style lang="scss" scoped>
.el-menu {
  border-right: none; /* 去掉右侧边框 */
  .el-icon {
    color: #666; /* 图标颜色（深灰色） */
    font-size: 18px; /* 图标大小 */
    margin-right: 8px; /* 图标与文字的间距 */
  }
}
</style>