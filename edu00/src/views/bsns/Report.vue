<!--<template>-->
<!--  <div class="learning-report">-->
<!--    <h1>学习报告</h1>-->
<!--    <div v-if="report" class="report-content">-->
<!--      <h2>学生: {{ report.student_name }}</h2>-->
<!--      <div class="charts-container">-->
<!--        <div v-for="course in report.report" :key="course.course_id" class="chart">-->
<!--          <h3 class="title">{{ course.course_name }}</h3>-->
<!--          <div class="chart-svg">-->
<!--            <LineChart :chart-data="course.progressData" :options="chartOptions" />-->
<!--            <BarChart :chart-data="course.durationData" :options="chartOptions" />-->
<!--            <PieChart :chart-data="course.contentData" :options="chartOptions" />-->
<!--            <DoughnutChart :chart-data="course.completionData" :options="chartOptions" />-->
<!--          </div>-->
<!--          <div class="chart-values">-->
<!--            <p class="h-value">总时长: {{ course.total_duration }}分钟</p>-->
<!--            <p class="h-value">完成率: {{ course.completion_rate }}%</p>-->
<!--          </div>-->
<!--        </div>-->
<!--      </div>-->
<!--      <div v-for="course in report.report" :key="course.course_id" class="course-details">-->
<!--        <h4>课程: {{ course.course_name }}</h4>-->
<!--        <ul>-->
<!--          <li v-for="record in course.records" :key="record.record_id">-->
<!--            内容: {{ record.content }}, 时长: {{ record.duration }}分钟-->
<!--          </li>-->
<!--        </ul>-->
<!--      </div>-->
<!--    </div>-->
<!--    <div v-else class="no-report">未找到学习报告</div>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--import axios from 'axios';-->
<!--import { Line, Bar, Pie, Doughnut } from 'vue-chartjs';-->
<!--import { Chart as ChartJS, Title, Tooltip, Legend, LineElement, BarElement, CategoryScale, LinearScale, PointElement, ArcElement } from 'chart.js';-->

<!--ChartJS.register(Title, Tooltip, Legend, LineElement, BarElement, CategoryScale, LinearScale, PointElement, ArcElement);-->

<!--export default {-->
<!--  name: 'LearningReport',-->
<!--  components: {-->
<!--    LineChart: Line,-->
<!--    BarChart: Bar,-->
<!--    PieChart: Pie,-->
<!--    DoughnutChart: Doughnut-->
<!--  },-->
<!--  data() {-->
<!--    return {-->
<!--      report: null,-->
<!--      chartOptions: {-->
<!--        responsive: true,-->
<!--        maintainAspectRatio: false,-->
<!--        animation: {-->
<!--          duration: 1000-->
<!--        }-->
<!--      }-->
<!--    };-->
<!--  },-->
<!--  async mounted() {-->
<!--    const user = JSON.parse(sessionStorage.getItem('currentUser'));-->
<!--    const id = user.student_or_teacher_id;-->
<!--    await this.fetchReport(id);-->
<!--  },-->
<!--  methods: {-->
<!--    async fetchReport(id) {-->
<!--      try {-->
<!--        const response = await axios.get(`http://localhost:8002/api/learning-report/${id}/`);-->
<!--        this.report = response.data;-->
<!--        this.report.report.forEach(course => {-->
<!--          course.progressData = {-->
<!--            labels: ['进度'],-->
<!--            datasets: [-->
<!--              {-->
<!--                label: '学习进度',-->
<!--                data: [course.progress],-->
<!--                borderColor: '#00d5bd',-->
<!--                backgroundColor: '#00d5bd',-->
<!--                fill: false-->
<!--              }-->
<!--            ]-->
<!--          };-->
<!--          course.durationData = {-->
<!--            labels: ['总时长'],-->
<!--            datasets: [-->
<!--              {-->
<!--                label: '总时长 (分钟)',-->
<!--                data: [course.total_duration],-->
<!--                backgroundColor: '#24c1ed'-->
<!--              }-->
<!--            ]-->
<!--          };-->
<!--          course.contentData = {-->
<!--            labels: course.records.map(record => record.content),-->
<!--            datasets: [-->
<!--              {-->
<!--                label: '内容时长 (分钟)',-->
<!--                data: course.records.map(record => record.duration),-->
<!--                backgroundColor: ['#00d5bd', '#24c1ed', '#954ce9', '#ffcc00', '#ff6666'],-->
<!--                hoverOffset: 4-->
<!--              }-->
<!--            ]-->
<!--          };-->
<!--          course.completionData = {-->
<!--            labels: ['已完成', '未完成'],-->
<!--            datasets: [-->
<!--              {-->
<!--                label: '课程完成率',-->
<!--                data: [course.completion_rate, 100 - course.completion_rate],-->
<!--                backgroundColor: ['#4caf50', '#f44336'],-->
<!--                hoverOffset: 4-->
<!--              }-->
<!--            ]-->
<!--          };-->
<!--        });-->
<!--      } catch (error) {-->
<!--        console.error(error);-->
<!--      }-->
<!--    }-->
<!--  }-->
<!--};-->
<!--</script>-->

<!--<style scoped>-->
<!--.learning-report {-->
<!--  max-width: 800px;-->
<!--  margin: 0 auto;-->
<!--  padding: 20px;-->
<!--  background-color: #f9f9f9;-->
<!--  border-radius: 8px;-->
<!--  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);-->
<!--  text-align: center;-->
<!--  font-family: 'Arial', sans-serif;-->
<!--  transition: all 0.3s ease;-->
<!--}-->

<!--h1, h2, h3, h4 {-->
<!--  color: #333;-->
<!--  transition: color 0.3s ease;-->
<!--}-->

<!--.report-content {-->
<!--  margin-top: 20px;-->
<!--}-->

<!--.charts-container {-->
<!--  display: flex;-->
<!--  flex-wrap: wrap;-->
<!--  justify-content: center;-->
<!--  gap: 20px;-->
<!--}-->

<!--.chart {-->
<!--  width: 100%;-->
<!--  max-width: 300px;-->
<!--  margin: 10px auto;-->
<!--  padding: 20px;-->
<!--  background-color: #fff;-->
<!--  border-radius: 8px;-->
<!--  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);-->
<!--  text-align: center;-->
<!--  transition: all 0.3s ease;-->
<!--}-->

<!--.chart-svg {-->
<!--  margin: 10px 0;-->
<!--}-->

<!--.chart-values {-->
<!--  margin-top: 10px;-->
<!--}-->

<!--.chart-values .h-value {-->
<!--  font-size: 1.2em;-->
<!--  font-weight: bold;-->
<!--  color: #555;-->
<!--  transition: color 0.3s ease;-->
<!--}-->

<!--.course-details {-->
<!--  margin-top: 20px;-->
<!--  text-align: left;-->
<!--  transition: all 0.3s ease;-->
<!--}-->

<!--.course-details h4 {-->
<!--  margin-bottom: 10px;-->
<!--  color: #4caf50;-->
<!--  transition: color 0.3s ease;-->
<!--}-->

<!--.course-details ul {-->
<!--  list-style-type: none;-->
<!--  padding: 0;-->
<!--}-->

<!--.course-details li {-->
<!--  margin-bottom: 5px;-->
<!--  font-size: 0.9em;-->
<!--  color: #666;-->
<!--  transition: color 0.3s ease;-->
<!--}-->

<!--.no-report {-->
<!--  margin-top: 20px;-->
<!--  color: #999;-->
<!--  font-size: 1.2em;-->
<!--  transition: color 0.3s ease;-->
<!--}-->
<!--</style>-->




<template>
  <div class="learning-report">
    <h1>学习报告</h1>
    <div v-if="report" class="report-content">
      <h2>学生: {{ report.student_name }}</h2>
      <div class="charts-container">
        <div v-for="course in report.report" :key="course.course_id" class="chart">
          <h3 class="title">{{ course.course_name }}</h3>
          <div class="chart-svg">
            <LineChart :chart-data="course.progressData" :options="chartOptions" />
            <BarChart :chart-data="course.durationData" :options="chartOptions" />
            <PieChart :chart-data="course.contentData" :options="chartOptions" />
            <DoughnutChart :chart-data="course.completionData" :options="chartOptions" />
            <BarChart :chart-data="course.dailyDurationsData" :options="chartOptions" />
          </div>
          <div class="chart-values">
            <p class="h-value">总时长: {{ course.total_duration }}分钟</p>
            <p class="h-value">完成率: {{ course.completion_rate }}%</p>
          </div>
        </div>
      </div>
      <div v-for="course in report.report" :key="course.course_id" class="course-details">
        <h4>课程: {{ course.course_name }}</h4>
        <ul>
          <li v-for="record in course.records" :key="record.record_id">
            内容: {{ record.content }}, 时长: {{ record.duration }}分钟, 时间: {{ record.record_time }}
          </li>
        </ul>
      </div>
    </div>
    <div v-else class="no-report">未找到学习报告</div>
  </div>
</template>

<script>
import axios from 'axios';
import { Line, Bar, Pie, Doughnut } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, LineElement, BarElement, CategoryScale, LinearScale, PointElement, ArcElement } from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, LineElement, BarElement, CategoryScale, LinearScale, PointElement, ArcElement);

export default {
  name: 'LearningReport',
  components: {
    LineChart: Line,
    BarChart: Bar,
    PieChart: Pie,
    DoughnutChart: Doughnut
  },
  data() {
    return {
      report: null,
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        animation: {
          duration: 1000
        }
      }
    };
  },
  async mounted() {
    const user = JSON.parse(sessionStorage.getItem('currentUser'));
    const id = user.student_or_teacher_id;
    await this.fetchReport(id);
  },
  methods: {
    async fetchReport(id) {
      try {
        const response = await axios.get(`http://localhost:8002/api/learning-report/${id}/`);
        this.report = response.data;
        this.report.report.forEach(course => {
          course.progressData = {
            labels: ['进度'],
            datasets: [
              {
                label: '学习进度',
                data: [course.progress],
                borderColor: '#00d5bd',
                backgroundColor: '#00d5bd',
                fill: false
              }
            ]
          };
          course.durationData = {
            labels: ['总时长'],
            datasets: [
              {
                label: '总时长 (分钟)',
                data: [course.total_duration],
                backgroundColor: '#24c1ed'
              }
            ]
          };
          course.contentData = {
            labels: course.records.map(record => record.content),
            datasets: [
              {
                label: '内容时长 (分钟)',
                data: course.records.map(record => record.duration),
                backgroundColor: ['#00d5bd', '#24c1ed', '#954ce9', '#ffcc00', '#ff6666'],
                hoverOffset: 4
              }
            ]
          };
          course.completionData = {
            labels: ['已完成', '未完成'],
            datasets: [
              {
                label: '课程完成率',
                data: [course.completion_rate, 100 - course.completion_rate],
                backgroundColor: ['#4caf50', '#f44336'],
                hoverOffset: 4
              }
            ]
          };
          course.dailyDurationsData = {
            labels: course.daily_durations.map(item => item.date),
            datasets: [
              {
                label: '每日学习时长 (分钟)',
                data: course.daily_durations.map(item => item.daily_duration),
                backgroundColor: '#24c1ed'
              }
            ]
          };
        });
      } catch (error) {
        console.error(error);
      }
    }
  }
};
</script>

<style scoped>
.learning-report {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
  font-family: 'Arial', sans-serif;
  transition: all 0.3s ease;
}

h1, h2, h3, h4 {
  color: #333;
  transition: color 0.3s ease;
}

.report-content {
  margin-top: 20px;
}

.charts-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
}

.chart {
  width: 100%;
  max-width: 300px;
  margin: 10px auto;
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  text-align: center;
  transition: all 0.3s ease;
}

.chart-svg {
  margin: 10px 0;
}

.chart-values {
  margin-top: 10px;
}

.chart-values .h-value {
  font-size: 1.2em;
  font-weight: bold;
  color: #555;
  transition: color 0.3s ease;
}

.learning-sessions, .content-summary {
  margin-top: 20px;
  text-align: left;
  transition: all 0.3s ease;
}

.learning-sessions h4, .content-summary h4 {
  margin-bottom: 10px;
  color: #4caf50;
  transition: color 0.3s ease;
}

.learning-sessions ul, .content-summary ul {
  list-style-type: none;
  padding: 0;
}

.learning-sessions li, .content-summary li {
  margin-bottom: 5px;
  font-size: 0.9em;
  color: #666;
  transition: color 0.3s ease;
}

.course-details {
  margin-top: 20px;
  text-align: left;
  transition: all 0.3s ease;
}

.course-details h4 {
  margin-bottom: 10px;
  color: #4caf50;
  transition: color 0.3s ease;
}

.course-details ul {
  list-style-type: none;
  padding: 0;
}

.course-details li {
  margin-bottom: 5px;
  font-size: 0.9em;
  color: #666;
  transition: color 0.3s ease;
}

.no-report {
  margin-top: 20px;
  color: #999;
  font-size: 1.2em;
  transition: color 0.3s ease;
}
</style>