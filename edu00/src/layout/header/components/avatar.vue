

<template>

<el-dropdown>
    <span class="el-dropdown-link">
      <el-avatar shape="square" :size="40" :src="squareUrl" />
      &nbsp;&nbsp;{{currentUser.username}}
      <el-icon class="el-icon--right">
        <arrow-down />
      </el-icon>
    </span>
    <template #dropdown>
      <el-dropdown-menu>
        <el-dropdown-item>
          <router-link :to="{name:'个人中心'}">个人中心</router-link>
        </el-dropdown-item>
        <el-dropdown-item @click="logout">安全退出</el-dropdown-item>
<!--        <el-dropdown-item>Action 3</el-dropdown-item>-->
<!--        <el-dropdown-item disabled>Action 4</el-dropdown-item>-->
<!--        <el-dropdown-item divided>Action 5</el-dropdown-item>-->
      </el-dropdown-menu>
    </template>
  </el-dropdown>
</template>

<script setup>
import { ArrowDown } from '@element-plus/icons-vue'
import {ref} from "vue";

// import router from "@/router";
import requestUtil,{getServerUrl} from "@/util/request";
// import store from "@/store";

import { useStore } from 'vuex';
import { useRouter } from 'vue-router';

const store = useStore();
const router = useRouter();

// const currentUser=JSON.parse(sessionStorage.getItem("currentUser"))


const currentUser = JSON.parse(sessionStorage.getItem("currentUser") || "{}");
// const squareUrl=getServerUrl()+'media/userAvatar/'+currentUser.avatar
const serverUrl = getServerUrl();
// const squareUrl = `${serverUrl}media/userAvatar/${currentUser.avatar}`;


const squareUrl = `${serverUrl}media/userAvatar/${currentUser.avatar || "default.jpg"}`;
const logout=()=>{
  window.sessionStorage.clear()
  localStorage.clear(); // 清除访问 Token
  store.commit('RESET_TAB')

  store.dispatch('clearUser'); // 调用 clearUser action 清除用户信息
  store.dispatch('clearRole')

  router.replace("/login")
}
</script>

<style scoped lang="scss">
.el-dropdown-link{
  cursor: pointer;
  color: var(--el-color-primary);
  display: flex;
  align-items: center;
}
</style>