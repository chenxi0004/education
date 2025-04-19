<template>
  <div class="login">
    <el-form ref="loginRef":model="loginForm":rules="loginRules" class="login-form">
      <h3 class="title">Django在线教育服务平台</h3>
      <el-form-item prop="username">
        <el-input
            v-model="loginForm.username"
            type="text"
            size="large"
            auto-complete="off"
            placeholder="账号"
        >
<!--          <template #prefix><svg-icon icon="user"/></template>-->
          <template #prefix><svg-icon icon-class="user"/></template>
        </el-input>
      </el-form-item>
      <el-form-item prop="password">
        <el-input
          v-model="loginForm.password"
          type="password"
          size="large"
          auto-complete="off"
          placeholder="密码"
        >
          <template #prefix><svg-icon icon-class="password"/></template>
        </el-input>
      </el-form-item>
      <el-checkbox v-model="loginForm.rememberMe" style="margin: 0px 0px 25px 0px;">记住密码</el-checkbox>
      <el-form-item style="width: 100%;">
        <el-button
            size="large"
            type="primary"
            style="width: 100%;"
            @click.prevent="handleLogin"
        >
          <span>登录</span>
        </el-button>
      </el-form-item>
    </el-form>
    <div class="el-login-footer">
      <span>没有账号？<router-link to="/register">立即注册</router-link></span>
<!--      <span>Copyright @2021-2025<a href="http://localhost:8080" target="_blank">local.com</a>版权所有</span>-->
    </div>
  </div>
</template>

<script setup>

// import { ref } from 'vue';
// import { ElMessage } from 'element-plus';
// import requestUtil from '@/util/request'
// import Cookies from "js-cookie"
// import {encrypt,decrypt} from "@/util/jsencrypt";
// import qs from 'qs'
// import router from "@/router";
// import axios from "axios";
// // // 设置 axios 的默认头部
// // axios.defaults.headers.common["Authorization"] = `Bearer ${sessionStorage.getItem("token")}`;
//
//
//
// const loginForm = ref({
//   username:'',
//   password:'',
//   rememberMe:false
// })
// const loginRules={
//   username:[{required:true,trigger:'blur',message:"请输入您的账号"}],
//   password:[{required:true,trigger:'blur',message:"请输入您的密码"}]
// }
// const loginRef = ref(null);
// // const username = ref('');
// // const password = ref('');
//
// const handleLogin = () => {
//   loginRef.value.validate (async (valid)=>{
//     if (valid){
//       // const formData=qs.stringify(loginForm.value)
//       // let result=await axios.post("http://localhost:8000/user/login?"+formData,{
//       //   timeout: 10000, // 设置超时时间为 10000ms
//       // })
//       let result=await requestUtil.post("user/login?"+qs.stringify(loginForm.value))
//       // const formData=qs.stringify(loginForm.value)
//       // const result = await requestUtil.post(`user/login?${formData}`);
//       let data=result.data
//       if (data.code==200){
//         ElMessage.success(data.info)
//         window.sessionStorage.setItem("token",data.token)
//         const currentUser=data.user
//         currentUser.roles=data.roles
//         window.sessionStorage.setItem("currentUser",JSON.stringify(currentUser))
//         // window.sessionStorage.setItem("currentUser",JSON.stringify(data.user))
//         window.sessionStorage.setItem("menuList",JSON.stringify(data.menuList))
//         //勾选记住密码设置在cookie中设置记住用户名和密码
//         if(loginForm.value.rememberMe){
//           Cookies.set("username",loginForm.value.username,{expires:30});
//           Cookies.set("password",loginForm.value.password,{expires:30});
//           // Cookies.set("password",encrypt(loginForm.value.password),{expires:30});
//           Cookies.set("rememberMe",loginForm.value.rememberMe,{expires:30});
//         }else {
//           Cookies.remove("username");
//           Cookies.remove("password");
//           Cookies.remove("rememberMe");
//         }
//           router.replace("/")
//       }else {
//         ElMessage.error((data.info))
//       }
//     }else {
//       console.log("验证失败")
//     }
//   })
// }
// function getCookie(){
//   const username=Cookies.get("username");
//   const password=Cookies.get("password");
//   const rememberMe=Cookies.get("rememberMe");
//   loginForm.value={
//     username: username===undefined?loginForm.value.username:username,
//     password: password===undefined?loginForm.value.password:password,
//     // password: password===undefined?loginForm.value.password:decrypt(password),
//     rememberMe: rememberMe===undefined?false:Boolean(rememberMe)
//   };
//   // 确保密码字段被正确赋值
//   // console.log("Decrypted Password:", loginForm.value.password);
// }
// getCookie();
//   // if (!username.value || !password.value) {
//   //   ElMessage.error('请输入账号和密码');
//   // }
//   // // 这里可以添加登录逻辑，例如发送请求到后端
//   // ElMessage.success('登录成功');


import { ref } from 'vue';
import { ElMessage } from 'element-plus';
import requestUtil from '@/util/request';
import Cookies from "js-cookie";
import qs from 'qs';
// import router from "@/router";



import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
// vuex存储用户信息
const store = useStore();
const router = useRouter();


const loginForm = ref({
  username: '',
  password: '',
  rememberMe: false
});

const loginRules = {
  username: [{ required: true, trigger: 'blur', message: "请输入您的账号" }],
  password: [{ required: true, trigger: 'blur', message: "请输入您的密码" }]
};

const loginRef = ref(null);

const handleLogin = () => {
  loginRef.value.validate(async (valid) => {
    if (valid) {
      let result = await requestUtil.post("user/login?" + qs.stringify(loginForm.value));
      let data = result.data;
      if (data.code == 200) {
        ElMessage.success(data.info);
        window.sessionStorage.setItem("token", data.token);
        window.sessionStorage.setItem("refresh", data.refresh);  // 保存refresh令牌
        localStorage.setItem('access_token', data.token); // 保存访问 Token
        localStorage.setItem('refresh_token', data.refresh); // 保存刷新 Token
        window.sessionStorage.setItem("currentUser", JSON.stringify(data.user));
        window.sessionStorage.setItem("menuList", JSON.stringify(data.menuList));
        window.sessionStorage.setItem("roles", data.roles); // 保存访问 Token

        // 保存用户信息到 Vuex
        store.dispatch('setUser', data.user);
        store.dispatch('setRole', data.roles);
        // store.commit('SET_USER', data.user); // 将用户信息保存到 Vuex

        if (loginForm.value.rememberMe) {
          Cookies.set("username", loginForm.value.username, { expires: 30 });
          Cookies.set("password", loginForm.value.password, { expires: 30 });
          Cookies.set("rememberMe", loginForm.value.rememberMe, { expires: 30 });
        } else {
          Cookies.remove("username");
          Cookies.remove("password");
          Cookies.remove("rememberMe");
        }
        router.replace("/");
      } else {
        ElMessage.error(data.info);
      }
    } else {
      console.log("验证失败");
    }
  });
};

function getCookie() {
  const username = Cookies.get("username");
  const password = Cookies.get("password");
  const rememberMe = Cookies.get("rememberMe");
  loginForm.value = {
    username: username === undefined ? loginForm.value.username : username,
    password: password === undefined ? loginForm.value.password : password,
    rememberMe: rememberMe === undefined ? false : Boolean(rememberMe)
  };
}
getCookie();


</script>

<style lang="scss" scoped>
a{
  color: white;
}
.login {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  background-image: url("../assets/styles/01.png");
  background-size: cover;
}

.login-form {
  border-radius: 6px;
  background: #ffffff;
  width: 400px;
  //box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  padding: 25px 25px 5px 25px;
  .el-input{
    height: 40px;
    input{
      display: inline-block;
      height: 40px;
    }
  }
  .input-icon{
    height: 39px;
    width:14px;
    margin-left: 0px;
  }
}
.login-tip{
  font-size: 13px;
  text-align: center;
  color: #bfbfbf;
}
.login-code{
  width: 33%;
  height: 40px;
  float: right;
  img{
    cursor: pointer;
    vertical-align: middle;
  }
}
.title {
  text-align: center;
  margin: 0px auto 30px auto;
  color: #707070;
}

.el-login-footer {
  height: 40px;
  line-height: 40px;
  position: fixed;
  bottom: 0;
  text-align: center;
  margin-top: 20px;
  color: #999;
}
</style>