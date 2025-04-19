<template>
  <div>
    <div v-if="loading">Loading...</div>
    <div v-if="success">Account activated successfully!</div>
    <div v-if="error">Failed to activate account. Please try again.</div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';

export default {
  props: {
    uid: String,
    tokens: String
  },
  setup(props) {
    // 定义响应式变量
    const loading = ref(true);
    const success = ref(false);
    const error = ref(false);

    // 激活账户的方法
    async function activateAccount(uid, token) {
      try {
        const response = await axios.get(`http://localhost:8000/user/activate/${uid}/${tokens}`);
        if (response.data.success) {
          success.value = true;
        } else {
          error.value = true;
        }
      } catch (error) {
        console.error('Activation failed:', error);
        error.value = true;
      } finally {
        loading.value = false;
      }
    }

    // 在组件挂载时调用激活方法
    onMounted(() => {
      activateAccount(props.uid, props.tokens);
    });

    // 返回响应式变量和方法
    return {
      loading,
      success,
      error
    };
  }
};
</script>

<style scoped>
.activation-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  text-align: center;
}

.success, .error {
  margin-top: 20px;
  padding: 10px;
  border-radius: 5px;
}

.success {
  background-color: #d4edda;
  color: #155724;
}

.error {
  background-color: #f8d7da;
  color: #721c24;
}
</style>