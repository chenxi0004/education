
<template>
  <div class="app-container">
    <el-row :gutter="20" class="header">
      <el-col :span="7">
        <el-input placeholder="请输入教师编号或姓名..." v-model="queryForm.query" clearable></el-input>
      </el-col>
      <el-button type="primary" :icon="Search" @click="fetchTeachers">搜索</el-button>
      <el-button type="success" :icon="DocumentAdd" @click="openDialog(null)">新增教师</el-button>
    </el-row>

    <el-table :data="teachers" style="width: 100%">
      <el-table-column prop="teacher_id" label="教师编号"></el-table-column>
      <el-table-column prop="teacher_name" label="教师姓名"></el-table-column>
      <el-table-column prop="gender" label="性别"></el-table-column>
      <el-table-column prop="school" label="学校"></el-table-column>
      <el-table-column prop="phone_number" label="手机号码"></el-table-column>
      <el-table-column prop="email" label="电子邮箱"></el-table-column>
      <el-table-column label="操作" width="200">
        <template #default="scope">
          <el-button type="success" @click="openDialog(scope.row)">编辑</el-button>
          <el-button type="danger" @click="deleteTeacher(scope.row.teacher_id)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <!-- 新增/编辑对话框 -->
    <el-dialog :title="dialogTitle" v-model="dialogVisible">
      <el-form :model="form" label-width="100px">
        <el-form-item label="教师编号">
          <el-input v-model="form.teacher_id" placeholder="教师编号"></el-input>
        </el-form-item>
        <el-form-item label="教师姓名">
          <el-input v-model="form.teacher_name" placeholder="教师姓名"></el-input>
        </el-form-item>
        <el-form-item label="性别">
          <el-select v-model="form.gender">
            <el-option label="男" value="男"></el-option>
            <el-option label="女" value="女"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="学校">
          <el-input v-model="form.school" placeholder="学校"></el-input>
        </el-form-item>
        <el-form-item label="手机号码">
          <el-input v-model="form.phone_number" placeholder="手机号码"></el-input>
        </el-form-item>
        <el-form-item label="电子邮箱">
          <el-input v-model="form.email" placeholder="电子邮箱"></el-input>
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="saveTeacher">保存</el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script>
import { Delete, DocumentAdd, Search } from "@element-plus/icons-vue";
import requestUtil from "@/util/request"; // 确保正确导入 requestUtil
import { ElMessage } from "element-plus";

const BASE_URL = "http://127.0.0.1:8000/permission/";

export default {
  components: { Delete, DocumentAdd, Search },
  data() {
    return {
      teachers: [], // 存储教师列表
      dialogVisible: false, // 控制对话框显示
      dialogTitle: "", // 对话框标题
      form: {
        teacher_id: "",
        teacher_name: "",
        gender: "",
        school: "",
        phone_number: "",
        email: "",
      }, // 表单数据
      queryForm: {
        query: "",
      }, // 搜索表单数据
    };
  },
  methods: {
    // 获取教师列表
    async fetchTeachers() {
    try {
    const query = this.queryForm.query.trim(); // 获取搜索条件并去除空格
    const response = await requestUtil.get(`${BASE_URL}teachers/`, {
      query // 将搜索条件作为 URL 参数传递
    });

    if (response.status !== 200) {
      ElMessage.error("无法获取教师列表，请检查网络或后端服务是否正常运行！");
      return;
    }
    this.teachers = response.data; // 更新教师列表
  } catch (error) {
    console.error("请求失败：", error);
    ElMessage.error("无法获取教师列表，请检查网络或后端服务是否正常运行！");
  }
},
    // 保存教师信息（新增或更新）
    async saveTeacher() {
      try {
        if (this.form.teacher_id) {
          // 如果有 teacher_id，则执行更新操作
          await requestUtil.put(`${BASE_URL}teachers/${this.form.teacher_id}/`, this.form);
        } else {
          // 否则执行新增操作
          await requestUtil.post(`${BASE_URL}teachers/`, this.form);
        }
        this.dialogVisible = false; // 关闭对话框
        this.fetchTeachers(); // 刷新教师列表
        ElMessage.success("操作成功！");
      } catch (error) {
        console.error("请求失败：", error);
        ElMessage.error("操作失败，请检查网络或后端服务是否正常运行！");
      }
    },
    // 删除教师
    async deleteTeacher(teacherId) {
      try {
        await requestUtil.del(`${BASE_URL}teachers/${teacherId}/`); // 发起 DELETE 请求
        this.fetchTeachers(); // 刷新教师列表
        ElMessage.success("删除成功！");
      } catch (error) {
        console.error("请求失败：", error);
        ElMessage.error("删除失败，请检查网络或后端服务是否正常运行！");
      }
    },
    // 打开对话框（新增或编辑）
    openDialog(teacher) {
      if (teacher) {
        // 如果传入了教师对象，则为编辑操作
        this.dialogTitle = "编辑教师";
        this.form = { ...teacher }; // 将教师数据填充到表单
      } else {
        // 否则为新增操作
        this.dialogTitle = "新增教师";
        this.form = {
          teacher_id: "",
          teacher_name: "",
          gender: "",
          school: "",
          phone_number: "",
          email: "",
        }; // 清空表单
      }
      this.dialogVisible = true; // 显示对话框
    },
  },
  mounted() {
    this.fetchTeachers(); // 组件挂载时获取教师列表
  },
};




//
// import axios from "axios";
// import { Delete, DocumentAdd, Search } from "@element-plus/icons-vue";
// import requestUtil from "@/util/request";
// import { ElMessage } from "element-plus";
//
// // // 设置 Axios 请求拦截器
// // axios.interceptors.request.use(config => {
// //     const token = localStorage.getItem('access_token');
// //     if (token) {
// //         config.headers['Authorization'] = `Bearer ${token}`;
// //     }
// //     return config;
// // }, error => {
// //     return Promise.reject(error);
// // });
// //
// // // 设置 Axios 响应拦截器
// // axios.interceptors.response.use(response => {
// //     return response;
// // }, error => {
// //     const originalRequest = error.config;
// //     if (error.response.status === 401 && !originalRequest._retry) {
// //         originalRequest._retry = true;
// //         const refreshToken = localStorage.getItem('refresh_token');
// //         return axios.post('http://localhost:8000/user/token/refresh/', {
// //             refresh: refreshToken
// //         }).then(response => {
// //             const { access } = response.data;
// //             localStorage.setItem('access_token', access);
// //             axios.defaults.headers.common['Authorization'] = `Bearer ${access}`;
// //             return axios(originalRequest);
// //         }).catch(error => {
// //             ElMessage.error('Token 刷新失败，请重新登录。');
// //             return Promise.reject(error);
// //         });
// //     }
// //     return Promise.reject(error);
// // });
// const BASE_URL = "http://127.0.0.1:8000/permission/";
// export default {
//   components: { Delete, DocumentAdd, Search },
//   data() {
//     return {
//       teachers: [],
//       dialogVisible: false,
//       dialogTitle: "",
//       form: {
//         teacher_id: "",
//         teacher_name: "",
//         gender: "",
//         school: "",
//         phone_number: "",
//         email: "",
//       },
//       queryForm: {
//         query: "",
//       },
//     };
//   },
//   methods: {
// async fetchTeachers() {
//   try {
//     const query = this.queryForm.query;  // 获取用户输入的查询条件
//     // const response = await axios.get(`${BASE_URL}teachers/`, {
//     //   params: { query }  // 将查询条件作为 URL 参数传递
//     // });
//     const response = await requestUtil.get(`${BASE_URL}teachers/`, {
//       params: { query }  // 将查询条件作为 URL 参数传递
//     });
//     this.teachers = response.data;
//   } catch (error) {
//     console.error("请求失败：", error);
//     this.$message.error("无法获取教师列表，请检查网络或后端服务是否正常运行！");
//   }
// },
// async saveTeacher() {
//   try {
//     if (this.form.teacher_id) {
//       // 更新教师
//       await axios.put(`${BASE_URL}teachers/${this.form.teacher_id}/`, this.form);
//     } else {
//       // 新增教师
//       await axios.post(`${BASE_URL}teachers/`, this.form);
//     }
//     this.dialogVisible = false;
//     this.fetchTeachers();
//     this.$message.success("操作成功！");
//   } catch (error) {
//     console.error("请求失败：", error);
//     console.log('error',this.form)
//     this.$message.error("操作失败，请检查网络或后端服务是否正常运行！");
//   }
// },
//
// async deleteTeacher(teacherId) {
//   try {
//     await axios.delete(`${BASE_URL}teachers/${teacherId}/`);
//     this.fetchTeachers();
//     this.$message.success("删除成功！");
//   } catch (error) {
//     console.error("请求失败：", error);
//     this.$message.error("删除失败，请检查网络或后端服务是否正常运行！");
//   }
// },
//     openDialog(teacher) {
//       if (teacher) {
//         this.dialogTitle = "编辑教师";
//         this.form = { ...teacher };
//       } else {
//         this.dialogTitle = "新增教师";
//         this.form = {
//           teacher_id: "",
//           teacher_name: "",
//           gender: "",
//           school: "",
//           phone_number: "",
//           email: "",
//         };
//       }
//       this.dialogVisible = true;
//     },
//   },
//   mounted() {
//     this.fetchTeachers();
//   },
// };
</script>
