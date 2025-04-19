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
          <td>{{ formatDate(course.start_time) }}</td>
          <td>{{ formatDate(course.end_time) }}</td>
          <td>
            <button class="btn btn-primary" @click="viewChapters(course.course_id, course)">查看章节</button>
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

    <!-- 章节详情对话框 -->
    <div
      v-if="showChapterDialog"
      class="dialog-overlay"
      :class="{ show: showChapterDialog }"
    >
      <div class="dialog-content show">
        <h3 class="dialog-title">章节详情</h3>
        <table class="table">
          <thead>
            <tr>
              <th>章节编号</th>
              <th>章节名称</th>
              <th>章节顺序</th>
              <th>操作</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="chapter in chapters" :key="chapter.chapter_id">
              <td>{{ chapter.chapter_id }}</td>
              <td>{{ chapter.chapter_name }}</td>
              <td>{{ chapter.chapter_order }}</td>
              <td>
                <button class="btn btn-success" @click="editChapter(chapter.chapter_id)">编辑</button>
                <button class="btn btn-danger" @click="deleteChapter(chapter.chapter_id)">删除</button>
              </td>
            </tr>
          </tbody>
        </table>
        <div class="form-group">
          <button type="button" @click="closeChapterDialog" class="btn btn-secondary">关闭</button>
          <button type="button" @click="openCreateChapterDialog(selectedCourse.course_id)" class="btn btn-primary">添加章节</button>
        </div>
      </div>
    </div>

    <!-- 添加/编辑章节对话框 -->
    <div
      v-if="showChapterForm"
      class="dialog-overlay"
      :class="{ show: showChapterForm }"
    >
      <div class="dialog-content show">
        <h3 class="dialog-title">{{ editChapterMode ? '编辑章节' : '添加章节' }}</h3>
        <form @submit.prevent="saveChapter">
          <div class="form-group">
            <label>章节编号</label>
            <input
              type="text"
              v-model="chapterForm.chapter_id"
              :disabled="editChapterMode"
              class="form-input"
              required
            />
          </div>
          <div class="form-group">
            <label>章节名称</label>
            <input
              type="text"
              v-model="chapterForm.chapter_name"
              class="form-input"
              required
            />
          </div>
          <div class="form-group">
            <label>章节顺序</label>
            <input
              type="number"
              v-model="chapterForm.chapter_order"
              class="form-input"
              required
            />
          </div>
          <div class="form-group">
            <button type="submit" class="btn btn-primary">保存</button>
            <button type="button" @click="closeChapterForm" class="btn btn-secondary">取消</button>
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
import { ElMessage } from "element-plus";

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

    const chapters = ref([]);
    const showChapterDialog = ref(false);
    const showChapterForm = ref(false);
    const editChapterMode = ref(false);
    const chapterForm = ref({
      chapter_id: '',
      chapter_name: '',
      chapter_order: 1,
      course_id: ''
    });

    const selectedCourse = ref(null); // 当前选中的课程对象

    const fetchCourses = async () => {
      try {
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
        await requestUtil.del(`http://localhost:8002/api/courses/${courseId}/`);
        ElMessage.success('删除成功！');
        await fetchCourses();
      } catch (error) {
        console.error('删除课程失败:', error);
      }
    };

    const viewChapters = async (courseId, course) => {
      selectedCourse.value = course; // 更新当前选中的课程对象
      try {
        const response = await axios.get(`http://localhost:8002/api/chapters/?course_id=${courseId}`);
        chapters.value = response.data;
        showChapterDialog.value = true;
      } catch (error) {
        console.error('获取章节详情失败:', error);
      }
    };

    const closeChapterDialog = () => {
      showChapterDialog.value = false;
    };

    const openCreateChapterDialog = (courseId) => {
      editChapterMode.value = false;
      chapterForm.value = {
        chapter_id: '',
        chapter_name: '',
        chapter_order: 1,
        course_id: courseId
      };
      showChapterForm.value = true;
    };

    const closeChapterForm = () => {
      showChapterForm.value = false;
    };

    const saveChapter = async () => {
      try {
        const url = editChapterMode.value
          ? `http://localhost:8002/api/chapters/${chapterForm.value.chapter_id}/`
          : 'http://localhost:8002/api/chapters/';
        const method = editChapterMode.value ? 'put' : 'post';

        const response = await axios({
          method: method,
          url: url,
          data: chapterForm.value
        });

        await viewChapters(chapterForm.value.course_id); // 刷新章节列表
        closeChapterForm();
      } catch (error) {
        console.error('保存章节失败:', error);
      }
    };

    const editChapter = (chapterId) => {
      const chapter = chapters.value.find(chapter => chapter.chapter_id === chapterId);
      chapterForm.value = { ...chapter };
      showChapterForm.value = true;
      editChapterMode.value = true;
    };

    const deleteChapter = async (chapterId) => {
      try {
        await axios.delete(`http://localhost:8002/api/chapters/${chapterId}/`);
        await viewChapters(chapterForm.value.course_id); // 刷新章节列表
      } catch (error) {
        console.error('删除章节失败:', error);
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
      chapters,
      showChapterDialog,
      showChapterForm,
      editChapterMode,
      chapterForm,
      viewChapters,
      closeChapterDialog,
      openCreateChapterDialog,
      closeChapterForm,
      saveChapter,
      editChapter,
      deleteChapter,
      formatDate,
      imageLoadError,
      selectedCourse
    };
  }
};
</script>

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