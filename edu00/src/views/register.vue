
<!--<template>-->
<!--  <div class="register">-->
<!--    <el-form ref="registerRef" :model="registerForm" :rules="registerRules" class="register-form">-->
<!--      <h3 class="title">Django在线教育服务平台</h3>-->
<!--      <el-form-item prop="username">-->
<!--        <el-input-->
<!--            v-model="registerForm.username"-->
<!--            type="text"-->
<!--            size="large"-->
<!--            auto-complete="off"-->
<!--            placeholder="账号"-->
<!--        ></el-input>-->
<!--      </el-form-item>-->
<!--      <el-form-item prop="password">-->
<!--        <el-input-->
<!--          v-model="registerForm.password"-->
<!--          type="password"-->
<!--          size="large"-->
<!--          auto-complete="off"-->
<!--          placeholder="密码"-->
<!--        >-->
<!--        </el-input>-->
<!--      </el-form-item>-->
<!--      <el-form-item prop="confirmPassword">-->
<!--        <el-input-->
<!--          v-model="registerForm.confirmPassword"-->
<!--          type="password"-->
<!--          size="large"-->
<!--          auto-complete="off"-->
<!--          placeholder="确认密码"-->
<!--        >-->
<!--        </el-input>-->
<!--      </el-form-item>-->
<!--      <el-form-item style="width: 100%;">-->
<!--        <el-button-->
<!--            size="large"-->
<!--            type="primary"-->
<!--            style="width: 100%;"-->
<!--            @click.prevent="handleRegister"-->
<!--        >-->
<!--          <span>注册</span>-->
<!--        </el-button>-->
<!--      </el-form-item>-->
<!--    </el-form>-->
<!--    <div class="el-register-footer">-->
<!--      <span>已有账号？<router-link to="/login">立即登录</router-link></span>-->
<!--      <span>Copyright @2021-2025<a href="http://localhost:8080" target="_blank">local.com</a>版权所有</span>-->
<!--    </div>-->
<!--  </div>-->
<!--</template>-->
<!--<script setup>-->
<!--import { ref } from 'vue';-->
<!--import { ElMessage } from 'element-plus';-->
<!--import requestUtil from '@/util/request';-->
<!--import qs from 'qs';-->
<!--import axios from "axios";-->

<!--const registerForm = ref({-->
<!--  username: '',-->
<!--  password: '',-->
<!--  confirmPassword: ''-->
<!--});-->

<!--const validateConfirmPassword = (rule, value, callback) => {-->
<!--  if (value !== registerForm.value.password) {-->
<!--    callback(new Error('两次输入的密码不一致'));-->
<!--  } else {-->
<!--    callback();-->
<!--  }-->
<!--};-->

<!--const registerRules = {-->
<!--  username: [-->
<!--    { required: true, trigger: 'blur', message: '请输入您的账号' }-->
<!--  ],-->
<!--  password: [-->
<!--    { required: true, trigger: 'blur', message: '请输入您的密码' }-->
<!--  ],-->
<!--  confirmPassword: [-->
<!--    { required: true, trigger: 'blur', message: '请确认您的密码' },-->
<!--    { validator: validateConfirmPassword, trigger: 'blur' }-->
<!--  ]-->
<!--};-->

<!--const registerRef = ref(null);-->


<!--const handleRegister = () => {-->
<!--  registerRef.value.validate(async (valid) => {-->
<!--    if (valid) {-->
<!--      try {-->
<!--        // // 将响应式对象转换为普通对象-->
<!--        // const plainFormData = JSON.parse(JSON.stringify(registerForm.value));-->
<!--        // const formData = qs.stringify(plainFormData);-->
<!--        //-->
<!--        // console.log('FormData:', plainFormData);-->
<!--        // console.log('Serialized Data:', formData);-->
<!--        // 将表单数据序列化为 URL 编码格式-->
<!--        // const formData = registerForm.value;-->
<!--        const formData = qs.stringify(registerForm.value);-->
<!--        // 发送 POST 请求，将 formData 作为请求体发送-->
<!--        // let result = await requestUtil.post("/user/register",formData,{-->
<!--        // let result = await requestUtil.post("user/register?",qs.stringify(registerForm.value));-->
<!--        // let result = await requestUtil.post("/user/register", formData,{-->
<!--        let result = await axios.post("http://localhost:8000/user/register", formData, {-->
<!--          headers: {-->
<!--            'Content-Type': 'application/x-www-form-urlencoded'-->
<!--          }-->
<!--        });-->
<!--        let data = result.data;-->
<!--        if (data.code === 200) {-->
<!--          ElMessage.success(data.info);-->
<!--        } else {-->
<!--          ElMessage.error(data.info);-->
<!--        }-->
<!--      } catch (error) {-->
<!--        ElMessage.error('注册失败');-->
<!--      }-->
<!--    } else {-->
<!--      ElMessage.error('表单验证失败');-->
<!--    }-->
<!--  });-->
<!--};-->
<!--</script>-->


<!--<style lang="scss" scoped>-->
<!--a {-->
<!--  color: white;-->
<!--}-->
<!--.register {-->
<!--  display: flex;-->
<!--  justify-content: center;-->
<!--  align-items: center;-->
<!--  height: 100%;-->
<!--  background-image: url("../assets/styles/background01.png");-->
<!--  background-size: cover;-->
<!--}-->

<!--.register-form {-->
<!--  border-radius: 6px;-->
<!--  background: #ffffff;-->
<!--  width: 400px;-->
<!--  padding: 25px 25px 5px 25px;-->
<!--  .el-input {-->
<!--    height: 40px;-->
<!--    input {-->
<!--      display: inline-block;-->
<!--      height: 40px;-->
<!--    }-->
<!--  }-->
<!--}-->

<!--.title {-->
<!--  text-align: center;-->
<!--  margin: 0px auto 30px auto;-->
<!--  color: #707070;-->
<!--}-->

<!--.el-register-footer {-->
<!--  height: 40px;-->
<!--  line-height: 40px;-->
<!--  position: fixed;-->
<!--  bottom: 0;-->
<!--  text-align: center;-->
<!--  margin-top: 20px;-->
<!--  color: #999;-->
<!--}-->
<!--</style>-->












<template>
  <div class="register">
    <el-form ref="registerRef" :model="registerForm" :rules="registerRules" class="register-form">
      <h3 class="title">Django在线教育服务平台</h3>
      <el-form-item prop="username">
        <el-input
            v-model="registerForm.username"
            type="text"
            size="large"
            auto-complete="off"
            placeholder="账号"
        ></el-input>
      </el-form-item>
      <el-form-item prop="password">
        <el-input
          v-model="registerForm.password"
          type="password"
          size="large"
          auto-complete="off"
          placeholder="密码"
        >
        </el-input>
      </el-form-item>
      <el-form-item prop="confirmPassword">
        <el-input
          v-model="registerForm.confirmPassword"
          type="password"
          size="large"
          auto-complete="off"
          placeholder="确认密码"
        >
        </el-input>
      </el-form-item>
      <el-form-item prop="email">
        <el-input
            v-model="registerForm.email"
            type="text"
            size="large"
            auto-complete="off"
            placeholder="邮箱"
        ></el-input>
      </el-form-item>
      <el-form-item style="width: 100%;">
        <el-button
            size="large"
            type="primary"
            style="width: 100%;"
            @click.prevent="handleRegister"
        >
          <span>注册</span>
        </el-button>
      </el-form-item>
    </el-form>
    <div class="el-register-footer">
      <span>已有账号？<router-link to="/login">立即登录</router-link></span>
<!--      <span>Copyright @2021-2025<a href="http://localhost:8080" target="_blank">local.com</a>版权所有</span>-->
    </div>
  </div>
</template>
<script setup>
import { ref } from 'vue';
import { ElMessage } from 'element-plus';
import requestUtil from '@/util/request';
import qs from 'qs';
import axios from "axios";

const registerForm = ref({
  username: '',
  password: '',
  confirmPassword: '',
  email:'',
});

const validateConfirmPassword = (rule, value, callback) => {
  if (value !== registerForm.value.password) {
    callback(new Error('两次输入的密码不一致'));
  } else {
    callback();
  }
};

const registerRules = {
  username: [
    { required: true, trigger: 'blur', message: '请输入您的账号' }
  ],
  password: [
    { required: true, trigger: 'blur', message: '请输入您的密码' }
  ],
  confirmPassword: [
    { required: true, trigger: 'blur', message: '请确认您的密码' },
    { validator: validateConfirmPassword, trigger: 'blur' }
  ],
  email: [
    { required: true, trigger: 'blur', message: '请输入您的邮箱' },
    { type: 'email', message: '请输入有效的邮箱地址', trigger: 'blur' }
  ]
};

const registerRef = ref(null);


const handleRegister = () => {
  registerRef.value.validate(async (valid) => {
    if (valid) {
      try {
        // // 将响应式对象转换为普通对象
        // 将表单数据序列化为 URL 编码格式
        // const formData = qs.stringify(registerForm.value);
        const formData = JSON.stringify(registerForm.value);
        // 发送 POST 请求，将 formData 作为请求体发送
        let result = await axios.post("http://localhost:8000/user/register", formData, {
          headers: {
            // 'Content-Type': 'application/x-www-form-urlencoded'
            'Content-Type': 'application/json'
          }
        });
        let data = result.data;
        if (data.code === 200) {
          ElMessage.success(data.info);
          ElMessage.info("请检查您的邮箱，点击验证链接完成注册");
        } else {
          ElMessage.error(data.info);
        }
      } catch (error) {
        ElMessage.error('注册失败');
      }
    } else {
      ElMessage.error('表单验证失败');
    }
  });
};
</script>


<style lang="scss" scoped>
a {
  color: white;
}
.register {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  background-image: url("../assets/styles/background01.png");
  background-size: cover;
}

.register-form {
  border-radius: 6px;
  background: #ffffff;
  width: 400px;
  padding: 25px 25px 5px 25px;
  .el-input {
    height: 40px;
    input {
      display: inline-block;
      height: 40px;
    }
  }
}

.title {
  text-align: center;
  margin: 0px auto 30px auto;
  color: #707070;
}

.el-register-footer {
  height: 40px;
  line-height: 40px;
  position: fixed;
  bottom: 0;
  text-align: center;
  margin-top: 20px;
  color: #999;
}
</style>