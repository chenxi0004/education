
<!--<template>-->
<!--  <div class="container">-->
<!--    &lt;!&ndash; 课程列表 &ndash;&gt;-->
<!--    <el-card class="box-card">-->
<!--      <template #header>-->
<!--        <div class="card-header">-->
<!--          <span>我的课程</span>-->
<!--        </div>-->
<!--      </template>-->
<!--      <div v-if="courses.length > 0">-->
<!--        <el-row :gutter="20">-->
<!--          <el-col :span="6" v-for="course in courses" :key="course.course_id">-->
<!--            <el-card :body-style="{ padding: '0px' }" class="course-card" @click="selectCourse(course.course_id)">-->
<!--              <img :src="getAbsoluteUrl(course.course_cover)" class="image" alt="课程封面">-->
<!--              <div class="course-info">-->
<!--                <h3 class="course-name">{{ course.course_name }}</h3>-->
<!--                <p class="course-id">编号: {{ course.course_id }}</p>-->
<!--              </div>-->
<!--            </el-card>-->
<!--          </el-col>-->
<!--        </el-row>-->
<!--      </div>-->
<!--      <div v-else>-->
<!--        <el-empty description="您尚未选任何课程"></el-empty>-->
<!--      </div>-->
<!--    </el-card>-->

<!--    &lt;!&ndash; 视频列表 &ndash;&gt;-->
<!--    <el-card class="box-card" v-if="selectedCourse">-->
<!--      <template #header>-->
<!--        <div class="card-header">-->
<!--          <span>课程视频</span>-->
<!--        </div>-->
<!--      </template>-->
<!--      <div v-if="videos.length > 0">-->
<!--        <el-table :data="videos" style="width: 100%">-->
<!--          <el-table-column prop="video_name" label="视频名称"></el-table-column>-->
<!--          <el-table-column label="操作">-->
<!--            <template #default="scope">-->
<!--              <el-button type="primary" @click="playVideo(scope.row.video_url)">播放</el-button>-->
<!--              <el-button type="success" @click="downloadVideo(scope.row.video_url, scope.row.video_name)">下载</el-button>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--        </el-table>-->
<!--      </div>-->
<!--      <div v-else>-->
<!--        <el-empty description="暂无视频"></el-empty>-->
<!--      </div>-->
<!--    </el-card>-->
<!--  </div>-->
<!--</template>-->




<!--&lt;!&ndash;<template>&ndash;&gt;-->
<!--&lt;!&ndash;  <div class="container">&ndash;&gt;-->
<!--&lt;!&ndash;    &lt;!&ndash; 课程列表 &ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;    <el-card class="box-card">&ndash;&gt;-->
<!--&lt;!&ndash;      <template #header>&ndash;&gt;-->
<!--&lt;!&ndash;        <div class="card-header">&ndash;&gt;-->
<!--&lt;!&ndash;          <span>我的课程</span>&ndash;&gt;-->
<!--&lt;!&ndash;        </div>&ndash;&gt;-->
<!--&lt;!&ndash;      </template>&ndash;&gt;-->
<!--&lt;!&ndash;      <div v-if="courses.length > 0">&ndash;&gt;-->
<!--&lt;!&ndash;        <el-row :gutter="20">&ndash;&gt;-->
<!--&lt;!&ndash;          <el-col :span="6" v-for="course in courses" :key="course.course_id">&ndash;&gt;-->
<!--&lt;!&ndash;            <el-card :body-style="{ padding: '0px' }" class="course-card" @click="selectCourse(course)">&ndash;&gt;-->
<!--&lt;!&ndash;              <img :src="getAbsoluteUrl(course.course_cover)" class="image" alt="课程封面">&ndash;&gt;-->
<!--&lt;!&ndash;              <div class="course-info">&ndash;&gt;-->
<!--&lt;!&ndash;                <h3 class="course-name">{{ course.course_name }}</h3>&ndash;&gt;-->
<!--&lt;!&ndash;                <p class="course-id">编号: {{ course.course_id }}</p>&ndash;&gt;-->
<!--&lt;!&ndash;              </div>&ndash;&gt;-->
<!--&lt;!&ndash;            </el-card>&ndash;&gt;-->
<!--&lt;!&ndash;          </el-col>&ndash;&gt;-->
<!--&lt;!&ndash;        </el-row>&ndash;&gt;-->
<!--&lt;!&ndash;      </div>&ndash;&gt;-->
<!--&lt;!&ndash;      <div v-else>&ndash;&gt;-->
<!--&lt;!&ndash;        <el-empty description="您尚未选任何课程"></el-empty>&ndash;&gt;-->
<!--&lt;!&ndash;      </div>&ndash;&gt;-->
<!--&lt;!&ndash;    </el-card>&ndash;&gt;-->

<!--&lt;!&ndash;    &lt;!&ndash; 章节和视频列表 &ndash;&gt;&ndash;&gt;-->
<!--&lt;!&ndash;    <el-card class="box-card" v-if="selectedCourse">&ndash;&gt;-->
<!--&lt;!&ndash;      <template #header>&ndash;&gt;-->
<!--&lt;!&ndash;        <div class="card-header">&ndash;&gt;-->
<!--&lt;!&ndash;          <span>课程内容</span>&ndash;&gt;-->
<!--&lt;!&ndash;        </div>&ndash;&gt;-->
<!--&lt;!&ndash;      </template>&ndash;&gt;-->
<!--&lt;!&ndash;      <div v-if="chapters.length > 0">&ndash;&gt;-->
<!--&lt;!&ndash;        <el-collapse v-model="activeChapter">&ndash;&gt;-->
<!--&lt;!&ndash;          <el-collapse-item v-for="chapter in chapters" :key="chapter.chapter_id" :name="chapter.chapter_id">&ndash;&gt;-->
<!--&lt;!&ndash;            <template #title>&ndash;&gt;-->
<!--&lt;!&ndash;              <span class="chapter-title">{{ chapter.chapter_name }}</span>&ndash;&gt;-->
<!--&lt;!&ndash;            </template>&ndash;&gt;-->
<!--&lt;!&ndash;            <el-table :data="chapter.videos" style="width: 100%">&ndash;&gt;-->
<!--&lt;!&ndash;              <el-table-column prop="video_name" label="视频名称"></el-table-column>&ndash;&gt;-->
<!--&lt;!&ndash;              <el-table-column label="操作">&ndash;&gt;-->
<!--&lt;!&ndash;                <template #default="scope">&ndash;&gt;-->
<!--&lt;!&ndash;                  <el-button type="primary" @click="playVideo(scope.row.video_url)">播放</el-button>&ndash;&gt;-->
<!--&lt;!&ndash;                  <el-button type="success" @click="downloadVideo(scope.row.video_url, scope.row.video_name)">下载</el-button>&ndash;&gt;-->
<!--&lt;!&ndash;                </template>&ndash;&gt;-->
<!--&lt;!&ndash;              </el-table-column>&ndash;&gt;-->
<!--&lt;!&ndash;            </el-table>&ndash;&gt;-->
<!--&lt;!&ndash;          </el-collapse-item>&ndash;&gt;-->
<!--&lt;!&ndash;        </el-collapse>&ndash;&gt;-->
<!--&lt;!&ndash;      </div>&ndash;&gt;-->
<!--&lt;!&ndash;      <div v-else>&ndash;&gt;-->
<!--&lt;!&ndash;        <el-empty description="暂无视频"></el-empty>&ndash;&gt;-->
<!--&lt;!&ndash;      </div>&ndash;&gt;-->
<!--&lt;!&ndash;    </el-card>&ndash;&gt;-->
<!--&lt;!&ndash;  </div>&ndash;&gt;-->
<!--&lt;!&ndash;</template>&ndash;&gt;-->



<!--<script>-->
<!--import axios from "axios";-->
<!--import { ElMessage } from "element-plus";-->

<!--export default {-->
<!--  data() {-->
<!--    return {-->
<!--      enrolledCourseIds: [], // 存储已选课程的ID-->
<!--      courses: [], // 存储完整的课程详情-->
<!--      videos: [], // 存储当前课程的视频-->
<!--      selectedCourse: null // 当前选择的课程ID-->
<!--    };-->
<!--  },-->
<!--  methods: {-->
<!--    // 获取学生已选课程ID-->
<!--    async fetchEnrolledCourses() {-->
<!--      try {-->
<!--        const response = await axios.get(-->
<!--          `http://localhost:8002/api/enrollments/?student_id=${this.user.student_or_teacher_id}`-->
<!--        );-->
<!--        this.enrolledCourseIds = response.data; // 假设返回的是课程ID数组-->
<!--        this.fetchCourseDetails(); // 根据课程ID获取课程详情-->
<!--      } catch (error) {-->
<!--        console.error("获取已选课程失败:", error);-->
<!--        ElMessage.error("获取已选课程失败");-->
<!--      }-->
<!--    },-->
<!--    // 根据课程ID获取课程详情-->
<!--    async fetchCourseDetails() {-->
<!--      if (!this.enrolledCourseIds || this.enrolledCourseIds.length === 0) {-->
<!--        this.courses = [];-->
<!--        return;-->
<!--      }-->

<!--      try {-->
<!--        const coursePromises = this.enrolledCourseIds.map(courseId =>-->
<!--          axios.get(`http://localhost:8002/api/courses/${courseId}/`)-->
<!--        );-->

<!--        const courseResponses = await Promise.all(coursePromises);-->
<!--        this.courses = courseResponses.map(response => response.data);-->
<!--      } catch (error) {-->
<!--        console.error("获取课程详情失败:", error);-->
<!--        ElMessage.error("获取课程详情失败");-->
<!--      }-->
<!--    },-->
<!--    // 根据课程ID获取视频列表-->
<!--    async fetchVideos(courseId) {-->
<!--      try {-->
<!--        // 清空当前视频列表-->
<!--        this.videos = [];-->
<!--        const response = await axios.get(-->
<!--          `http://localhost:8002/api/student/${this.user.student_or_teacher_id}/course/${courseId}/videos/`-->
<!--        );-->
<!--        this.videos = response.data.videos;-->
<!--      } catch (error) {-->
<!--        console.error("获取视频列表失败:", error);-->
<!--        ElMessage.error("获取视频列表失败，请重新登录");-->
<!--      }-->
<!--    },-->
<!--    // 选择课程-->
<!--    selectCourse(courseId) {-->
<!--      this.selectedCourse = courseId;-->
<!--      this.fetchVideos(courseId);-->
<!--    },-->
<!--    // 播放视频-->
<!--    playVideo(url) {-->
<!--      window.open(this.getAbsoluteUrl(url), '_blank');-->
<!--    },-->
<!--    // 下载视频-->
<!--    downloadVideo(url, name) {-->
<!--      const a = document.createElement('a');-->
<!--      a.href = this.getAbsoluteUrl(url);-->
<!--      a.download = name;-->
<!--      a.click();-->
<!--    },-->
<!--    // 获取绝对路径-->
<!--    getAbsoluteUrl(relativeUrl) {-->
<!--      const backendUrl = "http://localhost:8002";-->
<!--      return new URL(relativeUrl, backendUrl).href;-->
<!--    }-->
<!--  },-->
<!--  computed: {-->
<!--    user() {-->
<!--      return this.$store.state.user; // 从 Vuex 获取用户信息-->
<!--    }-->
<!--  },-->
<!--  mounted() {-->
<!--    this.fetchEnrolledCourses(); // 页面加载时获取已选课程ID并获取课程详情-->
<!--  }-->
<!--};-->


<!--//-->
<!--// import axios from "axios";-->
<!--// import { ElMessage } from "element-plus";-->
<!--//-->
<!--// export default {-->
<!--//   data() {-->
<!--//     return {-->
<!--//       enrolledCourseIds: [], // 存储已选课程的ID-->
<!--//       courses: [], // 存储完整的课程详情-->
<!--//       chapters: [], // 存储当前课程的章节-->
<!--//       selectedCourse: null, // 当前选择的课程对象-->
<!--//       activeChapter: null // 当前激活的章节-->
<!--//     };-->
<!--//   },-->
<!--//   methods: {-->
<!--//     // 获取学生已选课程ID-->
<!--//     async fetchEnrolledCourses() {-->
<!--//       try {-->
<!--//         const response = await axios.get(-->
<!--//           `http://localhost:8002/api/enrollments/?student_id=${this.user.student_or_teacher_id}`-->
<!--//         );-->
<!--//         this.enrolledCourseIds = response.data; // 假设返回的是课程ID数组-->
<!--//         this.fetchCourseDetails(); // 根据课程ID获取课程详情-->
<!--//       } catch (error) {-->
<!--//         console.error("获取已选课程失败:", error);-->
<!--//         ElMessage.error("获取已选课程失败");-->
<!--//       }-->
<!--//     },-->
<!--//     // 根据课程ID获取课程详情-->
<!--//     async fetchCourseDetails() {-->
<!--//       if (!this.enrolledCourseIds || this.enrolledCourseIds.length === 0) {-->
<!--//         this.courses = [];-->
<!--//         return;-->
<!--//       }-->
<!--//-->
<!--//       try {-->
<!--//         const coursePromises = this.enrolledCourseIds.map(courseId =>-->
<!--//           axios.get(`http://localhost:8002/api/courses/${courseId}/`)-->
<!--//         );-->
<!--//-->
<!--//         const courseResponses = await Promise.all(coursePromises);-->
<!--//         this.courses = courseResponses.map(response => response.data);-->
<!--//       } catch (error) {-->
<!--//         console.error("获取课程详情失败:", error);-->
<!--//         ElMessage.error("获取课程详情失败");-->
<!--//       }-->
<!--//     },-->
<!--//     // 根据课程ID获取章节和视频-->
<!--//     async fetchChaptersAndVideos(courseId) {-->
<!--//       try {-->
<!--//         // 清空当前章节和视频列表-->
<!--//         this.chapters = [];-->
<!--//         const response = await axios.get(-->
<!--//           `http://localhost:8002/api/courses/${courseId}/chapters/`-->
<!--//         );-->
<!--//         const chapters = response.data;-->
<!--//-->
<!--//         if (chapters.length > 0) {-->
<!--//           // 如果有章节，获取每个章节的视频-->
<!--//           const chapterPromises = chapters.map(chapter =>-->
<!--//             axios.get(`http://localhost:8002/material/chapters/${chapter.chapter_id}/videos/`)-->
<!--//           );-->
<!--//-->
<!--//           const chapterResponses = await Promise.all(chapterPromises);-->
<!--//           this.chapters = chapters.map((chapter, index) => ({-->
<!--//             ...chapter,-->
<!--//             videos: chapterResponses[index].data.videos-->
<!--//           }));-->
<!--//         } else {-->
<!--//           // 如果没有章节，直接获取课程的视频-->
<!--//           const response = await axios.get(-->
<!--//             `http://localhost:8002/api/student/${this.user.student_or_teacher_id}/course/${courseId}/videos/`-->
<!--//           );-->
<!--//           this.chapters = [{ chapter_name: "默认章节", videos: response.data.videos }];-->
<!--//         }-->
<!--//       } catch (error) {-->
<!--//         console.error("获取章节和视频失败:", error);-->
<!--//         ElMessage.error("获取章节和视频失败，请重新登录");-->
<!--//       }-->
<!--//     },-->
<!--//     // 选择课程-->
<!--//     selectCourse(course) {-->
<!--//       this.selectedCourse = course;-->
<!--//       this.fetchChaptersAndVideos(course.course_id);-->
<!--//     },-->
<!--//     // 播放视频-->
<!--//     playVideo(url) {-->
<!--//       window.open(this.getAbsoluteUrl(url), '_blank');-->
<!--//     },-->
<!--//     // 下载视频-->
<!--//     downloadVideo(url, name) {-->
<!--//       const a = document.createElement('a');-->
<!--//       a.href = this.getAbsoluteUrl(url);-->
<!--//       a.download = name;-->
<!--//       a.click();-->
<!--//     },-->
<!--//     // 获取绝对路径-->
<!--//     getAbsoluteUrl(relativeUrl) {-->
<!--//       const backendUrl = "http://localhost:8002";-->
<!--//       return new URL(relativeUrl, backendUrl).href;-->
<!--//     }-->
<!--//   },-->
<!--//   computed: {-->
<!--//     user() {-->
<!--//       return this.$store.state.user; // 从 Vuex 获取用户信息-->
<!--//     }-->
<!--//   },-->
<!--//   mounted() {-->
<!--//     this.fetchEnrolledCourses(); // 页面加载时获取已选课程ID并获取课程详情-->
<!--//   }-->
<!--// };-->
<!--</script>-->

<!--<style scoped>-->
<!--.container {-->
<!--  max-width: 1200px;-->
<!--  margin: 20px auto;-->
<!--  padding: 20px;-->
<!--  font-family: Arial, sans-serif;-->
<!--}-->

<!--.card-header {-->
<!--  display: flex;-->
<!--  justify-content: space-between;-->
<!--  align-items: center;-->
<!--  background-color: #f0f9eb;-->
<!--  padding: 10px;-->
<!--  border-bottom: 1px solid #e4e7ed;-->
<!--}-->

<!--.box-card {-->
<!--  margin-bottom: 20px;-->
<!--  border: 1px solid #e4e7ed;-->
<!--  border-radius: 4px;-->
<!--  background-color: #fff;-->
<!--  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);-->
<!--  transition: all 0.3s;-->
<!--}-->

<!--.box-card:hover {-->
<!--  box-shadow: 0 5px 20px 0 rgba(0, 0, 0, 0.2);-->
<!--}-->

<!--.course-card {-->
<!--  margin-bottom: 20px;-->
<!--  cursor: pointer;-->
<!--  transition: all 0.3s;-->
<!--}-->

<!--.course-card:hover {-->
<!--  transform: scale(1.05);-->
<!--  box-shadow: 0 5px 20px 0 rgba(0, 0, 0, 0.2);-->
<!--}-->

<!--.image {-->
<!--  width: 100%;-->
<!--  height: 200px;-->
<!--  object-fit: cover;-->
<!--  display: block;-->
<!--  border-radius: 4px;-->
<!--  transition: all 0.3s;-->
<!--}-->

<!--.image:hover {-->
<!--  transform: scale(1.1);-->
<!--}-->

<!--.course-info {-->
<!--  padding: 14px;-->
<!--  background-color: #f9f9f9;-->
<!--  border-radius: 0 0 4px 4px;-->
<!--}-->

<!--.course-name {-->
<!--  font-size: 16px;-->
<!--  color: #333;-->
<!--  margin: 0;-->
<!--}-->

<!--.course-id {-->
<!--  font-size: 14px;-->
<!--  color: #999;-->
<!--  margin: 5px 0 0;-->
<!--}-->
<!--</style>-->













<template>
  <div class="container">
    <!-- 课程列表 -->
    <el-card class="box-card">
      <template #header>
        <div class="card-header">
          <span>我的课程</span>
        </div>
      </template>
      <div v-if="courses.length > 0">
        <el-row :gutter="20">
          <el-col :span="6" v-for="course in courses" :key="course.course_id">
            <el-card :body-style="{ padding: '0px' }" class="course-card" @click="selectCourse(course.course_id)">
              <img :src="getAbsoluteUrl(course.course_cover)" class="image" alt="课程封面">
              <div class="course-info">
                <h3 class="course-name">{{ course.course_name }}</h3>
                <p class="course-id">编号: {{ course.course_id }}</p>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </div>
      <div v-else>
        <el-empty description="您尚未选任何课程"></el-empty>
      </div>
    </el-card>

    <!-- 视频列表 -->
    <el-card class="box-card" v-if="selectedCourse">
      <template #header>
        <div class="card-header">
          <span>课程视频</span>
        </div>
      </template>
      <div v-if="videos.length > 0">
        <el-table :data="videos" style="width: 100%">
          <el-table-column prop="video_name" label="视频名称"></el-table-column>
          <el-table-column label="操作">
            <template #default="scope">
              <el-button type="primary" @click="playVideo(scope.row.video_url, scope.row.video_id)">播放</el-button>
              <el-button type="success" @click="downloadVideo(scope.row.video_url, scope.row.video_name)">下载</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
      <div v-else>
        <el-empty description="暂无视频"></el-empty>
      </div>
    </el-card>

    <!-- 学习报告 -->
    <el-card class="box-card">
      <template #header>
        <div class="card-header">
          <span>学习报告</span>
        </div>
      </template>
      <div v-if="learningReport.length > 0">
        <el-table :data="learningReport" style="width: 100%">
          <el-table-column prop="course_name" label="课程名称"></el-table-column>
          <el-table-column prop="progress" label="学习进度"></el-table-column>
          <el-table-column prop="total_duration" label="总学习时长"></el-table-column>
        </el-table>
      </div>
      <div v-else>
        <el-empty description="暂无学习报告"></el-empty>
      </div>
    </el-card>
  </div>
</template>

<script>
import axios from "axios";
import { ElMessage } from "element-plus";

export default {
  data() {
    return {
      enrolledCourseIds: [],
      courses: [],
      videos: [],
      selectedCourse: null,
      learningReport: [],
      currentVideoId: null,
      learningDuration: 0,
      videoElement: null,
    };
  },
  methods: {
    async fetchEnrolledCourses() {
      try {
        const response = await axios.get(
          `http://localhost:8002/api/enrollments/?student_id=${this.user.student_or_teacher_id}`
        );
        this.enrolledCourseIds = response.data;
        this.fetchCourseDetails();
      } catch (error) {
        console.error("获取已选课程失败:", error);
        ElMessage.error("获取已选课程失败");
      }
    },
    async fetchCourseDetails() {
      if (!this.enrolledCourseIds || this.enrolledCourseIds.length === 0) {
        this.courses = [];
        return;
      }

      try {
        const coursePromises = this.enrolledCourseIds.map(courseId =>
          axios.get(`http://localhost:8002/api/courses/${courseId}/`)
        );

        const courseResponses = await Promise.all(coursePromises);
        this.courses = courseResponses.map(response => response.data);
      } catch (error) {
        console.error("获取课程详情失败:", error);
        ElMessage.error("获取课程详情失败");
      }
    },
    async fetchVideos(courseId) {
      try {
        this.videos = [];
        const response = await axios.get(
          `http://localhost:8002/api/student/${this.user.student_or_teacher_id}/course/${courseId}/videos/`
        );
        this.videos = response.data.videos;
      } catch (error) {
        console.error("获取视频列表失败:", error);
        ElMessage.error("获取视频列表失败，请重新登录");
      }
    },
    selectCourse(courseId) {
      this.selectedCourse = courseId;
      this.fetchVideos(courseId);
    },
    playVideo(url, videoId) {
  this.currentVideoId = videoId;
  this.learningDuration = 0;
  this.videoPlayedPercentage = 0;

  // 创建一个视频容器
  const videoContainer = document.createElement('div');
  videoContainer.style.position = 'fixed';
  videoContainer.style.top = '0';
  videoContainer.style.left = '0';
  videoContainer.style.width = '100%';
  videoContainer.style.height = '100%';
  videoContainer.style.display = 'flex';
  videoContainer.style.flexDirection = 'column';
  videoContainer.style.justifyContent = 'center';
  videoContainer.style.alignItems = 'center';
  videoContainer.style.zIndex = '1000';
  videoContainer.style.backgroundColor = 'rgba(0, 0, 0, 0.8)';
  videoContainer.style.overflow = 'hidden';
  videoContainer.classList.add('video-container'); // 添加类名以便媒体查询生效

  // 创建一个内部容器，用于固定视频和控件的大小
  const innerContainer = document.createElement('div');
  innerContainer.style.width = '80vw'; // 宽度为屏幕宽度的80%
  innerContainer.style.height = '80vh'; // 高度为屏幕高度的80%
  innerContainer.style.display = 'flex';
  innerContainer.style.flexDirection = 'column';
  innerContainer.style.justifyContent = 'space-between';
  innerContainer.style.alignItems = 'center';
  innerContainer.style.borderRadius = '15px';
  innerContainer.style.overflow = 'hidden';
  innerContainer.style.backgroundColor = 'black';

  // 创建关闭按钮
  const closeButton = document.createElement('button');
  closeButton.innerText = '关闭';
  closeButton.style.position = 'absolute';
  closeButton.style.top = '10px';
  closeButton.style.right = '10px';
  closeButton.style.zIndex = '1001';
  closeButton.style.padding = '10px 20px';
  closeButton.style.backgroundColor = '#FF5733';
  closeButton.style.color = 'white';
  closeButton.style.border = 'none';
  closeButton.style.borderRadius = '10px';
  closeButton.style.cursor = 'pointer';
  closeButton.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.3)';
  closeButton.style.transition = 'background-color 0.3s ease';

  closeButton.addEventListener('click', () => {
    this.stopLearningTimer();
    document.body.removeChild(videoContainer);
  });

  closeButton.addEventListener('mouseover', () => {
    closeButton.style.backgroundColor = '#E04828';
  });

  closeButton.addEventListener('mouseout', () => {
    closeButton.style.backgroundColor = '#FF5733';
  });

  // 创建一个新的 video 元素
  this.videoElement = document.createElement('video');
  this.videoElement.src = this.getAbsoluteUrl(url);
  this.videoElement.autoplay = true;
  this.videoElement.style.maxWidth = '100%';
  this.videoElement.style.maxHeight = '70%'; // 视频高度占内部容器的70%
  this.videoElement.style.borderRadius = '10px';
  this.videoElement.style.boxShadow = '0 6px 12px rgba(0, 0, 0, 0.4)';
  this.videoElement.style.transition = 'box-shadow 0.3s ease';

  // 创建控制栏容器
  const controlBarContainer = document.createElement('div');
  controlBarContainer.style.width = '100%'; // 控制栏宽度与内部容器一致
  controlBarContainer.style.display = 'flex';
  controlBarContainer.style.justifyContent = 'space-between';
  controlBarContainer.style.alignItems = 'center';
  controlBarContainer.style.padding = '10px';
  controlBarContainer.style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
  controlBarContainer.style.borderBottomLeftRadius = '10px';
  controlBarContainer.style.borderBottomRightRadius = '10px';

  // 创建自定义播放/暂停按钮
  const playPauseButton = document.createElement('button');
  playPauseButton.innerText = '播放';
  playPauseButton.style.padding = '10px 20px';
  playPauseButton.style.backgroundColor = '#33FF57';
  playPauseButton.style.color = 'white';
  playPauseButton.style.border = 'none';
  playPauseButton.style.borderRadius = '10px';
  playPauseButton.style.cursor = 'pointer';
  playPauseButton.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.3)';
  playPauseButton.style.transition = 'background-color 0.3s ease';

  playPauseButton.addEventListener('click', () => {
    if (this.videoElement.paused) {
      this.videoElement.play();
      playPauseButton.innerText = '暂停';
    } else {
      this.videoElement.pause();
      playPauseButton.innerText = '播放';
    }
  });

  playPauseButton.addEventListener('mouseover', () => {
    playPauseButton.style.backgroundColor = '#28E048';
  });

  playPauseButton.addEventListener('mouseout', () => {
    playPauseButton.style.backgroundColor = '#33FF57';
  });

  // 创建自定义音量控制
  const volumeContainer = document.createElement('div');
  volumeContainer.style.display = 'flex';
  volumeContainer.style.alignItems = 'center';

  const volumeButton = document.createElement('button');
  volumeButton.innerText = '音量';
  volumeButton.style.padding = '10px 20px';
  volumeButton.style.backgroundColor = '#3357FF';
  volumeButton.style.color = 'white';
  volumeButton.style.border = 'none';
  volumeButton.style.borderRadius = '10px';
  volumeButton.style.cursor = 'pointer';
  volumeButton.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.3)';
  volumeButton.style.transition = 'background-color 0.3s ease';

  volumeButton.addEventListener('click', () => {
    if (this.videoElement.volume === 0) {
      this.videoElement.volume = 0.5;
    } else {
      this.videoElement.volume = 0;
    }
  });

  volumeButton.addEventListener('mouseover', () => {
    volumeButton.style.backgroundColor = '#2848E0';
  });

  volumeButton.addEventListener('mouseout', () => {
    volumeButton.style.backgroundColor = '#3357FF';
  });

  const volumeSlider = document.createElement('input');
  volumeSlider.type = 'range';
  volumeSlider.min = '0';
  volumeSlider.max = '1';
  volumeSlider.step = '0.01';
  volumeSlider.value = '0.5';
  volumeSlider.style.width = '100px';
  volumeSlider.style.marginLeft = '10px';
  volumeSlider.style.accentColor = '#33FF57';

  volumeSlider.addEventListener('input', () => {
    this.videoElement.volume = volumeSlider.value;
  });

  volumeContainer.appendChild(volumeButton);
  volumeContainer.appendChild(volumeSlider);

  // 创建自定义全屏按钮
  const fullscreenButton = document.createElement('button');
  fullscreenButton.innerText = '全屏';
  fullscreenButton.style.padding = '10px 20px';
  fullscreenButton.style.backgroundColor = '#FF3357';
  fullscreenButton.style.color = 'white';
  fullscreenButton.style.border = 'none';
  fullscreenButton.style.borderRadius = '10px';
  fullscreenButton.style.cursor = 'pointer';
  fullscreenButton.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.3)';
  fullscreenButton.style.transition = 'background-color 0.3s ease';

  fullscreenButton.addEventListener('click', () => {
    if (!document.fullscreenElement) {
      videoContainer.requestFullscreen().catch(err => {
        // 处理无法进入全屏的情况
      });
    } else {
      document.exitFullscreen().catch(err => {
        // 处理无法退出全屏的情况
      });
    }
  });

  fullscreenButton.addEventListener('mouseover', () => {
    fullscreenButton.style.backgroundColor = '#E02848';
  });

  fullscreenButton.addEventListener('mouseout', () => {
    fullscreenButton.style.backgroundColor = '#FF3357';
  });

  // 创建自定义进度条容器
  const progressBarContainer = document.createElement('div');
  progressBarContainer.style.width = '100%'; // 进度条宽度与内部容器一致
  progressBarContainer.style.height = '10px';
  progressBarContainer.style.backgroundColor = '#ddd';
  progressBarContainer.style.marginTop = '10px';
  progressBarContainer.style.borderRadius = '5px';
  progressBarContainer.style.transition = 'background-color 0.3s ease';

  // 创建自定义进度条
  const progressBar = document.createElement('div');
  progressBar.style.width = '0%';
  progressBar.style.height = '100%';
  progressBar.style.backgroundColor = '#33FF57';
  progressBar.style.borderRadius = '5px';
  progressBar.style.transition = 'width 0.3s ease';

  progressBarContainer.appendChild(progressBar);

  // 创建重新播放按钮
  const replayButton = document.createElement('button');
  replayButton.innerText = '重新播放';
  replayButton.style.marginTop = '10px';
  replayButton.style.padding = '10px 20px';
  replayButton.style.backgroundColor = '#FF5733';
  replayButton.style.color = 'white';
  replayButton.style.border = 'none';
  replayButton.style.borderRadius = '10px';
  replayButton.style.cursor = 'pointer';
  replayButton.style.display = 'none';
  replayButton.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.3)';
  replayButton.style.transition = 'background-color 0.3s ease';

  replayButton.addEventListener('click', () => {
    this.videoElement.currentTime = 0;
    this.videoElement.play();
    replayButton.style.display = 'none';
  });

  replayButton.addEventListener('mouseover', () => {
    replayButton.style.backgroundColor = '#E04828';
  });

  replayButton.addEventListener('mouseout', () => {
    replayButton.style.backgroundColor = '#FF5733';
  });

  // 将控制栏内的按钮和进度条添加到控制栏容器中
  controlBarContainer.appendChild(playPauseButton);
  controlBarContainer.appendChild(volumeContainer);
  controlBarContainer.appendChild(fullscreenButton);

  // 将关闭按钮、视频元素、控制栏容器和重新播放按钮添加到内部容器中
  innerContainer.appendChild(closeButton);
  innerContainer.appendChild(this.videoElement);
  innerContainer.appendChild(progressBarContainer);
  innerContainer.appendChild(controlBarContainer);
  innerContainer.appendChild(replayButton);

  // 将内部容器添加到视频容器中
  videoContainer.appendChild(innerContainer);

  // 将容器添加到页面中
  document.body.appendChild(videoContainer);

  // 从本地存储中读取上次的播放进度
  const savedProgress = localStorage.getItem(`videoProgress_${videoId}`);
  if (savedProgress) {
    this.videoElement.currentTime = parseFloat(savedProgress);
  }

  // 监听视频播放事件
  this.videoElement.addEventListener('play', () => {
    this.startLearningTimer();
  });

  // 监听视频结束事件
  this.videoElement.addEventListener('ended', () => {
    this.stopLearningTimer();
    this.recordLearningProgress(true);
    replayButton.style.display = 'block';
  });

  // 监听视频播放位置变化事件
  this.videoElement.addEventListener('timeupdate', () => {
    this.updateLearningProgress();
    const percent = (this.videoElement.currentTime / this.videoElement.duration) * 100;
    progressBar.style.width = `${percent}%`;
    if (Math.floor(this.videoElement.currentTime) % 1 === 0) {
      localStorage.setItem(`videoProgress_${videoId}`, this.videoElement.currentTime);
    }
  });
//   this.videoElement.addEventListener('seeking', (event) => {
//   event.preventDefault(); // 阻止默认的进度条拖动行为
//   const savedProgress = localStorage.getItem(`videoProgress_${videoId}`);
//   if (savedProgress) {
//     this.videoElement.currentTime = parseFloat(savedProgress);
//   }
// });

  // 防止用户改变播放速度
  this.videoElement.addEventListener('ratechange', () => {
    if (this.videoElement.playbackRate !== 1.0) {
      this.videoElement.playbackRate = 1.0;
    }
  });
},
    downloadVideo(url, name) {
      // 创建一个模态窗口容器
      const modalContainer = document.createElement('div');
      modalContainer.style.position = 'fixed';
      modalContainer.style.top = '0';
      modalContainer.style.left = '0';
      modalContainer.style.width = '100%';
      modalContainer.style.height = '100%';
      modalContainer.style.display = 'flex';
      modalContainer.style.justifyContent = 'center';
      modalContainer.style.alignItems = 'center';
      modalContainer.style.zIndex = '1000';
      modalContainer.style.backgroundColor = 'rgba(0, 0, 0, 0.5)'; // 添加半透明背景

      // 创建一个模态窗口内容区域
      const modalContent = document.createElement('div');
      modalContent.style.backgroundColor = 'white';
      modalContent.style.padding = '20px';
      modalContent.style.borderRadius = '10px';
      modalContent.style.boxShadow = '0 4px 10px rgba(0, 0, 0, 0.2)';
      modalContent.style.textAlign = 'center';

      // 创建下载按钮
      const downloadButton = document.createElement('button');
      downloadButton.innerText = '下载';
      downloadButton.style.margin = '10px';
      downloadButton.style.padding = '10px 20px';
      downloadButton.style.backgroundColor = '#4CAF50';
      downloadButton.style.color = 'white';
      downloadButton.style.border = 'none';
      downloadButton.style.borderRadius = '5px';
      downloadButton.style.cursor = 'pointer';

      // 下载按钮的点击事件处理程序
      downloadButton.addEventListener('click', () => {
        // 创建一个 <a> 标签
        const a = document.createElement('a');
        a.href = this.getAbsoluteUrl(url); // 设置下载链接
        a.download = name; // 设置下载文件的名称
        document.body.appendChild(a); // 将 <a> 标签添加到页面中
        a.click(); // 触发点击事件，开始下载
        document.body.removeChild(a); // 移除 <a> 标签
        document.body.removeChild(modalContainer); // 关闭模态窗口
      });

      // 创建关闭按钮
      const closeButton = document.createElement('button');
      closeButton.innerText = '关闭';
      closeButton.style.margin = '10px';
      closeButton.style.padding = '10px 20px';
      closeButton.style.backgroundColor = '#f44336';
      closeButton.style.color = 'white';
      closeButton.style.border = 'none';
      closeButton.style.borderRadius = '5px';
      closeButton.style.cursor = 'pointer';

      // 关闭按钮的点击事件处理程序
      closeButton.addEventListener('click', () => {
        document.body.removeChild(modalContainer); // 移除模态窗口容器
      });

      // 将下载按钮和关闭按钮添加到模态窗口内容区域
      modalContent.appendChild(downloadButton);
      modalContent.appendChild(closeButton);

      // 将模态窗口内容区域添加到模态窗口容器
      modalContainer.appendChild(modalContent);

      // 将模态窗口容器添加到页面中
      document.body.appendChild(modalContainer);
    },
    getAbsoluteUrl(relativeUrl) {
      const backendUrl = "http://localhost:8002";
      return new URL(relativeUrl, backendUrl).href;
    },
    // startLearningTimer() {
    //   this.learningTimer = setInterval(() => {
    //     this.learningDuration += 1; // 每秒增加 1 秒
    //   }, 1000);
    // },
    // stopLearningTimer() {
    //   clearInterval(this.learningTimer);
    //   this.learningTimer = null;
    // },
    startLearningTimer() {
      if (this.learningTimer) return; // 如果定时器已经启动，则直接返回
      this.learningTimer = setInterval(() => {
        this.learningDuration += 1 / 60; // 每秒增加 1/60 分钟
      }, 1000);
    },
    stopLearningTimer() {
      clearInterval(this.learningTimer); // 清除定时器
      this.learningTimer = null; // 将定时器引用设置为 null
    },
    // beforeDestroy() {
    //   this.stopLearningTimer(); // 在组件销毁前停止定时器
    // },

    async recordLearningProgress(isCompleted) {
      try {
        const response = await axios.post(
          `http://localhost:8002/api/learning-records/`,
          {
            student_id: this.user.student_or_teacher_id,
            course_id: this.selectedCourse,
            material_id: null, // 假设没有材料 ID
            video_id: this.currentVideoId,
            content: "学习视频",
            duration: this.learningDuration,
            is_completed: isCompleted, // 标记视频是否已完播
          }
        );
        console.log("学习记录成功:", response.data);
        this.updateLearningReport();
      } catch (error) {
        console.error("记录学习进度失败:", error);
        ElMessage.error("记录学习进度失败");
      }
    },
    async updateLearningProgress() {
      try {
        const progress = this.videoElement.currentTime / this.videoElement.duration * 100;
        const response = await axios.patch(
          `http://localhost:8002/api/learning-progress/${this.user.student_or_teacher_id}/${this.selectedCourse}/`,
          {
            progress: progress,
          }
        );
        console.log("更新学习进度成功:", response.data);
      } catch (error) {
        console.error("更新学习进度失败:", error);
        ElMessage.error("更新学习进度失败");
      }
    },
    async updateLearningReport() {
      try {
        const response = await axios.get(
          `http://localhost:8002/api/learning-report/${this.user.student_or_teacher_id}/`
        );
        this.learningReport = response.data.report;
      } catch (error) {
        console.error("获取学习报告失败:", error);
        ElMessage.error("获取学习报告失败");
      }
    },
  },
  computed: {
    user() {
      return this.$store.state.user;
    },
  },
  mounted() {
    this.fetchEnrolledCourses();
    this.updateLearningReport();
  },
};
</script>

<style scoped>
.container {
  max-width: 1200px;
  margin: 20px auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #f0f9eb;
  padding: 10px;
  border-bottom: 1px solid #e4e7ed;
}

.box-card {
  margin-bottom: 20px;
  border: 1px solid #e4e7ed;
  border-radius: 4px;
  background-color: #fff;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  transition: all 0.3s;
}

.box-card:hover {
  box-shadow: 0 5px 20px 0 rgba(0, 0, 0, 0.2);
}

.course-card {
  margin-bottom: 20px;
  cursor: pointer;
  transition: all 0.3s;
}

.course-card:hover {
  transform: scale(1.05);
  box-shadow: 0 5px 20px 0 rgba(0, 0, 0, 0.2);
}

.image {
  width: 100%;
  height: 200px;
  object-fit: cover;
  display: block;
  border-radius: 4px;
  transition: all 0.3s;
}

.image:hover {
  transform: scale(1.1);
}

.course-info {
  padding: 14px;
  background-color: #f9f9f9;
  border-radius: 0 0 4px 4px;
}

.course-name {
  font-size: 16px;
  color: #333;
  margin: 0;
}

.course-id {
  font-size: 14px;
  color: #999;
  margin: 5px 0 0;
}

/* 新增样式 */
.modal-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  background-color: rgba(0, 0, 0, 0.5);
}

.modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  text-align: center;
}

.modal-content button {
  margin: 10px;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.modal-content button.download-button {
  background-color: #4CAF50;
  color: white;
}

.modal-content button.close-button {
  background-color: #f44336;
  color: white;
}
</style>