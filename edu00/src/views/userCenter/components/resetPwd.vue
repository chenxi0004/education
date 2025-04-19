<script setup>
import {ref,defineProps} from "vue";
import requestUtil from "@/util/request"
import {ElMessage} from "element-plus";
import axios from "axios";
import qs from "qs";
// // 设置 Axios 请求拦截器
// axios.interceptors.request.use(config => {
//     const token = localStorage.getItem('access_token');
//     if (token) {
//         config.headers['Authorization'] = `Bearer ${token}`;
//     }
//     return config;
// }, error => {
//     return Promise.reject(error);
// });
//
// // 设置 Axios 响应拦截器
// axios.interceptors.response.use(response => {
//     return response;
// }, error => {
//     const originalRequest = error.config;
//     if (error.response.status === 401 && !originalRequest._retry) {
//         originalRequest._retry = true;
//         const refreshToken = localStorage.getItem('refresh_token');
//         return axios.post('http://localhost:8000/user/token/refresh/', {
//             refresh: refreshToken
//         }).then(response => {
//             const { access } = response.data;
//             localStorage.setItem('access_token', access);
//             axios.defaults.headers.common['Authorization'] = `Bearer ${access}`;
//             return axios(originalRequest);
//         }).catch(error => {
//             ElMessage.error('Token 刷新失败，请重新登录。');
//             return Promise.reject(error);
//         });
//     }
//     return Promise.reject(error);
// });

const props=defineProps({
  user:{
    type:Object,
    default:()=>{

    },required:true
  }
})

const form=ref({
  id:-1,
  oldPassword:'',
  newPassword:'',
  confirmPassword:''
})

const pwdRef=ref(null)
form.value=props.user;

// 自定义验证器：密码必须包含大小写字母、数字或特殊字符
const validatePassword = (rule, value, callback) => {
  const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,20}$/;
  if (!passwordRegex.test(value)) {
    callback(new Error('密码必须包含大小写字母、数字和特殊字符、长度在6到20个字符'));
  } else {
    callback();
  }
};

const equalToPassword=(rule,value,callback)=>{
  if(form.value.newPassword!==value){
    callback(new Error("两次输入的密码不一致"));
  }else {
    callback();
  }
};

const rules=ref({
  oldPassword:[{required:true,message:"旧密码不能为空",trigger:"blur"}],
  newPassword:[{required:true,message:"新密码不能为空",trigger:"blur"},{
    min:6,
    max:20,
    message: "长度在6到20个字符",
    // // 其他验证规则
    // validator: validatePassword,
    trigger: "blur"
  }],
  confirmPassword:[{required:true,message:"确认密码不能为空",trigger:"blur"},{
  required: true,
  validator:equalToPassword,
  trigger: "blur"
  }],
});

const handleSubmit=()=>{
  pwdRef.value.validate(async (valid)=>{
    if(valid){
      // let result=await requestUtil.post("user/save",form.value);
      const formData = form.value;
      let result = await axios.post("http://localhost:8000/user/updateUserPwd", formData, {
          headers: {
            'Content-Type': 'application/json'
          }
        });
      let data=result.data;
      if(data.code==200){
        ElMessage.success("修改密码操作成功,重新登录时请采用新密码!")
        // window.sessionStorage.setItem("currentUser",JSON.stringify(form.value))
      }else {
        ElMessage.error(data.errorInfo)
      }
    }
  })
}
</script>

<template>
    <el-form ref="pwdRef" :model="form" :rules="rules" label-width="80px">
    <el-form-item label="旧密码：" prop="oldPassword">
      <el-input v-model="form.oldPassword" placeholder="请输入旧密码" type="password" show-password/>
    </el-form-item>
    <el-form-item label="新密码：" prop="newPassword">
      <el-input v-model="form.newPassword" placeholder="请输入新密码" type="password" show-password/>
    </el-form-item>
    <el-form-item label="确认密码：" prop="confirmPassword">
      <el-input v-model="form.confirmPassword" placeholder="请确认密码" type="password" show-password/>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="handleSubmit">保存</el-button>

    </el-form-item>
  </el-form>
</template>

<style scoped lang="scss">

</style>