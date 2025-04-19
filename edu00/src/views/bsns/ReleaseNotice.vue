<!--<template>-->
<!--  <div class="send-notification-container">-->
<!--    <h1 class="title">📩 发送新通知</h1>-->
<!--    <form @submit.prevent="sendNotification" class="notification-form">-->
<!--      <div class="form-group">-->
<!--        <label class="form-label" for="studentId">学生ID</label>-->
<!--        <input-->
<!--          type="text"-->
<!--          v-model="studentId"-->
<!--          required-->
<!--          class="form-input"-->
<!--          id="studentId"-->
<!--        />-->
<!--      </div>-->

<!--      <div class="form-group">-->
<!--        <label class="form-label" for="message">消息内容</label>-->
<!--        <textarea-->
<!--          v-model="message"-->
<!--          required-->
<!--          class="form-textarea"-->
<!--          id="message"-->
<!--          rows="4"-->
<!--        ></textarea>-->
<!--      </div>-->

<!--      <button type="submit" class="submit-btn">-->
<!--        <span class="btn-text">发送通知</span>-->
<!--        <span class="btn-icon">➔</span>-->
<!--      </button>-->
<!--    </form>-->
<!--  </div>-->
<!--</template>-->


<!--<script>-->
<!--import { ref } from 'vue';-->
<!--import axios from 'axios';-->

<!--export default {-->
<!--  setup() {-->
<!--    const studentId = ref('');-->
<!--    const message = ref('');-->

<!--    const sendNotification = async () => {-->
<!--      try {-->
<!--        await axios.post('http://localhost:8002/interact/send-notification/', {-->
<!--          student_id: studentId.value,-->
<!--          message: message.value-->
<!--        });-->
<!--        alert('通知发送成功');-->
<!--        studentId.value = '';-->
<!--        message.value = '';-->
<!--      } catch (error) {-->
<!--        console.error('发送通知失败:', error);-->
<!--        alert('发送通知失败');-->
<!--      }-->
<!--    };-->

<!--    return {-->
<!--      studentId,-->
<!--      message,-->
<!--      sendNotification,-->
<!--    };-->
<!--  },-->
<!--};-->
<!--</script>-->


<!--<style scoped>-->
<!--.send-notification-container {-->
<!--  max-width: 600px;-->
<!--  margin: 2rem auto;-->
<!--  padding: 2rem;-->
<!--  background: #fff;-->
<!--  border-radius: 15px;-->
<!--  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);-->
<!--}-->

<!--.title {-->
<!--  color: #2c3e50;-->
<!--  text-align: center;-->
<!--  margin-bottom: 2.5rem;-->
<!--  font-size: 2.2rem;-->
<!--  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);-->
<!--}-->

<!--.notification-form {-->
<!--  display: flex;-->
<!--  flex-direction: column;-->
<!--  gap: 1.5rem;-->
<!--}-->

<!--.form-group {-->
<!--  display: flex;-->
<!--  flex-direction: column;-->
<!--  gap: 0.5rem;-->
<!--}-->

<!--.form-label {-->
<!--  color: #34495e;-->
<!--  font-weight: 500;-->
<!--  font-size: 1.1rem;-->
<!--}-->

<!--.form-input,-->
<!--.form-textarea {-->
<!--  padding: 0.8rem 1rem;-->
<!--  border: 2px solid #e0e0e0;-->
<!--  border-radius: 8px;-->
<!--  font-size: 1rem;-->
<!--  transition: border-color 0.3s ease;-->
<!--}-->

<!--.form-input:focus,-->
<!--.form-textarea:focus {-->
<!--  border-color: #42b983;-->
<!--  outline: none;-->
<!--  box-shadow: 0 0 0 3px rgba(66, 185, 131, 0.1);-->
<!--}-->

<!--.form-textarea {-->
<!--  resize: vertical;-->
<!--  min-height: 100px;-->
<!--}-->

<!--.submit-btn {-->
<!--  background: #42b983;-->
<!--  color: white;-->
<!--  border: none;-->
<!--  padding: 1rem 2rem;-->
<!--  border-radius: 25px;-->
<!--  cursor: pointer;-->
<!--  transition: all 0.3s ease;-->
<!--  display: flex;-->
<!--  align-items: center;-->
<!--  gap: 0.8rem;-->
<!--  font-weight: 600;-->
<!--  justify-content: center;-->
<!--}-->

<!--.submit-btn:hover {-->
<!--  background: #33a06f;-->
<!--  transform: translateY(-2px);-->
<!--  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);-->
<!--}-->

<!--.submit-btn:active {-->
<!--  transform: translateY(0);-->
<!--}-->

<!--.btn-icon {-->
<!--  font-size: 1.2rem;-->
<!--  transition: transform 0.3s ease;-->
<!--}-->

<!--.submit-btn:hover .btn-icon {-->
<!--  transform: translateX(3px);-->
<!--}-->

<!--/* 响应式设计 */-->
<!--@media (max-width: 480px) {-->
<!--  .send-notification-container {-->
<!--    margin: 1rem;-->
<!--    padding: 1.5rem;-->
<!--  }-->

<!--  .title {-->
<!--    font-size: 1.8rem;-->
<!--    margin-bottom: 1.5rem;-->
<!--  }-->

<!--  .form-input,-->
<!--  .form-textarea {-->
<!--    padding: 0.6rem 0.8rem;-->
<!--    font-size: 0.9rem;-->
<!--  }-->

<!--  .submit-btn {-->
<!--    padding: 0.8rem 1.5rem;-->
<!--    font-size: 0.9rem;-->
<!--    gap: 0.5rem;-->
<!--  }-->
<!--}-->
<!--</style>-->



<!--<template>-->
<!--  <div class="send-notification-container">-->
<!--    <h1 class="title">📩 批量发送通知</h1>-->

<!--    &lt;!&ndash; 新增学生列表区域 &ndash;&gt;-->
<!--    <div class="student-list-wrapper">-->
<!--      <el-input-->
<!--        placeholder="输入学生编号/姓名筛选..."-->
<!--        v-model="queryForm.query"-->
<!--        clearable-->
<!--        style="width: 300px; margin-bottom: 15px"-->
<!--      />-->

<!--      <el-table-->
<!--        :data="tableData"-->
<!--        @selection-change="handleSelectionChange"-->
<!--        height="300"-->
<!--        style="width: 100%"-->
<!--      >-->
<!--        &lt;!&ndash; 添加多选列 &ndash;&gt;-->
<!--        <el-table-column type="selection" width="55" />-->
<!--        <el-table-column prop="student_id" label="学号" width="120" />-->
<!--        <el-table-column prop="student_name" label="姓名" width="120" />-->
<!--        <el-table-column prop="school" label="学校" />-->
<!--      </el-table>-->
<!--    </div>-->

<!--    <form @submit.prevent="sendNotification" class="notification-form">-->
<!--      <div class="form-group">-->
<!--        <label class="form-label">消息内容</label>-->
<!--        <textarea-->
<!--          v-model="message"-->
<!--          required-->
<!--          class="form-textarea"-->
<!--          rows="4"-->
<!--          placeholder="请输入通知内容..."-->
<!--        ></textarea>-->
<!--      </div>-->

<!--      <button type="submit" class="submit-btn">-->
<!--        <span class="btn-text">发送通知</span>-->
<!--        <span class="btn-icon">➔</span>-->
<!--      </button>-->

<!--      &lt;!&ndash; 新增发送状态提示 &ndash;&gt;-->
<!--      <div v-if="sendStatus" class="status-indicator">-->
<!--        {{ sendStatus }}-->
<!--      </div>-->
<!--    </form>-->
<!--  </div>-->
<!--</template>-->

<!--<script setup>-->
<!--import { ref } from 'vue';-->
<!--import axios from 'axios';-->
<!--import { ElMessage } from 'element-plus';-->

<!--// 复用学生列表逻辑-->
<!--const queryForm = ref({-->
<!--  query: '',-->
<!--  pageNum: 1,-->
<!--  pageSize: 10-->
<!--});-->

<!--const total = ref(0);-->
<!--const tableData = ref([]);-->
<!--const multipleSelection = ref([]);-->

<!--// 加载学生列表-->
<!--const loadStudents = async () => {-->
<!--  try {-->
<!--    const res = await axios.post('http://localhost:8000/permission/search', queryForm.value);-->
<!--    tableData.value = res.data.roleList;-->
<!--    total.value = res.data.total;-->
<!--  } catch (error) {-->
<!--    ElMessage.error('加载学生列表失败');-->
<!--  }-->
<!--};-->

<!--// 多选处理-->
<!--const handleSelectionChange = (selection) => {-->
<!--  multipleSelection.value = selection;-->
<!--};-->

<!--// 通知相关逻辑-->
<!--const message = ref('');-->
<!--const sendStatus = ref('');-->

<!--const sendNotification = async () => {-->
<!--  if (multipleSelection.value.length === 0) {-->
<!--    ElMessage.warning('请先选择接收学生');-->
<!--    return;-->
<!--  }-->

<!--  try {-->
<!--    sendStatus.value = '发送中...';-->

<!--    // 提取选中的学生ID-->
<!--    const studentIds = multipleSelection.value.map(item => item.student_id);-->

<!--    // 批量发送请求-->
<!--    await axios.post('http://localhost:8002/interact/send-notification/', {-->
<!--      student_ids: studentIds,  // 修改为接收数组-->
<!--      message: message.value-->
<!--    });-->

<!--    sendStatus.value = '发送成功！';-->
<!--    message.value = '';-->
<!--    multipleSelection.value = []; // 清空选择-->
<!--    loadStudents(); // 刷新列表-->
<!--  } catch (error) {-->
<!--    sendStatus.value = '发送失败，请重试';-->
<!--    console.error('发送通知失败:', error);-->
<!--  } finally {-->
<!--    setTimeout(() => sendStatus.value = '', 3000); // 3秒后清除状态-->
<!--  }-->
<!--};-->

<!--// 初始化加载-->
<!--loadStudents();-->
<!--</script>-->

<!--<style scoped>-->
<!--/* 新增样式 */-->
<!--.student-list-wrapper {-->
<!--  margin: 20px 0;-->
<!--  border: 1px solid #ebeef5;-->
<!--  border-radius: 4px;-->
<!--  padding: 15px;-->
<!--  background: #fff;-->
<!--}-->

<!--.status-indicator {-->
<!--  margin-top: 15px;-->
<!--  color: #67c23a;-->
<!--  font-weight: bold;-->
<!--}-->

<!--/* 调整原有样式 */-->
<!--.send-notification-container {-->
<!--  max-width: 800px;-->
<!--  margin: 2rem auto;-->
<!--  padding: 2rem;-->
<!--}-->

<!--.title {-->
<!--  color: #409eff;-->
<!--  border-bottom: 2px solid #409eff;-->
<!--  padding-bottom: 10px;-->
<!--}-->

<!--.notification-form {-->
<!--  margin-top: 25px;-->
<!--}-->

<!--.form-textarea {-->
<!--  width: 100%;-->
<!--  padding: 12px 15px;-->
<!--  border: 1px solid #dcdfe6;-->
<!--  border-radius: 4px;-->
<!--}-->

<!--.submit-btn {-->
<!--  background: #409eff;-->
<!--  color: white;-->
<!--  border: none;-->
<!--  padding: 12px 25px;-->
<!--  border-radius: 4px;-->
<!--  cursor: pointer;-->
<!--  transition: all 0.3s;-->
<!--  margin-top: 15px;-->
<!--  width: 100%;-->
<!--}-->

<!--.submit-btn:hover {-->
<!--  background: #66b1ff;-->
<!--}-->
<!--</style>-->







<template>
  <div class="send-notification-container">
    <h1 class="title">📩 发送通知</h1>

    <!-- 模式切换按钮 -->
    <div class="mode-switch">
      <button
        @click="currentMode = 'single'"
        :class="{ active: currentMode === 'single' }"
      >
        单发模式
      </button>
      <button
        @click="currentMode = 'batch'"
        :class="{ active: currentMode === 'batch' }"
      >
        批量模式
      </button>
    </div>

    <!-- 单发模式表单 -->
    <form v-if="currentMode === 'single'" @submit.prevent="sendNotification" class="notification-form">
      <div class="form-group">
        <label class="form-label">学生/教师ID</label>
        <input
          type="text"
          v-model="studentId"
          required
          class="form-input"
          placeholder="输入单个ID"
        />
      </div>

      <div class="form-group">
        <label class="form-label">消息内容</label>
        <textarea
          v-model="message"
          required
          class="form-textarea"
          rows="4"
          placeholder="请输入通知内容..."
        ></textarea>
      </div>

      <button type="submit" class="submit-btn">
        <span class="btn-text">发送通知</span>
        <span class="btn-icon">➔</span>
      </button>
    </form>

    <!-- 批量模式表单 -->
    <form v-if="currentMode === 'batch'" @submit.prevent="sendBatchNotification" class="notification-form">
      <div class="student-list-wrapper">
        <el-input
          placeholder="输入学生编号/姓名筛选..."
          v-model="queryForm.query"
          clearable
          style="width: 300px; margin-bottom: 15px"
        />

        <el-table
          :data="tableData"
          @selection-change="handleSelectionChange"
          height="300"
          style="width: 100%"
        >
          <el-table-column type="selection" width="55" />
          <el-table-column prop="student_id" label="学号" width="120" />
          <el-table-column prop="student_name" label="姓名" width="120" />
          <el-table-column prop="school" label="学校" />
        </el-table>
      </div>

      <div class="form-group">
        <label class="form-label">消息内容</label>
        <textarea
          v-model="message"
          required
          class="form-textarea"
          rows="4"
          placeholder="请输入通知内容..."
        ></textarea>
      </div>

      <button type="submit" class="submit-btn">
        <span class="btn-text">批量发送</span>
        <span class="btn-icon">➔</span>
      </button>

      <div v-if="sendStatus" class="status-indicator">
        {{ sendStatus }}
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { ElMessage } from 'element-plus';

const currentMode = ref('single'); // 默认单发模式

// 单发模式数据
const studentId = ref('');
const message = ref('');

// 批量模式数据
const queryForm = ref({
  query: '',
  pageNum: 1,
  pageSize: 10
});

const total = ref(0);
const tableData = ref([]);
const multipleSelection = ref([]);
const sendStatus = ref('');

// 加载学生列表
const loadStudents = async () => {
  try {
    const res = await axios.post('http://localhost:8000/permission/search', queryForm.value);
    tableData.value = res.data.roleList;
    total.value = res.data.total;
  } catch (error) {
    ElMessage.error('加载学生列表失败');
  }
};

// 多选处理
const handleSelectionChange = (selection) => {
  multipleSelection.value = selection;
};

// 发送通知
const sendNotification = async () => {
  try {
    await axios.post('http://localhost:8002/interact/send-notification/', {
      student_id: studentId.value.trim(),
      message: message.value
    });
    ElMessage.success('通知发送成功');
    studentId.value = '';
    message.value = '';
  } catch (error) {
    ElMessage.error('发送通知失败');
    console.error('发送通知失败:', error);
  }
};

// 批量发送通知
const sendBatchNotification = async () => {
  if (multipleSelection.value.length === 0) {
    ElMessage.warning('请先选择接收学生');
    return;
  }

  try {
    sendStatus.value = '发送中...';
    const studentIds = multipleSelection.value.map(item => item.student_id);

    await axios.post('http://localhost:8002/interact/send-notification/', {
      student_ids: studentIds,
      message: message.value
    });

    sendStatus.value = `成功发送 ${studentIds.length} 条通知`;
    message.value = '';
    multipleSelection.value = [];
    loadStudents();
  } catch (error) {
    sendStatus.value = '发送失败，请重试';
    console.error('批量发送失败:', error);
  } finally {
    setTimeout(() => sendStatus.value = '', 3000);
  }
};

// 初始化加载
loadStudents();
</script>

<style scoped>
.send-notification-container {
  max-width: 800px;
  margin: 2rem auto;
  padding: 2rem;
  background: #fff;
  border-radius: 15px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.title {
  color: #2c3e50;
  text-align: center;
  margin-bottom: 2.5rem;
  font-size: 2.2rem;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
}

.mode-switch {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin-bottom: 2rem;
}

.mode-switch button {
  padding: 0.8rem 2rem;
  border: none;
  border-radius: 25px;
  background: #e0e0e0;
  color: #333;
  cursor: pointer;
  transition: all 0.3s ease;
}

.mode-switch button.active {
  background: #42b983;
  color: white;
  transform: translateY(-2px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

.notification-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.form-label {
  color: #34495e;
  font-weight: 500;
  font-size: 1.1rem;
}

.form-input,
.form-textarea {
  padding: 0.8rem 1rem;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.3s ease;
}

.form-input:focus,
.form-textarea:focus {
  border-color: #42b983;
  outline: none;
  box-shadow: 0 0 0 3px rgba(66, 185, 131, 0.1);
}

.form-textarea {
  resize: vertical;
  min-height: 100px;
}

.submit-btn {
  background: #42b983;
  color: white;
  border: none;
  padding: 1rem 2rem;
  border-radius: 25px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 0.8rem;
  font-weight: 600;
  justify-content: center;
}

.submit-btn:hover {
  background: #33a06f;
  transform: translateY(-2px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

.submit-btn:active {
  transform: translateY(0);
}

.btn-icon {
  font-size: 1.2rem;
  transition: transform 0.3s ease;
}

.submit-btn:hover .btn-icon {
  transform: translateX(3px);
}

.status-indicator {
  margin-top: 15px;
  color: #67c23a;
  font-weight: bold;
  text-align: center;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .send-notification-container {
    margin: 1rem;
    padding: 1.5rem;
  }

  .title {
    font-size: 1.8rem;
    margin-bottom: 1.5rem;
  }

  .mode-switch {
    flex-direction: column;
  }

  .form-input,
  .form-textarea {
    padding: 0.6rem 0.8rem;
    font-size: 0.9rem;
  }

  .submit-btn {
    padding: 0.8rem 1.5rem;
    font-size: 0.9rem;
    gap: 0.5rem;
  }
}
</style>