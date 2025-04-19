<template>
  <div class="upload-container">
    <h2>上传课程资料</h2>
    <form @submit.prevent="uploadMaterial">
      <div class="form-group">
        <label for="course_id">课程编号</label>
        <input
          type="text"
          id="course_id"
          v-model="courseId"
          required
        />
      </div>
      <div class="form-group">
        <label for="material_name">资料名称</label>
        <input
          type="text"
          id="material_name"
          v-model="materialName"
          required
        />
      </div>
      <div class="form-group">
        <label for="material_file">选择文件</label>
        <input
          type="file"
          id="material_file"
          @change="handleFileChange"
          required
        />
      </div>
      <div class="form-group">
        <button type="submit">上传</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import { ElMessage } from "element-plus";
import {useStore} from 'vuex'
const store = useStore()
const user = store.state.user
const courseId = ref("");
const materialName = ref("");
const materialFile = ref(null);

const handleFileChange = (event) => {
  materialFile.value = event.target.files[0];
};

const uploadMaterial = async () => {
  if (!materialFile.value) {
    alert("请选择文件");
    return;
  }

  const formData = new FormData();
  formData.append("course_id", courseId.value);
  formData.append("material_name", materialName.value);
  formData.append("material_file", materialFile.value);
  formData.append("student_or_teacher_id", user.student_or_teacher_id);

  try {
    const response = await axios.post(
      "http://localhost:8002/material/materials/",
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }
    );
    ElMessage.success("上传成功");
    // alert("上传成功");
  } catch (error) {
    if (error.response && error.response.status === 403) {
          // 捕获 403 错误并显示特定提示
          ElMessage.error("您没有权限上传资料到该课程。");
        } else {
          // 其他错误
          ElMessage.error("资料上传失败");
        }
    console.error("上传失败:", error);
    // ElMessage.error("上传失败");
    // alert("上传失败");
  }
};
</script>

<style scoped>
.upload-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input[type="text"],
input[type="file"],
button {
  width: 100%;
  padding: 10px;
  box-sizing: border-box;
}

button {
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>

<!--<template>-->
<!--  <div class="upload-container">-->
<!--    <h2>上传课程资料</h2>-->
<!--    <form @submit.prevent="uploadMaterial">-->
<!--      <div class="form-group">-->
<!--        <label for="material_name">资料名称</label>-->
<!--        <input-->
<!--          type="text"-->
<!--          id="material_name"-->
<!--          v-model="materialName"-->
<!--          required-->
<!--        />-->
<!--      </div>-->
<!--      <div class="form-group">-->
<!--        <label for="material_file">选择文件</label>-->
<!--        <input-->
<!--          type="file"-->
<!--          id="material_file"-->
<!--          @change="handleFileChange"-->
<!--          required-->
<!--        />-->
<!--      </div>-->
<!--      <div class="form-group">-->
<!--        <button type="submit">上传</button>-->
<!--      </div>-->
<!--    </form>-->
<!--  </div>-->
<!--</template>-->

<!--<script setup>-->
<!--import { ref } from "vue";-->
<!--import axios from "axios";-->
<!--import { useStore } from "vuex";-->

<!--const store = useStore();-->
<!--const materialName = ref("");-->
<!--const materialFile = ref(null);-->

<!--const handleFileChange = (event) => {-->
<!--  materialFile.value = event.target.files[0];-->
<!--};-->

<!--const uploadMaterial = async () => {-->
<!--  if (!materialFile.value) {-->
<!--    alert("请选择文件");-->
<!--    return;-->
<!--  }-->

<!--  // 从 Vuex 中获取当前用户的 student_or_teacher_id-->
<!--  const userId = store.state.user.student_or_teacher_id;-->
<!--  if (!userId) {-->
<!--    alert("未获取到用户信息，请重新登录");-->
<!--    return;-->
<!--  }-->

<!--  // 查询课程表以获取课程编号-->
<!--  let courseId;-->
<!--  try {-->
<!--    const response = await axios.get(`http://localhost:8002/api/courses/search/?teacher_id=${userId}`);-->
<!--    if (response.data.length > 0) {-->
<!--      courseId = response.data[0].course_id; // 假设返回的第一个课程是目标课程-->
<!--    } else {-->
<!--      alert("未找到课程，请确保您有相关课程");-->
<!--      return;-->
<!--    }-->
<!--  } catch (error) {-->
<!--    console.error("获取课程编号失败:", error);-->
<!--    alert("获取课程编号失败");-->
<!--    return;-->
<!--  }-->

<!--  const formData = new FormData();-->
<!--  formData.append("course_id", courseId);-->
<!--  formData.append("material_name", materialName.value);-->
<!--  formData.append("material_file", materialFile.value);-->

<!--  try {-->
<!--    const response = await axios.post(-->
<!--      "http://localhost:8002/material/materials/",-->
<!--      formData,-->
<!--      {-->
<!--        headers: {-->
<!--          "Content-Type": "multipart/form-data",-->
<!--        },-->
<!--      }-->
<!--    );-->
<!--    alert("上传成功");-->
<!--  } catch (error) {-->
<!--    console.error("上传失败:", error);-->
<!--    alert("上传失败");-->
<!--  }-->
<!--};-->
<!--</script>-->

<!--<style scoped>-->
<!--.upload-container {-->
<!--  max-width: 400px;-->
<!--  margin: 0 auto;-->
<!--  padding: 20px;-->
<!--  border: 1px solid #ccc;-->
<!--  border-radius: 8px;-->
<!--}-->

<!--.form-group {-->
<!--  margin-bottom: 15px;-->
<!--}-->

<!--label {-->
<!--  display: block;-->
<!--  margin-bottom: 5px;-->
<!--}-->

<!--input[type="text"],-->
<!--input[type="file"],-->
<!--button {-->
<!--  width: 100%;-->
<!--  padding: 10px;-->
<!--  box-sizing: border-box;-->
<!--}-->

<!--button {-->
<!--  background-color: #007bff;-->
<!--  color: white;-->
<!--  border: none;-->
<!--  cursor: pointer;-->
<!--}-->

<!--button:hover {-->
<!--  background-color: #0056b3;-->
<!--}-->
<!--</style>-->