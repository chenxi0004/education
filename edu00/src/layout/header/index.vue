<script setup>
import Breadcrumb from "@/layout/header/components/breadcrumb.vue";
import Avatar from "@/layout/header/components/avatar.vue";
import AboutView from "@/views/AboutView.vue";
</script>

<template>
  <div class="navbar">
    <Breadcrumb/>
    <div class="navbar-right">
      <Avatar/>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.navbar {
  width: 100%;
  height: 60px;
  overflow: hidden;
  background-color: #42b983;
  box-shadow: 0 1px 4px rgba(0, 21, 41, 0.08);
  padding: 0 16px;
  display: flex;
  align-items: center;
  box-sizing: border-box;
  position: relative;

  .navbar-right {
    flex: 1; // 占据剩余空间
    display: flex;
    align-items: center;
    justify-content: flex-end; // 对齐到末尾

    :deep(.navbar-item) {
      display: inline-block;
      margin-left: 18px; // 子元素之间的间距
      font-size: 22px;
      color: #5e5e66;
      box-sizing: border-box;
      cursor: pointer;
    }
  }
}
</style>