

<!--<template>-->
<!--  <div>-->
<!--    <h2>课程列表</h2>-->
<!--    <ul>-->
<!--      <li v-for="course in courses" :key="course.course_id">-->
<!--        {{ course.course_name }}-->
<!--        <button @click="enroll(course.course_id)">报名</button>-->
<!--      </li>-->
<!--    </ul>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--import axios from 'axios';-->
<!--import { mapState } from 'vuex';-->

<!--export default {-->
<!--  data() {-->
<!--    return {-->
<!--      courses: [],-->
<!--    };-->
<!--  },-->
<!--  computed: {-->
<!--    ...mapState({-->
<!--      user: (state) => state.user,-->
<!--    }),-->
<!--  },-->
<!--  methods: {-->
<!--    async fetchCourses() {-->
<!--      try {-->
<!--        const response = await axios.get('http://localhost:8002/api/courses/');-->
<!--        this.courses = response.data;-->
<!--        console.log(this.courses);-->
<!--      } catch (error) {-->
<!--        console.error('获取课程列表失败:', error);-->
<!--        this.courses = [];-->
<!--        alert('获取课程列表失败');-->
<!--      }-->
<!--    },-->
<!--    async enroll(courseId) {-->
<!--      if (!this.user) {-->
<!--        alert('请先登录');-->
<!--        return;-->
<!--      }-->

<!--      try {-->
<!--        const response = await axios.post(`http://localhost:8002/api/enroll/${courseId}/`, {-->
<!--          userid: this.user.student_or_teacher_id,-->
<!--        });-->
<!--        alert(response.data.message);-->
<!--      } catch (error) {-->
<!--        alert(error.response.data.error || '报名失败');-->
<!--      }-->
<!--    },-->
<!--  },-->
<!--  mounted() {-->
<!--    this.fetchCourses();-->
<!--  },-->
<!--};-->
<!--</script>-->


<!--<template>-->
<!--  <div class="container">-->
<!--    <h2 class="title">课程列表</h2>-->
<!--    <table class="table">-->
<!--      <thead>-->
<!--        <tr>-->
<!--          <th>课程编号</th>-->
<!--          <th>课程名称</th>-->
<!--          <th>课程封面</th>-->
<!--          <th>课程简介</th>-->
<!--          <th>课程类型</th>-->
<!--          <th>开课时间</th>-->
<!--          <th>结课时间</th>-->
<!--          <th>操作</th>-->
<!--        </tr>-->
<!--      </thead>-->
<!--      <tbody>-->
<!--        <tr v-for="course in courses" :key="course.course_id">-->
<!--          <td>{{ course.course_id }}</td>-->
<!--          <td>{{ course.course_name }}</td>-->
<!--          <td>-->
<!--            <img-->
<!--              v-if="course.course_cover"-->
<!--              :src="course.course_cover"-->
<!--              alt="课程封面"-->
<!--              class="course-cover"-->
<!--              @error="imageLoadError"-->
<!--            />-->
<!--            <span v-else class="text-muted">无封面</span>-->
<!--          </td>-->
<!--          <td>{{ course.course_intro }}</td>-->
<!--          <td>{{ course.course_type }}</td>-->
<!--          <td>{{ formatDate(course.start_time) }}</td>-->
<!--          <td>{{ formatDate(course.end_time) }}</td>-->
<!--          <td>-->
<!--            <button class="btn btn-primary" @click="viewCourseDetails(course.course_id)">查看详情</button>-->
<!--            <button class="btn btn-success" @click="enroll(course.course_id)">报名</button>-->
<!--          </td>-->
<!--        </tr>-->
<!--      </tbody>-->
<!--    </table>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--import axios from 'axios';-->
<!--import { mapState } from 'vuex';-->
<!--import {ElMessage} from "element-plus";-->

<!--export default {-->
<!--  data() {-->
<!--    return {-->
<!--      courses: [],-->
<!--    };-->
<!--  },-->
<!--  computed: {-->
<!--    ...mapState({-->
<!--      user: (state) => state.user,-->
<!--    }),-->
<!--  },-->
<!--  methods: {-->
<!--    async fetchCourses() {-->
<!--      try {-->
<!--        const response = await axios.get('http://localhost:8002/api/courses/');-->
<!--        this.courses = response.data;-->
<!--      } catch (error) {-->
<!--        console.error('获取课程列表失败:', error);-->
<!--        this.courses = [];-->
<!--        alert('获取课程列表失败');-->
<!--      }-->
<!--    },-->
<!--    async enroll(courseId) {-->
<!--      if (!this.user) {-->
<!--        alert('请先登录');-->
<!--        return;-->
<!--      }-->

<!--      try {-->
<!--        const response = await axios.post(`http://localhost:8002/api/enroll/${courseId}/`, {-->
<!--          userid: this.user.student_or_teacher_id,-->
<!--        });-->
<!--        ElMessage("报名成功"+response.data.message);-->
<!--        // alert(response.data.message);-->
<!--      } catch (error) {-->
<!--        ElMessage('报名失败:' + error.response.data.error);-->
<!--        // alert(error.response.data.error || '报名失败');-->
<!--      }-->
<!--    },-->
<!--    viewCourseDetails(courseId) {-->
<!--      this.$router.push(`/course/${courseId}`);-->
<!--    },-->
<!--    formatDate(date) {-->
<!--      return new Date(date).toLocaleString();-->
<!--    },-->
<!--    imageLoadError(event) {-->
<!--      console.warn(`图片加载失败: ${event.target.src}`);-->
<!--      event.target.src = '/path/to/default/image.png';  // 设置默认图片-->
<!--    },-->
<!--  },-->
<!--  mounted() {-->
<!--    this.fetchCourses();-->
<!--  },-->
<!--};-->
<!--</script>-->



<template>
  <div class="container">
    <h2 class="title">课程列表</h2>
    <table class="table">
      <thead>
        <tr>
          <th>课程编号</th>
          <th>课程名称</th>
          <th>课程封面</th>
          <th>课程简介</th>
          <th>课程类型</th>
<!--          <th>教师编号</th>-->
          <th>开课时间</th>
          <th>结课时间</th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="course in courses" :key="course.course_id">
          <td>{{ course.course_id }}</td>
          <td>{{ course.course_name }}</td>
          <td>
            <img
              v-if="course.course_cover"
              :src="course.course_cover"
              alt="课程封面"
              class="course-cover"
              @error="imageLoadError"
            />
            <span v-else class="text-muted">无封面</span>
          </td>
          <td>{{ course.course_intro }}</td>
          <td>{{ course.course_type }}</td>
<!--          <td>{{ formatDate(course.teacher_id) }}</td>-->
          <td>{{ formatDate(course.start_time) }}</td>
          <td>{{ formatDate(course.end_time) }}</td>
          <td>
            <button
              v-if="!isEnrolled(course.course_id)"
              class="btn btn-primary"
              @click="enroll(course.course_id)"
            >
              报名
            </button>
            <button
              v-else
              class="btn btn-danger"
              @click="unenroll(course.course_id)"
            >
              退课
            </button>
            <button class="btn btn-primary" @click="viewCourseDetails(course.course_id)">
              查看详情
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';
import { mapState } from 'vuex';
import { ElMessage } from 'element-plus';

export default {
  data() {
    return {
      courses: [],
      enrolledCourses: [], // 用于存储已选课程
    };
  },
  computed: {
    ...mapState({
      user: (state) => state.user,
    }),
  },
  methods: {
    // 获取课程列表和已选课程
    async fetchCourses() {
      try {
        // 同时发起两个请求：获取课程列表和已选课程
        const [coursesResponse, enrolledResponse] = await Promise.all([
          axios.get("http://localhost:8002/api/courses/"),
          axios.get(
            `http://localhost:8002/api/enrollments/?student_id=${this.user.student_or_teacher_id}`
          )
        ]);
        // 提取已选课程的 course_id
        this.enrolledCourses = enrolledResponse.data.map(
          (enrollment) => enrollment.course_id
        );
        // 更新课程列表
        this.courses = coursesResponse.data;
      } catch (error) {
        console.error("获取课程列表或已选课程失败:", error);
        this.courses = []; // 清空课程列表
        this.enrolledCourses = []; // 清空已选课程列表
        ElMessage.error("获取课程列表失败");
      }
    },



    isEnrolled(courseId) {
      return this.enrolledCourses.includes(courseId);
    },
    async enroll(courseId) {
      if (!this.user) {
        alert('请先登录');
        return;
      }

      try {
        const response = await axios.post(`http://localhost:8002/api/enroll/${courseId}/`, {
          userid: this.user.student_or_teacher_id,
        });
        ElMessage('报名成功' + response.data.message);
        this.enrolledCourses.push(courseId); // 更新已选课程列表
      } catch (error) {
        ElMessage('报名失败:' + error.response.data.error);
      }
    },
    async unenroll(courseId) {
      if (!this.user) {
        alert('请先登录');
        return;
      }

      try {
        const response = await axios.delete(
          `http://localhost:8002/api/unenroll/${courseId}/`,
          {
            data: {
              userid: this.user.student_or_teacher_id,
            },
          }
        );
        ElMessage('退课成功' + response.data.message);
        this.enrolledCourses = this.enrolledCourses.filter((id) => id !== courseId); // 更新已选课程列表
      } catch (error) {
        ElMessage('退课失败:' + error.response.data.error);
      }
    },
    viewCourseDetails(courseId) {
      this.$router.push(`/bsns/coursedetail`);
    },
    formatDate(date) {
      return new Date(date).toLocaleString();
    },
    imageLoadError(event) {
      console.warn(`图片加载失败: ${event.target.src}`);
      event.target.src = '.src/assets/styles/01.png'; // 设置默认图片
    },
  },
  mounted() {
    this.fetchCourses();
  },
};
</script>



<style scoped>
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

.table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

.table th,
.table td {
  padding: 10px;
  border: 1px solid #ddd;
  text-align: left;
}

.table th {
  background-color: #f4f4f4;
  font-weight: bold;
}

.table tr:hover {
  background-color: #f9f9f9;
}

.btn {
  display: inline-block;
  padding: 5px 10px;
  margin: 5px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 14px;
  text-decoration: none;
  color: white;
}

.btn-primary {
  background-color: #007bff;
}

.btn-primary:hover {
  background-color: #0056b3;
}

.btn-success {
  background-color: #28a745;
}

.btn-success:hover {
  background-color: #1e6e35;
}

.course-cover {
  width: 50px;
  height: 50px;
  border-radius: 5px;
  object-fit: cover;
}

.text-muted {
  color: #6c757d;
}
</style>




