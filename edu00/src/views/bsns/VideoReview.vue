<!--<template>-->
<!--  <div class="review-container">-->
<!--    <h3>文件审核</h3>-->
<!--    <table class="review-table">-->
<!--      <thead>-->
<!--        <tr>-->
<!--          <th>资料编号</th>-->
<!--          <th>课程编号</th>-->
<!--          <th>文件名称</th>-->
<!--          <th>审核状态</th>-->
<!--          <th>文件链接</th>-->
<!--          <th>操作</th>-->
<!--        </tr>-->
<!--      </thead>-->
<!--      <tbody>-->
<!--        <tr v-for="video in videos" :key="video.video_id">-->
<!--          <td>{{ video.video_id }}</td>-->
<!--          <td>{{ video.course_id_display }}</td>-->
<!--          <td>{{ video.video_name }}</td>-->
<!--          <td :class="`status-${video.review_status}`">{{ video.review_status }}</td>-->
<!--          <td>-->
<!--            <a :href="video.video_file_url" target="_blank">查看文件</a>-->
<!--            <a-->
<!--                :href="video.video_file_url"-->
<!--                target="_blank"-->
<!--                rel="noopener noreferrer"-->
<!--                :download="video.video_name"-->
<!--              >-->
<!--                下载文件-->
<!--              </a>-->
<!--          </td>-->
<!--          <td>-->
<!--            <button-->
<!--              v-if="video.review_status === 'pending'"-->
<!--              @click="reviewvideo(video.video_id, 'approved')"-->
<!--              class="review-button approve"-->
<!--            >-->
<!--              通过-->
<!--            </button>-->
<!--            <button-->
<!--              v-if="video.review_status === 'pending'"-->
<!--              @click="reviewvideo(video.video_id, 'rejected')"-->
<!--              class="review-button reject"-->
<!--            >-->
<!--              拒绝-->
<!--            </button>-->
<!--          </td>-->
<!--        </tr>-->
<!--      </tbody>-->
<!--    </table>-->
<!--  </div>-->
<!--</template>-->


<!--<script>-->
<!--import axios from 'axios';-->

<!--export default {-->
<!--  data() {-->
<!--    return {-->
<!--      videos: [],-->
<!--    };-->
<!--  },-->
<!--  methods: {-->
<!--    async fetchvideos() {-->
<!--      try {-->
<!--        const response = await axios.get('http://localhost:8002/material/videos/');-->
<!--        this.videos = response.data;-->
<!--      } catch (error) {-->
<!--        console.error('获取数据失败:', error);-->
<!--        alert('获取数据失败');-->
<!--      }-->
<!--    },-->
<!--    async reviewvideo(videoId, review_status) {-->
<!--      try {-->
<!--        const response = await axios.post(`http://localhost:8002/material/videoreview/${videoId}/`, { review_status });-->
<!--        // 直接更新本地状态-->
<!--        const video = this.videos.find(m => m.video_id === videoId);-->
<!--        if (video) {-->
<!--          video.review_status = response.data.review_status;-->
<!--        }-->
<!--        alert('审核成功');-->
<!--      } catch (error) {-->
<!--        console.error('审核失败:', error);-->
<!--        alert('审核失败');-->
<!--      }-->
<!--    },-->
<!--  },-->
<!--  mounted() {-->
<!--    this.fetchvideos();-->
<!--  },-->
<!--};-->
<!--</script>-->

<!--<style scoped>-->
<!--.review-container {-->
<!--  max-width: 1000px; /* 增大容器宽度 */-->
<!--  margin: 20px auto;-->
<!--  padding: 20px;-->
<!--  background: #ffffff; /* 背景改为纯白色 */-->
<!--  border-radius: 12px; /* 增大圆角 */-->
<!--  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1); /* 增大阴影 */-->
<!--  font-family: Arial, sans-serif; /* 设置字体 */-->
<!--}-->

<!--h3 {-->
<!--  text-align: center;-->
<!--  color: #333;-->
<!--  font-size: 24px; /* 增大标题字体 */-->
<!--  margin-bottom: 20px; /* 增加标题与表格的间距 */-->
<!--}-->

<!--.review-table {-->
<!--  width: 100%;-->
<!--  border-collapse: collapse;-->
<!--  margin-top: 20px;-->
<!--  font-size: 14px; /* 设置表格字体大小 */-->
<!--}-->

<!--.review-table th,-->
<!--.review-table td {-->
<!--  padding: 15px; /* 增加单元格内间距 */-->
<!--  text-align: center;-->
<!--  border-bottom: 1px solid #ddd;-->
<!--}-->

<!--.review-table th {-->
<!--  background-color: #f0f0f0;-->
<!--  font-weight: bold;-->
<!--  color: #333;-->
<!--}-->

<!--.status-pending {-->
<!--  color: #ff9500; /* 使用更鲜艳的橙色 */-->
<!--  font-weight: bold;-->
<!--}-->

<!--.status-approved {-->
<!--  color: #28a745; /* 使用更鲜艳的绿色 */-->
<!--  font-weight: bold;-->
<!--}-->

<!--.status-rejected {-->
<!--  color: #dc3545; /* 使用更鲜艳的红色 */-->
<!--  font-weight: bold;-->
<!--}-->

<!--.review-button {-->
<!--  margin: 0 5px;-->
<!--  padding: 8px 16px; /* 增加按钮内间距 */-->
<!--  border: none;-->
<!--  border-radius: 6px; /* 增大按钮圆角 */-->
<!--  cursor: pointer;-->
<!--  font-size: 14px; /* 设置按钮字体大小 */-->
<!--  transition: background-color 0.3s ease; /* 添加过渡效果 */-->
<!--}-->

<!--.review-button.approve {-->
<!--  background-color: #28a745; /* 使用更鲜艳的绿色 */-->
<!--  color: white;-->
<!--}-->

<!--.review-button.reject {-->
<!--  background-color: #dc3545; /* 使用更鲜艳的红色 */-->
<!--  color: white;-->
<!--}-->

<!--.review-button:hover {-->
<!--  opacity: 0.8; /* 鼠标悬停时降低透明度 */-->
<!--}-->

<!--a {-->
<!--  color: #007bff; /* 链接颜色 */-->
<!--  text-decoration: none; /* 去掉下划线 */-->
<!--  font-weight: bold;-->
<!--  transition: color 0.3s ease; /* 添加过渡效果 */-->
<!--}-->

<!--a:hover {-->
<!--  color: #0056b3; /* 鼠标悬停时链接颜色变深 */-->
<!--}-->

<!--@media (max-width: 768px) {-->
<!--  .review-table {-->
<!--    font-size: 12px; /* 小屏幕下字体缩小 */-->
<!--  }-->

<!--  .review-button {-->
<!--    padding: 6px 12px; /* 小屏幕下按钮内间距缩小 */-->
<!--    font-size: 12px;-->
<!--  }-->
<!--}-->
<!--</style>-->



<template>
  <div class="review-container">
    <h3>视频审核</h3>
    <table class="review-table">
      <thead>
        <tr>
          <th>资料编号</th>
          <th>课程编号</th>
          <th>视频名称</th>
          <th>审核状态</th>
          <th>视频链接</th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="video in videos" :key="video.video_id">
          <td>{{ video.video_id }}</td>
          <td>{{ video.course_id_display }}</td>
          <td>{{ video.video_name }}</td>
          <td :class="`status-${video.review_status}`">{{ video.review_status }}</td>
          <td>
            <a :href="video.video_file_url" target="_blank">查看文件</a>
            <a
                :href="video.video_file_url"
                target="_blank"
                rel="noopener noreferrer"
                :download="video.video_name"
              >
                下载文件
              </a>
          </td>
          <td>
            <button
                v-if="video.review_status === 'approved' || video.review_status === 'rejected'"
                @click="reReviewVideo(video.video_id)"
                class="review-button re-review"
            >
                重新审核
            </button>
            <button
              v-if="video.review_status === 'pending'"
              @click="reviewvideo(video.video_id, 'approved')"
              class="review-button approve"
            >
              通过
            </button>
            <button
              v-if="video.review_status === 'pending'"
              @click="reviewvideo(video.video_id, 'rejected')"
              class="review-button reject"
            >
              拒绝
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>


<script>
import axios from 'axios';

export default {
  data() {
    return {
      videos: [],
    };
  },
  methods: {
    async fetchvideos() {
      try {
        const response = await axios.get('http://localhost:8002/material/videos/');
        this.videos = response.data;
      } catch (error) {
        console.error('获取数据失败:', error);
        alert('获取数据失败');
      }
    },
    async reviewvideo(videoId, review_status) {
      try {
        const response = await axios.post(`http://localhost:8002/material/videoreview/${videoId}/`, { review_status });
        // 直接更新本地状态
        const video = this.videos.find(m => m.video_id === videoId);
        if (video) {
          video.review_status = response.data.review_status;
        }
        alert('审核成功');
      } catch (error) {
        console.error('审核失败:', error);
        alert('审核失败');
      }
    },
    async reReviewVideo(videoId) {
        try {
            const response = await axios.post(`http://localhost:8002/material/videoreview/${videoId}/`, { review_status: 're-review' });
            const video = this.videos.find(v => v.video_id === videoId);
            if (video) {
                video.review_status = response.data.status;
            }
            alert('重新审核已启动');
        } catch (error) {
            console.error('重新审核失败:', error);
            alert('重新审核失败');
        }
    },
  },
  mounted() {
    this.fetchvideos();
  },
};
</script>

<style scoped>
.review-container {
  max-width: 1000px; /* 增大容器宽度 */
  margin: 20px auto;
  padding: 20px;
  background: #ffffff; /* 背景改为纯白色 */
  border-radius: 12px; /* 增大圆角 */
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1); /* 增大阴影 */
  font-family: Arial, sans-serif; /* 设置字体 */
}

h3 {
  text-align: center;
  color: #333;
  font-size: 24px; /* 增大标题字体 */
  margin-bottom: 20px; /* 增加标题与表格的间距 */
}

.review-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
  font-size: 14px; /* 设置表格字体大小 */
}

.review-table th,
.review-table td {
  padding: 15px; /* 增加单元格内间距 */
  text-align: center;
  border-bottom: 1px solid #ddd;
}

.review-table th {
  background-color: #f0f0f0;
  font-weight: bold;
  color: #333;
}

.status-pending {
  color: #ff9500; /* 使用更鲜艳的橙色 */
  font-weight: bold;
}

.status-approved {
  color: #28a745; /* 使用更鲜艳的绿色 */
  font-weight: bold;
}

.status-rejected {
  color: #dc3545; /* 使用更鲜艳的红色 */
  font-weight: bold;
}

.review-button {
  margin: 0 5px;
  padding: 8px 16px; /* 增加按钮内间距 */
  border: none;
  border-radius: 6px; /* 增大按钮圆角 */
  cursor: pointer;
  font-size: 14px; /* 设置按钮字体大小 */
  transition: background-color 0.3s ease; /* 添加过渡效果 */
}

.review-button.approve {
  background-color: #28a745; /* 使用更鲜艳的绿色 */
  color: white;
}

.review-button.reject {
  background-color: #dc3545; /* 使用更鲜艳的红色 */
  color: white;
}

.review-button:hover {
  opacity: 0.8; /* 鼠标悬停时降低透明度 */
}

a {
  color: #007bff; /* 链接颜色 */
  text-decoration: none; /* 去掉下划线 */
  font-weight: bold;
  transition: color 0.3s ease; /* 添加过渡效果 */
}

a:hover {
  color: #0056b3; /* 鼠标悬停时链接颜色变深 */
}

@media (max-width: 768px) {
  .review-table {
    font-size: 12px; /* 小屏幕下字体缩小 */
  }

  .review-button {
    padding: 6px 12px; /* 小屏幕下按钮内间距缩小 */
    font-size: 12px;
  }
}
</style>