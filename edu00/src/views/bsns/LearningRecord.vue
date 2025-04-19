<template>
  <div>
    <h2>提交学习记录</h2>
    <form @submit.prevent="submitRecord">
      <label>学习内容: <textarea v-model="content"></textarea></label>
      <label>学习时长（分钟）: <input v-model="duration" type="number" /></label>
      <button type="submit">提交</button>
    </form>
    <div v-if="message">{{ message }}</div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      courseId: '',
      content: '',
      duration: 0,
      message: ''
    };
  },
  async mounted() {
    this.courseId = this.$route.params.courseId;
  },
  methods: {
    async submitRecord() {
      try {
        const response = await axios.post(`/api/record/${this.courseId}/`, {
          content: this.content,
          duration: this.duration
        }, { withCredentials: true });
        this.message = '记录成功';
      } catch (error) {
        this.message = error.response.data.error;
      }
    }
  }
};
</script>
<style scoped>

</style>