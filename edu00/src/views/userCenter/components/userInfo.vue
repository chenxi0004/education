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
  username: '',  // 添加用户名字段
  gender: null,  // 添加性别字段
  student_or_teacher_id: '',  // 添加学生/教师编号字段
  phonenumber:'',
  email:''
})

const userRef=ref(null)
form.value=props.user;

const rules=ref({
  username: [
    { required: true, message: "用户名不能为空", trigger: "blur" },
    { min: 2, max: 100, message: "用户名长度应在2到100之间", trigger: "blur" }
  ],
  gender: [
    { required: true, message: "请选择性别", trigger: "blur" }
  ],
  student_or_teacher_id: [
    { required: true, message: "学生/教师编号不能为空", trigger: "blur" },
    { pattern: /^[a-zA-Z0-9]+$/, message: "学生/教师编号只能包含字母和数字", trigger: "blur" }
  ],
  email:[{required:true,message:"邮箱地址不能为空",trigger:"blur"},{
    type:"email",
    message: "请输入正确的邮箱地址",
    trigger: ["blur","change"]
  }],
  phonenumber:[{required:true,message:"手机号码不能为空",trigger:"blur"},{
    pattern:/^1[3|4|5|6|7|8|9][0-9]\d{8}$/,
    message: "请输入正确的手机号码",
    trigger: "blur"
  }],
});

const handleSubmit=()=>{
  userRef.value.validate(async (valid)=>{
    if(valid){
      // let result=await requestUtil.post("user/save",form.value);
      const formData = form.value;
      let result = await axios.post("http://localhost:8000/user/save", formData, {
          headers: {
            'Content-Type': 'application/json'
          }
        });
      let data=result.data;
      if(data.code==200){
        ElMessage.success("操作成功!")
        window.sessionStorage.setItem("currentUser",JSON.stringify(form.value))
      }
    }
  })
}
</script>

<template>
  <el-form ref="userRef" :model="form" :rules="rules" label-width="100px">
    <el-form-item label="用户名：" prop="username">
      <el-input v-model="form.username" maxlength="100"/>
    </el-form-item>
    <el-form-item label="性别：" prop="gender">
      <el-select v-model="form.gender" placeholder="请选择性别">
        <el-option label="男" value="0"></el-option>
        <el-option label="女" value="1"></el-option>
        <el-option label="其他" value="2"></el-option>
      </el-select>
    </el-form-item>
    <el-form-item label="学生/教师编号：" prop="student_or_teacher_id">
      <el-input v-model="form.student_or_teacher_id" maxlength="20"/>
    </el-form-item>
    <el-form-item label="手机号码：" prop="phonenumber">
      <el-input v-model="form.phonenumber" maxlength="11"/>
    </el-form-item>
    <el-form-item label="用户邮箱：" prop="email">
      <el-input v-model="form.email" maxlength="50"/>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="handleSubmit">保存</el-button>

    </el-form-item>
  </el-form>
</template>

<style scoped lang="scss">

</style>