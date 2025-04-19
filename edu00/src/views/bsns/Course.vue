<template>
  <div class="container">
    <h2 class="title">课程列表</h2>
    <button class="btn btn-primary" @click="openCreateCourseDialog">创建新课程</button>
    <table class="table">
      <thead>
        <tr>
          <th>课程编号</th>
          <th>课程名称</th>
          <th>课程封面</th>
          <th>课程简介</th>
          <th>课程类型</th>
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
            <button class="btn btn-success" @click="editCourse(course.course_id)">编辑</button>
            <button class="btn btn-danger" @click="deleteCourse(course.course_id)">删除</button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- 创建/编辑课程对话框 -->
    <div
      v-if="showCourseDialog"
      class="dialog-overlay"
      :class="{ show: showCourseDialog }"
    >
      <div class="dialog-content show">
        <h3 class="dialog-title">{{ editMode ? '编辑课程' : '创建新课程' }}</h3>
        <form @submit.prevent="saveCourse">
          <div class="form-group">
            <label>课程编号</label>
            <input
              type="text"
              v-model="courseForm.course_id"
              :disabled="editMode"
              class="form-input"
              required
            />
          </div>
          <div class="form-group">
            <label>课程名称</label>
            <input
              type="text"
              v-model="courseForm.course_name"
              class="form-input"
              required
            />
          </div>
          <div class="form-group">
            <label>课程封面</label>
            <input
              type="file"
              @change="courseForm.course_cover = $event.target.files[0]"
              class="form-input"
            />
          </div>
          <div class="form-group">
            <label>课程简介</label>
            <textarea
              v-model="courseForm.course_intro"
              class="form-input"
              required
            ></textarea>
          </div>
          <div class="form-group">
            <label>课程类型</label>
            <input
              type="text"
              v-model="courseForm.course_type"
              class="form-input"
              required
            />
          </div>
          <div class="form-group">
            <label>授课教师编号</label>
            <input
              type="text"
              v-model="courseForm.teacher_id"
              class="form-input"
              required
            />
          </div>
          <div class="form-group">
            <label>开课时间</label>
            <input
              type="datetime-local"
              v-model="courseForm.start_time"
              class="form-input"
              required
            />
          </div>
          <div class="form-group">
            <label>结课时间</label>
            <input
              type="datetime-local"
              v-model="courseForm.end_time"
              class="form-input"
              required
            />
          </div>
          <div class="form-group">
            <button type="submit" class="btn btn-primary">保存</button>
            <button type="button" @click="closeCourseDialog" class="btn btn-secondary">取消</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { ref } from 'vue';
import requestUtil from "@/util/request";
import {ElMessage} from "element-plus";

export default {
  setup() {
    const courses = ref([]);
    const showCourseDialog = ref(false);
    const editMode = ref(false);
    const courseForm = ref({
      course_id: '',
      course_name: '',
      course_cover: null,
      course_intro: '',
      course_type: '',
      teacher_id: '',
      start_time: '',
      end_time: ''
    });

    const fetchCourses = async () => {
      try {
        // const response = await axios.get('http://localhost:8002/api/courses/');
        const response = await requestUtil.get('http://localhost:8002/api/courses/');
        courses.value = response.data;
      } catch (error) {
        console.error('获取课程失败:', error);
      }
    };

    const openCreateCourseDialog = () => {
      editMode.value = false;
      courseForm.value = {
        course_id: '',
        course_name: '',
        course_cover: null,
        course_intro: '',
        course_type: '',
        teacher_id: '',
        start_time: '',
        end_time: ''
      };
      showCourseDialog.value = true;
    };

    const closeCourseDialog = () => {
      showCourseDialog.value = false;
    };

    const saveCourse = async () => {
      try {
        const url = editMode.value
          ? `http://localhost:8002/api/courses/${courseForm.value.course_id}/`
          : 'http://localhost:8002/api/courses/';
        const method = editMode.value ? 'put' : 'post';

        const formData = new FormData();
        formData.append("course_id", courseForm.value.course_id);
        formData.append("course_name", courseForm.value.course_name);
        if (courseForm.value.course_cover) {
          formData.append("course_cover", courseForm.value.course_cover);
        }
        formData.append("course_intro", courseForm.value.course_intro);
        formData.append("course_type", courseForm.value.course_type);
        formData.append("teacher_id", courseForm.value.teacher_id);
        formData.append("start_time", new Date(courseForm.value.start_time).toISOString());
        formData.append("end_time", new Date(courseForm.value.end_time).toISOString());

        const response = await axios({
          method: method,
          url: url,
          data: formData,
          headers: { "Content-Type": "multipart/form-data" }
        });
        console.log("数据",response.data);

        await fetchCourses();
        closeCourseDialog();
      } catch (error) {
        console.error('保存课程失败:', error);
      }
    };

    const editCourse = (courseId) => {
      const course = courses.value.find(course => course.course_id === courseId);
      courseForm.value = { ...course };
      showCourseDialog.value = true;
      editMode.value = true;
    };

    const deleteCourse = async (courseId) => {
      try {
        // await axios.delete(`http://localhost:8002/api/courses/${courseId}/`);
        await requestUtil.del(`http://localhost:8002/api/courses/${courseId}/`);
        ElMessage.success('删除成功！');
        await fetchCourses();
      } catch (error) {
        console.error('删除课程失败:', error);
      }
    };

    const formatDate = (date) => {
      return new Date(date).toLocaleString();
    };

    const imageLoadError = (event) => {
      console.warn(`图片加载失败: ${event.target.src}`);
      event.target.src = '/path/to/default/image.png';  // 设置默认图片
    };

    fetchCourses();

    return {
      courses,
      showCourseDialog,
      editMode,
      courseForm,
      openCreateCourseDialog,
      closeCourseDialog,
      saveCourse,
      editCourse,
      deleteCourse,
      formatDate,
      imageLoadError
    };
  }
};
</script>



<!--<script>-->
<!--import { ref } from "vue";-->
<!--import { get, post, put, del } from "@/util/request";-->
<!--import { ElMessage } from "element-plus";-->

<!--export default {-->
<!--  setup() {-->
<!--    const courses = ref([]);-->
<!--    const showCourseDialog = ref(false);-->
<!--    const editMode = ref(false);-->
<!--    const courseForm = ref({-->
<!--      course_id: "",-->
<!--      course_name: "",-->
<!--      course_cover: null,-->
<!--      course_intro: "",-->
<!--      course_type: "",-->
<!--      teacher_id: "",-->
<!--      start_time: "",-->
<!--      end_time: "",-->
<!--    });-->

<!--    const fetchCourses = async () => {-->
<!--      try {-->
<!--        const response = await get("http://localhost:8002/api/courses/");-->
<!--        courses.value = response.data;-->
<!--      } catch (error) {-->
<!--        console.error("获取课程失败:", error);-->
<!--        if (error.response.status === 401) {-->
<!--          ElMessage.error("未认证，请登录！");-->
<!--        } else {-->
<!--          ElMessage.error("获取课程失败，请检查网络或后端服务是否正常运行！");-->
<!--        }-->
<!--      }-->
<!--    };-->

<!--    const openCreateCourseDialog = () => {-->
<!--      editMode.value = false;-->
<!--      courseForm.value = {-->
<!--        course_id: "",-->
<!--        course_name: "",-->
<!--        course_cover: null,-->
<!--        course_intro: "",-->
<!--        course_type: "",-->
<!--        teacher_id: "",-->
<!--        start_time: "",-->
<!--        end_time: "",-->
<!--      };-->
<!--      showCourseDialog.value = true;-->
<!--    };-->

<!--    const closeCourseDialog = () => {-->
<!--      showCourseDialog.value = false;-->
<!--    };-->

<!--    const saveCourse = async () => {-->
<!--      try {-->
<!--        const url = editMode.value-->
<!--          ? `http://localhost:8002/api/courses/${courseForm.value.course_id}/`-->
<!--          : "http://localhost:8002/api/courses/";-->
<!--        const method = editMode.value ? "put" : "post";-->

<!--        const formData = new FormData();-->
<!--        formData.append("course_id", courseForm.value.course_id);-->
<!--        formData.append("course_name", courseForm.value.course_name);-->
<!--        if (courseForm.value.course_cover) {-->
<!--          formData.append("course_cover", courseForm.value.course_cover);-->
<!--        }-->
<!--        formData.append("course_intro", courseForm.value.course_intro);-->
<!--        formData.append("course_type", courseForm.value.course_type);-->
<!--        formData.append("teacher_id", courseForm.value.teacher_id);-->
<!--        formData.append("start_time", new Date(courseForm.value.start_time).toISOString());-->
<!--        formData.append("end_time", new Date(courseForm.value.end_time).toISOString());-->

<!--        if (method === "post") {-->
<!--          await post(url, formData);-->
<!--        } else {-->
<!--          await put(url, formData);-->
<!--        }-->

<!--        await fetchCourses();-->
<!--        closeCourseDialog();-->
<!--      } catch (error) {-->
<!--        console.error("保存课程失败:", error);-->
<!--        if (error.response.status === 401) {-->
<!--          ElMessage.error("未认证，请登录！");-->
<!--        } else {-->
<!--          ElMessage.error("保存课程失败，请检查网络或后端服务是否正常运行！");-->
<!--        }-->
<!--      }-->
<!--    };-->

<!--    const editCourse = (courseId) => {-->
<!--      const course = courses.value.find((course) => course.course_id === courseId);-->
<!--      courseForm.value = { ...course };-->
<!--      showCourseDialog.value = true;-->
<!--      editMode.value = true;-->
<!--    };-->

<!--    const deleteCourse = async (courseId) => {-->
<!--      try {-->
<!--        await del(`http://localhost:8002/api/courses/${courseId}/`);-->
<!--        ElMessage.success("删除成功！");-->
<!--        await fetchCourses();-->
<!--      } catch (error) {-->
<!--        console.error("删除课程失败:", error);-->
<!--        if (error.response.status === 401) {-->
<!--          ElMessage.error("未认证，请登录！");-->
<!--        } else {-->
<!--          ElMessage.error("删除课程失败，请检查网络或后端服务是否正常运行！");-->
<!--        }-->
<!--      }-->
<!--    };-->

<!--    const formatDate = (date) => {-->
<!--      return new Date(date).toLocaleString();-->
<!--    };-->

<!--    const imageLoadError = (event) => {-->
<!--      console.warn(`图片加载失败: ${event.target.src}`);-->
<!--      event.target.src = "/path/to/default/image.png"; // 设置默认图片-->
<!--    };-->

<!--    fetchCourses();-->

<!--    return {-->
<!--      courses,-->
<!--      showCourseDialog,-->
<!--      editMode,-->
<!--      courseForm,-->
<!--      openCreateCourseDialog,-->
<!--      closeCourseDialog,-->
<!--      saveCourse,-->
<!--      editCourse,-->
<!--      deleteCourse,-->
<!--      formatDate,-->
<!--      imageLoadError,-->
<!--    };-->
<!--  },-->
<!--};-->
<!--</script>-->






<style scoped>
/* 基础样式 */
.container {
  max-width: 100%;
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
  padding: 8px 16px;
  margin: 5px;
  border: none;
  border-radius: 6px;
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

.btn-danger {
  background-color: #dc3545;
}

.btn-danger:hover {
  background-color: #a71d2a;
}

.btn-secondary {
  background-color: #6c757d;
}

.btn-secondary:hover {
  background-color: #495057;
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

.dialog-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  opacity: 0;
  transition: opacity 0.3s ease-in-out;
}

.dialog-overlay.show {
  opacity: 1;
}

.dialog-content {
  background: #f9f9f9;
  border: 2px solid #ccc;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 20px;
  border-radius: 12px;
  width: 100%;
  max-width: 400px;
  margin: 20px;
  overflow-y: auto;
  max-height: 80vh;
  transform: translateY(-20px);
  transition: transform 0.3s ease-in-out;
}

.dialog-content.show {
  transform: translateY(0);
}

.dialog-title {
  font-size: 20px;
  font-weight: bold;
  color: #333;
  margin-bottom: 20px;
  text-align: center;
  opacity: 0; /* 初始状态透明 */
  transform: translateY(-20px); /* 初始状态向上偏移 */
  animation: fadeInSlide 0.5s ease-in-out forwards; /* 应用动画 */
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
}

.form-input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 6px;
  background: #fff;
  font-size: 14px;
}

.form-input[type="file"] {
  padding: 0;
}

/* 动画定义 */
@keyframes fadeInSlide {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
/* 响应式设计 */
@media (max-width: 768px) {
  .container {
    padding: 10px;
  }

  .table {
    font-size: 14px;
  }

  .course-cover {
    width: 40px;
    height: 40px;
  }

  .btn {
    padding: 4px 8px;
    font-size: 12px;
  }

  .dialog-content {
    padding: 15px;
    margin: 10px;
  }

  .form-input {
    padding: 6px;
  }
}

@media (max-width: 480px) {
  .dialog-content {
    padding: 10px;
    margin: 5px;
  }

  .form-input {
    padding: 4px;
  }

  .btn {
    padding: 3px 6px;
    font-size: 10px;
  }
}
</style>



