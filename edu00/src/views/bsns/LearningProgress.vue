<template>
  <div>
    <h2>学习进度</h2>
    <div v-if="progress">
      <p>课程名称: {{ progress.course_name }}</p>
      <p>学习进度: {{ progress.progress }}%</p>
    </div>
    <div v-else>未找到学习进度</div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      courseId: '',
      progress: null
    };
  },
  async mounted() {
    this.courseId = this.$route.params.courseId;
    await this.fetchProgress();
  },
  methods: {
    async fetchProgress() {
      try {
        const response = await axios.get(`/api/progress/${this.courseId}/`, { withCredentials: true });
        this.progress = response.data;
      } catch (error) {
        console.error(error);
      }
    }
  }
};
</script>