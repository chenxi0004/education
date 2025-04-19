<!--<template>-->
<!--  <div>-->
<!--    <h1>已选课程</h1>-->
<!--    <ul>-->
<!--      <li v-for="course in courses" :key="course.course_id">-->
<!--        <img :src="course.course_cover" alt="Course Cover" style="width: 100px; height: 100px;">-->
<!--        {{ course.course_id }} - {{ course.course_name }}-->
<!--        <button @click="viewExams(course.course_id)">查看考试</button>-->
<!--      </li>-->
<!--    </ul>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--import { ref, onMounted } from 'vue';-->
<!--import axios from 'axios';-->
<!--import {useStore} from "vuex";-->

<!--export default {-->
<!--  setup() {-->
<!--    const courses = ref([]);-->
<!--    const store = useStore();-->
<!--    const user = store.state.user;-->

<!--    const fetchCourses = async () => {-->
<!--      try {-->
<!--        const response = await axios.get('http://localhost:8002/api/enrollments/', {-->
<!--          params: {student_id: user.student_or_teacher_id} // 假设从用户信息中获取学生ID-->
<!--        });-->
<!--        courses.value = response.data;-->
<!--      } catch (error) {-->
<!--        console.error("获取课程列表失败:", error);-->
<!--      }-->
<!--    };-->

<!--    const viewExams = (courseId) => {-->
<!--      // 跳转到考试列表页面-->
<!--      window.location.href = `/exams/${courseId}`;-->
<!--    };-->

<!--    onMounted(fetchCourses);-->

<!--    return {-->
<!--      courses,-->
<!--      viewExams,-->
<!--    };-->
<!--  },-->
<!--};-->
<!--</script>-->





<template>
  <el-form :model="examForm" label-width="120px">
    <el-form-item label="所属课程">
      <el-select v-model="examForm.course_id" placeholder="选择课程">
        <el-option
          v-for="course in courses"
          :key="course.course_id"
          :label="course.course_name"
          :value="course.course_id"
        />
      </el-select>
    </el-form-item>

    <el-form-item label="考试名称">
      <el-input v-model="examForm.exam_name" />
    </el-form-item>

    <el-form-item label="考试类型">
      <el-select v-model="examForm.exam_type">
        <el-option
          v-for="type in examTypes"
          :key="type.value"
          :label="type.label"
          :value="type.value"
        />
      </el-select>
    </el-form-item>

    <question-editor :questions="questions" @update:questions="questions = $event" />

    <el-form-item>
      <el-button type="primary" @click="submitExam">发布考试</el-button>
    </el-form-item>
  </el-form>
</template>

<script setup>
import { ref } from 'vue'
import QuestionEditor from './QuestionEditor.vue'
import axios from 'axios'

const emit = defineEmits(['success'])
const examForm = ref({
  course_id: '',
  exam_name: '',
  exam_type: 'custom',
  total_score: 100,
  time_limit: 60
})

const questions = ref([])
const examTypes = [
  { value: 'midterm', label: '期中考试' },
  { value: 'final', label: '期末考试' },
  { value: 'quiz', label: '小测验' },
  { value: 'custom', label: '自定义考试' }
]

const submitExam = async () => {
  try {
    // 先创建考试
    const examRes = await axios.post('http://localhost:8002/api/teacher/exam/create/', examForm.value)

    // 再创建题目
    const questionPromises = questions.value.map(async q => {
      return axios.post(`http://localhost:8002/api/teacher/exam/${examRes.data.exam_id}/questions/`, q)
    })

    await Promise.all(questionPromises)
    emit('success')
  } catch (error) {
    ElMessage.error('发布失败: ' + error.message)
  }
}
</script>