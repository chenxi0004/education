<script setup>
import {defineProps,ref} from "vue"
import requestUtil,{getServerUrl} from "@/util/request"
import {ElMessage} from "element-plus";
import {Plus} from '@element-plus/icons-vue'
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

const headers=ref({
  Authorization:window.sessionStorage.getItem('token')
})

const form=ref({
  id:-1,
  avatar:''
})

const formRef=ref(null)
const imageUrl=ref("")
form.value=props.user;
imageUrl.value=getServerUrl()+'media/userAvatar/'+form.value.avatar

const handleAvatarSuccess=(res)=>{
  imageUrl.value = getServerUrl() + 'media/userAvatar/' + res.title;
  form.value.avatar = res.title;
}

const beforeAvatarUpload=(file)=>{
  const isJPG=file.type === 'image/jpeg'
  const isLt4M=file.size/1024/1024<4
  if(!isJPG){
    ElMessage.error('图片必须是jpg格式！')
  }
  if(!isLt4M){
    ElMessage.error('图片大小不能超过4MB！')
  }
  return isJPG && isLt4M
}

const handleConfirm=async ()=>{
  // let result=await requestUtil.post("user/updateAvatar",form.value);
      const formData = form.value;
      let result = await axios.post("http://localhost:8000/user/updateAvatar", formData, {
          headers: {
            'Content-Type': 'application/json'
          }
        });
      let data=result.data;
      if(data.code==200){
        ElMessage.success("操作成功!")
        window.sessionStorage.setItem("currentUser",JSON.stringify(form.value))
      }else {
        ElMessage.error(data.errorInfo);
      }
}

</script>

<template>
  <el-form
  ref="formRef"
  :model="form"
  label-width="100px"
  style="text-align: center;padding-bottom: 10px">
    <el-upload name="avatar" :headers="headers"
    class="avatar-uploader"
    :action="getServerUrl()+'user/uploadImage'"
    :show-file-list="false"
    :before-upload="beforeAvatarUpload"
    :on-success="handleAvatarSuccess"

  >
    <img v-if="imageUrl" :src="imageUrl" class="avatar" />
    <el-icon v-else class="avatar-uploader-icon">
      <Plus />
    </el-icon>
    </el-upload>
    <el-button @click="handleConfirm">确认更换</el-button>
  </el-form>
</template>

<style scoped lang="scss">
.avatar-uploader {
  .avatar {
    width: 128px;
    height: 128px;
    object-fit: cover;  // 确保图片在容器内保持宽高比例
    border-radius: 50%;  // 可选：设置为圆形头像
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 128px;
    height: 128px;
    line-height: 128px;
    text-align: center;
    border: 1px dashed #d9d9d9;
    border-radius: 50%;  // 可选：设置为圆形头像
  }
}
</style>