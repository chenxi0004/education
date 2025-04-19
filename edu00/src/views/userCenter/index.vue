<script setup>
import {ref} from "vue";
import avatar from "./components/avatar.vue"
import userInfo from "./components/userInfo.vue"
import resetPwd from "./components/resetPwd.vue"
const currentUser=JSON.parse(sessionStorage.getItem("currentUser"))
const activeTab=ref("userinfo");

</script>

<template>
<div class="app-container">
  <el-row :gutter="20">
    <el-col :span="6">
      <el-card class="box-card">
        <template v-slot:header>
          <div class="clearfix">
            <span>个人信息</span>
          </div>
        </template>
        <div>
          <div class="text-center">
            <avatar :user="currentUser"/>
          </div>
          <ul class="list-group list-group-striped">
            <li class="list-group-item">
              <svg-icon icon-class="user"/>&nbsp;&nbsp;用户名称
              <div class="pull-right">{{currentUser.username}}</div>
            </li>
            <li class="list-group-item">
              <svg-icon icon-class="user"/>&nbsp;&nbsp;性别
              <div class="pull-right">{{ currentUser.gender === 0 ? '男' : '女' }}</div>
            </li>
            <li class="list-group-item">
              <svg-icon icon-class="phone"/>&nbsp;&nbsp;手机号码
              <div class="pull-right">{{currentUser.phonenumber}}</div>
            </li>
            <li class="list-group-item">
              <svg-icon icon-class="email"/>&nbsp;&nbsp;用户邮箱
              <div class="pull-right">{{currentUser.email}}</div>
            </li>
            <li class="list-group-item">
              <svg-icon icon-class="peoples"/>&nbsp;&nbsp;所属角色
              <div class="pull-right">{{currentUser.roles}}</div>
            </li>
            <li class="list-group-item">
              <svg-icon icon-class="data"/>&nbsp;&nbsp;学生/教师编号
              <div class="pull-right">{{currentUser.student_or_teacher_id}}</div>
            </li>
            <li class="list-group-item">
              <svg-icon icon-class="date"/>&nbsp;&nbsp;创建日期
              <div class="pull-right">{{currentUser.login_date}}</div>
            </li>
          </ul>
        </div>
      </el-card>
    </el-col>
    <el-col :span="18">
      <el-card>
        <template v-slot:header>
          <div class="clearfix">
            <span>基本资料</span>
          </div>
        </template>
        <el-tabs v-model="activeTab">
          <el-tab-pane label="基本资料" name="userinfo">
            <userInfo :user="currentUser"/>
          </el-tab-pane>
          <el-tab-pane label="修改密码" name="resetPwd">
            <resetPwd :user="currentUser"/>
          </el-tab-pane>
        </el-tabs>
      </el-card>
    </el-col>
  </el-row>
</div>
</template>

<!--<style scoped lang="scss">-->
<!--.app-container {-->
<!--  padding: 20px;-->
<!--}-->

<!--.el-row {-->
<!--  margin-bottom: 20px;-->
<!--}-->

<!--.el-col {-->
<!--  margin-bottom: 20px;-->
<!--}-->

<!--.el-card {-->
<!--  .clearfix {-->
<!--    text-align: center;-->
<!--    font-size: 18px;-->
<!--    font-weight: bold;-->
<!--    color: #333;-->
<!--  }-->

<!--  .text-center {-->
<!--    text-align: center;-->
<!--    margin-bottom: 20px;-->
<!--  }-->

<!--  .list-group {-->
<!--    list-style: none;-->
<!--    padding: 0;-->
<!--    margin: 0;-->

<!--    .list-group-item {-->
<!--      display: flex;-->
<!--      align-items: center;-->
<!--      justify-content: space-between;-->
<!--      padding: 10px 0;-->
<!--      border-bottom: 1px solid #eee;-->

<!--      &:last-child {-->
<!--        border-bottom: none;-->
<!--      }-->

<!--      .svg-icon {-->
<!--        margin-right: 10px;-->
<!--      }-->

<!--      .pull-right {-->
<!--        text-align: right;-->
<!--        flex: 1;-->
<!--      }-->
<!--    }-->
<!--  }-->
<!--}-->

<!--.el-tabs {-->
<!--  margin-top: 20px;-->
<!--}-->
<!--</style>-->

<style scoped lang="scss">
.app-container {
  padding: 20px;
  display: flex;
  flex-direction: column;
}

.el-row {
  display: flex;
  flex-wrap: wrap;
  margin-bottom: 20px;
}

.el-col {
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
}

.el-card {
  flex: 1;
  display: flex;
  flex-direction: column;
  height: 100%;

  .clearfix {
    text-align: center;
    font-size: 18px;
    font-weight: bold;
    color: #333;
  }

  .text-center {
    text-align: center;
    margin-bottom: 20px;
  }

  .list-group {
    list-style: none;
    padding: 0;
    margin: 0;
    flex: 1;

    .list-group-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 10px 0;
      border-bottom: 1px solid #eee;

      &:last-child {
        border-bottom: none;
      }

      .svg-icon {
        margin-right: 10px;
      }

      .pull-right {
        text-align: right;
        flex: 1;
      }
    }
  }
}

.el-tabs {
  margin-top: 20px;
  flex: 1;
}
</style>