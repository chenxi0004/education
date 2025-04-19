
<!--<template>-->
<!--  <el-card class="course-container">-->
<!--    <h2 v-if="role === '学生'">我的课程</h2>-->
<!--    <h2 v-else>我创建的课程</h2>-->

<!--    &lt;!&ndash; 课程列表 &ndash;&gt;-->
<!--    <div v-if="!selectedCourse">-->
<!--      <div v-for="course in courses" :key="course.course_id" class="course-item">-->
<!--        <el-card class="course-card" @click="selectCourse(course.course_id)">-->
<!--          <img :src="course.course_cover" class="course-image" alt="课程封面">-->
<!--          <div class="course-info">-->
<!--            <h3>{{ course.course_name }}</h3>-->
<!--            <p>课程编号: {{ course.course_id }}</p>-->
<!--          </div>-->
<!--        </el-card>-->
<!--      </div>-->
<!--    </div>-->

<!--    &lt;!&ndash; 课程详情 &ndash;&gt;-->
<!--    <div v-else>-->
<!--      <el-card class="course-detail">-->
<!--        <h2>{{ selectedCourse.course_name }}</h2>-->
<!--        <p>课程编号: {{ selectedCourse.course_id }}</p>-->
<!--        <p>课程简介: {{ selectedCourse.course_intro }}</p>-->
<!--        <p>授课教师: {{ selectedCourse.get_teacher_name }}</p>-->
<!--        <p>开课时间: {{ selectedCourse.start_time }}</p>-->
<!--        <p>结课时间: {{ selectedCourse.end_time }}</p>-->
<!--      </el-card>-->

<!--      &lt;!&ndash; 评论区 &ndash;&gt;-->
<!--      <h3>评论区</h3>-->
<!--      <div v-for="comment in comments" :key="comment.comment_id" class="comment-item">-->
<!--        <p><strong>{{ comment.user_id }}</strong> ({{ comment.user_role }}): {{ comment.content }}</p>-->
<!--        <p>时间: {{ comment.created_time }}</p>-->
<!--      </div>-->

<!--      &lt;!&ndash; 发表评论 &ndash;&gt;-->
<!--      <h3>发表评论</h3>-->
<!--      <el-form @submit.prevent="submitComment">-->
<!--        <el-form-item>-->
<!--          <el-input-->
<!--            type="textarea"-->
<!--            v-model="commentContent"-->
<!--            placeholder="请输入评论内容"-->
<!--          ></el-input>-->
<!--        </el-form-item>-->
<!--        <el-form-item>-->
<!--          <el-button type="primary" @click="submitComment">提交评论</el-button>-->
<!--        </el-form-item>-->
<!--      </el-form>-->
<!--    </div>-->
<!--  </el-card>-->
<!--</template>-->

<!--<script>-->
<!--import { ref, onMounted } from "vue";-->
<!--import { ElMessage } from "element-plus";-->
<!--import axios from "axios";-->
<!--import { useStore } from "vuex";-->

<!--export default {-->
<!--  setup() {-->
<!--    const store = useStore();-->
<!--    const user = store.state.user;-->
<!--    const role = store.state.role;-->
<!--    const courses = ref([]);-->
<!--    const selectedCourse = ref(null);-->
<!--    const comments = ref([]);-->
<!--    const commentContent = ref("");-->

<!--    const fetchCourses = async () => {-->
<!--      try {-->
<!--        let url = `http://localhost:8002/api/courses/`;-->
<!--        if (role === 'teacher') {-->
<!--          // 教师只能看到自己创建的课程-->
<!--          url += `?teacher_id=${user.student_or_teacher_id}`;-->
<!--        } else if (role === '学生')-->
<!--        {-->
<!--          // 学生只能看到自己选修的课程-->
<!--          const enrolledCoursesResponse = await axios.get(`http://localhost:8002/api/enrollments/?student_id=${user.student_or_teacher_id}`);-->
<!--          const enrolledCourseIds = enrolledCoursesResponse.data.map(enrollment => enrollment.course_id);-->
<!--          url += `?course_id__in=${enrolledCourseIds.join(',')}`;-->
<!--        }-->
<!--        const response = await axios.get(url);-->
<!--        courses.value = response.data;-->
<!--      } catch (error) {-->
<!--        ElMessage.error("获取课程列表失败");-->
<!--      }-->
<!--    };-->

<!--    const fetchCourseDetail = async (courseId) => {-->
<!--      try {-->
<!--        const response = await axios.get(`http://localhost:8002/api/courses/${courseId}/`);-->
<!--        selectedCourse.value = response.data;-->
<!--      } catch (error) {-->
<!--        ElMessage.error("获取课程详情失败");-->
<!--      }-->
<!--    };-->

<!--    const fetchComments = async (courseId) => {-->
<!--      try {-->
<!--        const response = await axios.get(`http://localhost:8002/interact/comments/?course_id=${courseId}`);-->
<!--        comments.value = response.data;-->
<!--        console.log(user);-->
<!--      } catch (error) {-->
<!--        ElMessage.error("获取评论失败");-->
<!--      }-->
<!--    };-->

<!--    const selectCourse = async (courseId) => {-->
<!--      await fetchCourseDetail(courseId);-->
<!--      await fetchComments(courseId);-->
<!--    };-->

<!--    const submitComment = async () => {-->
<!--      if (!user) {-->
<!--        ElMessage.error("用户未登录");-->
<!--        return;-->
<!--      }-->

<!--      if (!commentContent.value.trim()) {-->
<!--        ElMessage.error("评论内容不能为空");-->
<!--        return;-->
<!--      }-->

<!--      try {-->
<!--        const response = await axios.post(`http://localhost:8002/interact/comments/`, {-->
<!--          course_id: selectedCourse.value.course_id,-->
<!--          user_id: user.student_or_teacher_id,-->
<!--          user_role:role,-->
<!--          content: commentContent.value,-->
<!--          parent: null,-->
<!--        });-->
<!--        ElMessage.success("评论成功");-->
<!--        commentContent.value = "";-->
<!--        await fetchComments(selectedCourse.value.course_id); // 刷新评论列表-->
<!--      } catch (error) {-->
<!--        ElMessage.error("评论失败");-->
<!--      }-->
<!--    };-->

<!--    onMounted(() => {-->
<!--      fetchCourses();-->
<!--    });-->

<!--    return {-->
<!--      courses,-->
<!--      selectedCourse,-->
<!--      comments,-->
<!--      commentContent,-->
<!--      selectCourse,-->
<!--      submitComment,-->
<!--    };-->
<!--  },-->
<!--};-->
<!--</script>-->

<!--<style scoped>-->
<!--.course-container {-->
<!--  max-width: 800px;-->
<!--  margin: 20px auto;-->
<!--}-->

<!--.course-item {-->
<!--  margin-bottom: 20px;-->
<!--}-->

<!--.course-card {-->
<!--  cursor: pointer;-->
<!--}-->

<!--.course-image {-->
<!--  width: 100%;-->
<!--  height: 200px;-->
<!--  object-fit: cover;-->
<!--}-->

<!--.course-info {-->
<!--  padding: 10px;-->
<!--}-->

<!--.course-detail {-->
<!--  margin-top: 20px;-->
<!--}-->

<!--.comment-item {-->
<!--  margin-bottom: 10px;-->
<!--  border-bottom: 1px solid #ccc;-->
<!--  padding-bottom: 10px;-->
<!--}-->
<!--</style>-->










<template>
  <el-card class="course-container">
    <h2 v-if="role === '学生'">我的课程</h2>
    <h2 v-else>我创建的课程</h2>

    <!-- 返回按钮 -->
    <el-button v-if="selectedCourse" class="back-button" @click="goBack">返回课程列表</el-button>

    <!-- 课程列表 -->
    <div v-if="!selectedCourse">
      <div v-for="course in courses" :key="course.course_id" class="course-item">
        <el-card class="course-card" @click="selectCourse(course.course_id)">
          <img :src="course.course_cover" class="course-image" alt="课程封面">
          <div class="course-info">
            <h3>{{ course.course_name }}</h3>
            <p>课程编号: {{ course.course_id }}</p>
          </div>
        </el-card>
      </div>
    </div>

    <!-- 课程详情 -->
    <div v-else>
      <el-card class="course-detail">
        <h2>{{ selectedCourse.course_name }}</h2>
        <p>课程编号: {{ selectedCourse.course_id }}</p>
        <p>课程简介: {{ selectedCourse.course_intro }}</p>
        <p>授课教师: {{ selectedCourse.get_teacher_name }}</p>
        <p>开课时间: {{ selectedCourse.start_time }}</p>
        <p>结课时间: {{ selectedCourse.end_time }}</p>
      </el-card>

      <!-- 评论区 -->
      <h3>评论区</h3>
      <div v-for="comment in comments" :key="comment.comment_id" class="comment-item">
        <div class="comment-header">
          <p><strong>{{ comment.user_id }}</strong> ({{ comment.user_role }}): {{ comment.content }}</p>
          <p>时间: {{ comment.created_time }}</p>
          <!-- 回复按钮 -->
          <el-button v-if="!comment.replying" @click="replyComment(comment)">回复</el-button>
        </div>
        <div v-if="comment.replying">
          <el-input
            type="textarea"
            v-model="comment.replyContent"
            placeholder="请输入回复内容"
          ></el-input>
          <el-button type="primary" @click="submitReply(comment)">提交回复</el-button>
          <el-button @click="cancelReply(comment)">取消</el-button>
        </div>
        <!-- 显示回复 -->
        <div v-for="reply in comment.replies" :key="reply.comment_id" class="reply-item">
          <p style="margin-left: 20px;"><strong>{{ reply.user_id }}</strong> ({{ reply.user_role }}): {{ reply.content }}</p>
          <p style="margin-left: 20px; font-size: 0.9em; color: #888;">时间: {{ reply.created_time }}</p>
        </div>
      </div>

      <!-- 发表评论 -->
      <h3>发表评论</h3>
      <el-form @submit.prevent="submitComment">
        <el-form-item>
          <el-input
            type="textarea"
            v-model="commentContent"
            placeholder="请输入评论内容"
          ></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitComment">提交评论</el-button>
        </el-form-item>
      </el-form>
    </div>
  </el-card>
</template>

<script>
import { ref, onMounted } from "vue";
import { ElMessage } from "element-plus";
import axios from "axios";
import { useStore } from "vuex";

export default {
  setup() {
    const store = useStore();
    const user = store.state.user;
    const role = store.state.role;
    const courses = ref([]);
    const selectedCourse = ref(null);
    const comments = ref([]);
    const commentContent = ref("");

    const fetchCourses = async () => {
      try {
        let url = `http://localhost:8002/api/courses/`;
        if (role === '老师') {
          // 教师只能看到自己创建的课程
          url += `?teacher_id=${user.student_or_teacher_id}`;
        } else if (role === '学生') {
          // 学生只能看到自己选修的课程
          const enrolledCoursesResponse = await axios.get(`http://localhost:8002/api/enrollments/?student_id=${user.student_or_teacher_id}`);
          const enrolledCourseIds = enrolledCoursesResponse.data.map(enrollment => enrollment.course_id);
          url += `?course_id__in=${enrolledCourseIds.join(',')}`;
          console.log(enrolledCourseIds.join(','));
        }
        const response = await axios.get(url);
        courses.value = response.data;
      } catch (error) {
        ElMessage.error("获取课程列表失败");
      }
    };

    const fetchCourseDetail = async (courseId) => {
      try {
        const response = await axios.get(`http://localhost:8002/api/courses/${courseId}/`);
        selectedCourse.value = response.data;
      } catch (error) {
        ElMessage.error("获取课程详情失败");
      }
    };

    const fetchComments = async (courseId) => {
      try {
        const response = await axios.get(`http://localhost:8002/interact/comments/?course_id=${courseId}`);
        comments.value = response.data.map(comment => ({
          ...comment,
          replying: false,
          replyContent: "",
          // replies: [] // 初始化回复列表
        }));
      } catch (error) {
        ElMessage.error("获取评论失败");
      }
    };

    const selectCourse = async (courseId) => {
      await fetchCourseDetail(courseId);
      await fetchComments(courseId);
    };

    const goBack = () => {
      selectedCourse.value = null;
    };

    const replyComment = (comment) => {
      comments.value = comments.value.map(c => {
        if (c.comment_id === comment.comment_id) {
          return { ...c, replying: true };
        }
        return c;
      });
    };

    const cancelReply = (comment) => {
      comments.value = comments.value.map(c => {
        if (c.comment_id === comment.comment_id) {
          return { ...c, replying: false, replyContent: "" };
        }
        return c;
      });
    };

    const submitReply = async (comment) => {
      if (!user) {
        ElMessage.error("用户未登录");
        return;
      }

      if (!comment.replyContent.trim()) {
        ElMessage.error("回复内容不能为空");
        return;
      }

      try {
        const response = await axios.post(`http://localhost:8002/interact/comments/`, {
          course_id: selectedCourse.value.course_id,
          user_id: user.student_or_teacher_id,
          user_role: role,
          content: comment.replyContent,
          parent: comment.comment_id,
        });
        ElMessage.success("回复成功");
        comment.replyContent = "";
        // 将回复添加到对应评论的 replies 列表中
        comments.value = comments.value.map(c => {
          if (c.comment_id === comment.comment_id) {
            return {
              ...c,
              replying: false,
              replies: [...c.replies, response.data]
            };
          }
          return c;
        });
      } catch (error) {
        ElMessage.error("回复失败");
      }
    };

    const submitComment = async () => {
      if (!user) {
        ElMessage.error("用户未登录");
        return;
      }

      if (!commentContent.value.trim()) {
        ElMessage.error("评论内容不能为空");
        return;
      }

      try {
        const response = await axios.post(`http://localhost:8002/interact/comments/`, {
          course_id: selectedCourse.value.course_id,
          user_id: user.student_or_teacher_id,
          user_role: role,
          content: commentContent.value,
          parent: null,
        });
        ElMessage.success("评论成功");
        commentContent.value = "";
        await fetchComments(selectedCourse.value.course_id); // 刷新评论列表
      } catch (error) {
        ElMessage.error("评论失败");
      }
    };

    onMounted(() => {
      fetchCourses();
    });

    return {
      courses,
      selectedCourse,
      comments,
      commentContent,
      selectCourse,
      goBack,
      replyComment,
      cancelReply,
      submitReply,
      submitComment,
    };
  },
};
</script>

<style scoped>
.course-container {
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.course-item {
  margin-bottom: 20px;
}

.course-card {
  cursor: pointer;
  transition: transform 0.3s ease;
}

.course-card:hover {
  transform: scale(1.02);
}

.course-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 8px;
}

.course-info {
  padding: 10px;
}

.course-detail {
  margin-top: 20px;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.comment-item {
  margin-bottom: 10px;
  border-bottom: 1px solid #ccc;
  padding-bottom: 10px;
}

.reply-item {
  margin-left: 20px; /* 缩进 */
  margin-top: 5px;
  border-left: 2px solid #ccc; /* 添加边框以增强视觉效果 */
  padding-left: 10px;
}

.back-button {
  margin-bottom: 20px;
}
</style>




