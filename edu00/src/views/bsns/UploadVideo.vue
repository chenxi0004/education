<!--<template>-->
<!--  <el-card class="upload-card">-->
<!--    <el-form ref="uploadForm" :model="form" label-width="120px" :rules="rules">-->
<!--      <el-form-item label="选择课程" prop="courseId">-->
<!--        <el-select v-model="form.courseId" placeholder="请选择课程" style="width: 100%">-->
<!--          <el-option-->
<!--            v-for="course in courses"-->
<!--            :key="course.course_id"-->
<!--            :label="course.course_name"-->
<!--            :value="course.course_id"-->
<!--          ></el-option>-->
<!--        </el-select>-->
<!--      </el-form-item>-->

<!--      <el-form-item label="上传视频" prop="videoFile">-->
<!--        <el-upload-->
<!--          ref="videoUpload"-->
<!--          class="upload-demo"-->
<!--          :headers="uploadHeaders"-->
<!--          :file-list="fileList"-->
<!--          :before-upload="handleBeforeUpload"-->
<!--          :on-progress="handleProgress"-->
<!--          :on-success="handleSuccess"-->
<!--          :on-error="handleError"-->
<!--          :on-remove="handleRemove"-->
<!--          :limit="1"-->
<!--          accept="video/mp4"-->
<!--          :action="uploadUrl"-->
<!--          name="video_file"-->
<!--        >-->
<!--          <el-button size="small" type="primary">点击上传</el-button>-->
<!--          <template #tip>-->
<!--            <div class="el-upload__tip">只能上传MP4文件，且不超过500MB</div>-->
<!--          </template>-->
<!--        </el-upload>-->
<!--      </el-form-item>-->

<!--      <el-form-item>-->
<!--        <el-button type="primary" @click="uploadVideo">提交</el-button>-->
<!--        <el-button @click="resetForm">重置</el-button>-->
<!--      </el-form-item>-->
<!--    </el-form>-->
<!--  </el-card>-->
<!--</template>-->

<!--<script setup>-->
<!--import { ref, reactive, onMounted, watch,computed } from "vue";-->
<!--import { ElMessage } from "element-plus";-->
<!--import axios from "axios";-->
<!--import { useStore } from "vuex";-->

<!--const store = useStore(); // 获取 Vuex 的 store-->
<!--const user = store.state.user; // 从 Vuex 中获取用户信息-->
<!--// const user = computed(() => store.state.user);-->

<!--const form = reactive({-->
<!--  courseId: "",-->
<!--  videoFile: null,-->
<!--});-->

<!--const courses = ref([]);-->
<!--const fileList = ref([]);-->
<!--const uploadHeaders = ref({-->
<!--  // Authorization: `Bearer ${localStorage.getItem("token")}`, // 假设使用 JWT Token-->
<!--});-->
<!--const uploadData = ref({});-->
<!--const uploadUrl = ref("http://localhost:8002/material/upload-video/");-->
<!--const videoUpload = ref(null); // 定义 ref-->

<!--const rules = {-->
<!--  courseId: [-->
<!--    { required: true, message: "请选择课程", trigger: "change" },-->
<!--  ],-->
<!--  videoFile: [-->
<!--    { required: true, message: "请上传视频文件", trigger: "blur" },-->
<!--  ],-->
<!--};-->

<!--const fetchCourses = async () => {-->
<!--  try {-->
<!--    const response = await axios.get("http://localhost:8002/api/courses/");-->
<!--    courses.value = response.data;-->
<!--  } catch (error) {-->
<!--    ElMessage.error("获取课程列表失败");-->
<!--  }-->
<!--};-->

<!--watch(() => form.courseId, (newVal) => {-->
<!--  if (newVal) {-->
<!--    uploadUrl.value = `http://localhost:8002/material/upload-video/${newVal}/`;-->
<!--    console.log(user.student_or_teacher_id);-->

<!--  }-->
<!--});-->
<!--watch(() => store.state.user, (newUser) => {-->
<!--  user.value = newUser;-->
<!--});-->

<!--const handleBeforeUpload = (file) => {-->
<!--  const isMP4 = file.type === "video/mp4";-->
<!--  const isLt500M = file.size / 1024 / 1024 < 500;-->

<!--  if (!isMP4) {-->
<!--    ElMessage.error("只能上传MP4格式的视频");-->
<!--  }-->
<!--  if (!isLt500M) {-->
<!--    ElMessage.error("视频大小不能超过500MB");-->
<!--  }-->

<!--  return isMP4 && isLt500M;-->
<!--};-->

<!--const handleProgress = (event, file) => {-->
<!--  ElMessage.info(`上传中... ${event.percent.toFixed(0)}%`);-->
<!--};-->

<!--const handleSuccess = (response, file) => {-->
<!--  ElMessage.success("视频上传成功");-->
<!--  fileList.value = [];-->
<!--  form.videoFile = null;-->
<!--};-->

<!--const handleError = (error, file) => {-->
<!--  ElMessage.error("视频上传失败");-->
<!--};-->

<!--const handleRemove = (file, fileList) => {-->
<!--  form.videoFile = null;-->
<!--};-->

<!--const uploadVideo = async () => {-->
<!--  // 动态获取用户信息-->
<!--  const user = store.state.user;-->
<!--  // const user = computed(() => store.state.user);-->
<!--  if (!form.courseId) {-->
<!--    ElMessage.error("请选择课程");-->
<!--    return;-->
<!--  }-->

<!--  if (fileList.value.length === 0) {-->
<!--    ElMessage.error("请上传视频文件");-->
<!--    return;-->
<!--  }-->

<!--  if (!user || !user.student_or_teacher_id) {-->
<!--    ElMessage.error("用户信息未找到");-->
<!--    return;-->
<!--  }-->

<!--  const formData = new FormData();-->
<!--  formData.append("course_id", form.courseId);-->
<!--  formData.append("video_file", fileList.value[0].raw);-->
<!--  formData.append("student_or_teacher_id", user.student_or_teacher_id);-->
<!--  console.log(formData.get("student_or_teacher_id")); // 检查是否正确添加-->
<!--  // 确保 form.courseId 有值后再设置 uploadUrl-->
<!--  uploadUrl.value = `http://localhost:8002/material/upload-video/${form.courseId}/`;-->

<!--  try {-->
<!--    const response = await axios.post(uploadUrl.value, formData, {-->
<!--      headers: {-->
<!--        "Content-Type": "multipart/form-data",-->
<!--        // Authorization: `Bearer ${localStorage.getItem("token")}`-->
<!--      }-->
<!--    });-->
<!--    ElMessage.success("视频上传成功");-->
<!--    fileList.value = [];-->
<!--    form.videoFile = null;-->
<!--  } catch (error) {-->
<!--    if (error.response && error.response.status === 403) {-->
<!--      // 捕获 403 错误并显示特定提示-->
<!--      ElMessage.error("您没有权限上传视频到该课程。");-->
<!--      console.log(user.student_or_teacher_id)-->
<!--    } else {-->
<!--      // 其他错误-->
<!--      ElMessage.error("视频上传失败");-->
<!--    }-->
<!--    console.error("Upload Error:", error);-->
<!--  }-->
<!--};-->

<!--const resetForm = () => {-->
<!--  form.courseId = "";-->
<!--  form.videoFile = null;-->
<!--  fileList.value = [];-->
<!--};-->

<!--onMounted(() => {-->
<!--  fetchCourses();-->
<!--});-->
<!--</script>-->

<!--<style scoped>-->
<!--.upload-card {-->
<!--  max-width: 600px;-->
<!--  margin: 20px auto;-->
<!--}-->
<!--</style>-->




<template>
  <el-card class="upload-card">
    <el-form ref="uploadForm" :model="form" label-width="120px" :rules="rules">
      <el-form-item label="选择课程" prop="courseId">
        <el-select v-model="form.courseId" placeholder="请选择课程" style="width: 100%">
          <el-option
            v-for="course in courses"
            :key="course.course_id"
            :label="course.course_name"
            :value="course.course_id"
          ></el-option>
        </el-select>
      </el-form-item>

      <el-form-item label="上传视频" prop="videoFile">
        <el-upload
          ref="videoUpload"
          class="upload-demo"
          :headers="uploadHeaders"
          :file-list="fileList"
          :before-upload="handleBeforeUpload"
          :on-progress="handleProgress"
          :on-success="handleSuccess"
          :on-error="handleError"
          :on-remove="handleRemove"
          :limit="1"
          accept="video/mp4"
          :action="uploadUrl"
          name="video_file"
          :auto-upload="false"
          :on-change="handleChange"
        >
          <el-button size="small" type="primary">点击上传</el-button>
          <template #tip>
            <div class="el-upload__tip">只能上传MP4文件，且不超过500MB</div>
          </template>
        </el-upload>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="uploadVideo">提交</el-button>
        <el-button @click="resetForm">重置</el-button>
      </el-form-item>
    </el-form>
  </el-card>
</template>

<script setup>
import { ref, reactive, onMounted,watch } from "vue";
import { ElMessage } from "element-plus";
import axios from "axios";
import { useStore } from "vuex";

const store = useStore();
const user = store.state.user;

const form = reactive({
  courseId: "",
  videoFile: null,
});

const courses = ref([]);
const fileList = ref([]);
const uploadHeaders = ref({});
const uploadUrl = ref("http://localhost:8002/material/upload-video/");
const videoUpload = ref(null);

const rules = {
  courseId: [
    { required: true, message: "请选择课程", trigger: "change" },
  ],
  videoFile: [
    { required: true, message: "请上传视频文件", trigger: "blur" },
  ],
};

const fetchCourses = async () => {
  try {
    const response = await axios.get("http://localhost:8002/api/courses/", {
      params: {
        teacher_id: user.student_or_teacher_id // 传递当前教师的 ID
      }});
    courses.value = response.data;
  } catch (error) {
    ElMessage.error("获取课程列表失败");
  }
};

watch(() => form.courseId, (newVal) => {
  if (newVal) {
    uploadUrl.value = `http://localhost:8002/material/upload-video/${newVal}/`;
  }
});

const handleBeforeUpload = (file) => {
  const isMP4 = file.type === "video/mp4";
  const isLt500M = file.size / 1024 / 1024 < 500;

  if (!isMP4) {
    ElMessage.error("只能上传MP4格式的视频");
  }
  if (!isLt500M) {
    ElMessage.error("视频大小不能超过500MB");
  }

  return isMP4 && isLt500M;
};

const handleProgress = (event, file) => {
  ElMessage.info(`上传中... ${event.percent.toFixed(0)}%`);
};

const handleSuccess = (response, file) => {
  ElMessage.success("视频上传成功");
  fileList.value = [];
  form.videoFile = null;
};

const handleError = (error, file) => {
  ElMessage.error("视频上传失败");
};

const handleRemove = (file, fileList) => {
  form.videoFile = null;
};

const handleChange = (file, fileList) => {
  form.videoFile = file.raw; // 同步文件到表单数据
  fileList.value = fileList; // 确保 fileList 的更新
};

const uploadVideo = async () => {
  if (!form.courseId) {
    ElMessage.error("请选择课程");
    return;
  }

  if (!form.videoFile) {
    ElMessage.error("请上传视频文件");
    return;
  }

  if (!user || !user.student_or_teacher_id) {
    ElMessage.error("用户信息未找到");
    return;
  }

  uploadUrl.value = `http://localhost:8002/material/upload-video/${form.courseId}/`;

  try {
    videoUpload.value.submit(); // 手动触发上传
  } catch (error) {
    ElMessage.error("视频上传失败");
    console.error("Upload Error:", error);
  }
};

const resetForm = () => {
  form.courseId = "";
  form.videoFile = null;
  fileList.value = [];
};

onMounted(() => {
  fetchCourses();
});
</script>

<style scoped>
.upload-card {
  max-width: 600px;
  margin: 20px auto;
}
</style>






