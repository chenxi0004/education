<script setup>
import {Search,Delete,DocumentAdd,Edit,Tools,RefreshRight} from "@element-plus/icons-vue";
import {ref} from "vue";
import requestUtil,{getServerUrl} from "@/util/request";
import {ElMessage,ElMessageBox} from "element-plus";
import axios from "axios";
import MenuDialog from "@/views/sys/role/components/menuDialog.vue";
import Dialog from "@/views/sys/role/components/dialog.vue";
// // 设置 Axios 请求拦截器
// axios.interceptors.request.use(config => {
//     const token = localStorage.getItem('access_token');
//     if (token) {
//         config.headers['Authorization'] = `Bearer ${token}`;
//     }
//     return config;
// }, error => {
//     return Promise.reject(error);
// });
//
// // 设置 Axios 响应拦截器
// axios.interceptors.response.use(response => {
//     return response;
// }, error => {
//     const originalRequest = error.config;
//     if (error.response.status === 401 && !originalRequest._retry) {
//         originalRequest._retry = true;
//         const refreshToken = localStorage.getItem('refresh_token');
//         return axios.post('http://localhost:8000/user/token/refresh/', {
//             refresh: refreshToken
//         }).then(response => {
//             const { access } = response.data;
//             localStorage.setItem('access_token', access);
//             axios.defaults.headers.common['Authorization'] = `Bearer ${access}`;
//             return axios(originalRequest);
//         }).catch(error => {
//             ElMessage.error('Token 刷新失败，请重新登录!');
//             return Promise.reject(error);
//         });
//     }
//     return Promise.reject(error);
// });
const queryForm=ref({
  query:'',
  pageNum:1,
  pageSize:10
})

const total=ref(0)

const tableData=ref([])

const id=ref(-1)

const dialogVisible=ref(false)

const dialogTitle=ref('')

const delBtnStatus=ref(true)

const multipleSelection=ref([])

const menuDialogVisible=ref(false)

const handleMenuDialogValue=(roleId)=>{
  if (roleId){
    id.value=roleId
  }
  menuDialogVisible.value=true
}

const handleSelectionChange=(selection)=>{
  multipleSelection.value=selection;
  delBtnStatus.value=selection.length==0;
}

const handleDelete = async (id) => {
  var ids = [];
  if (id) {
    ids.push(id);
  } else {
    multipleSelection.value.forEach(row => {
      ids.push(row.id);
    });
  }
  try {
    // const res = await axios.delete(`http://localhost:8000/role/action`, { data: { id: ids } });
    // const res = await axios.delete(`http://localhost:8000/role/action?id=${ids.join(',')}`);
    const res = await requestUtil.del(`http://localhost:8000/role/action?id=${ids.join(',')}`);
    if (res.data.code == 200) {
      ElMessage({
        type: 'success',
        message: '操作成功！'
      });
      initRoleList();
    } else {
      ElMessage({
        type: 'error',
        message: res.data.msg,
      });
    }
  } catch (error) {
    if (error.response) {
      ElMessage({
        type: 'error',
        message: error.response.data.msg || '服务器内部错误，请稍后再试。'
      });
    } else {
      ElMessage({
        type: 'error',
        message: '请求失败，请检查网络连接。'
      });
    }
  }
};

const handleDialogValue=(roleId)=>{
  if (roleId){
    id.value=roleId;
    dialogTitle.value="角色修改"
  }else {
    id.value=-1;
    dialogTitle.value="角色添加"
  }
  dialogVisible.value=true
}

const initRoleList = async () => {
  try {
    // const res = await axios.post('http://localhost:8000/role/search', queryForm.value);
    const res = await requestUtil.post('http://localhost:8000/role/search', queryForm.value);
    tableData.value = res.data.roleList;
    total.value = res.data.total;
  } catch (error) {
    if (error.response) {
      console.error('错误状态码:', error.response.status);
      console.error('错误数据:', error.response.data);
      ElMessage.error(`服务器错误，状态码：${error.response.status}`);
    } else if (error.request) {
      console.error('请求已发出但没有收到响应。');
      ElMessage.error('请求失败，请检查网络连接。');
    } else {
      console.error('请求配置错误:', error.message);
      ElMessage.error('请求失败，请检查网络连接。');
    }
  }
};

initRoleList();

const handleSizeChange = (pageSize) => {
  queryForm.value.pageNum = 1; // 重置页码为第一页
  queryForm.value.pageSize = pageSize;
  initRoleList();
};

const handleCurrentChange = (pageNum) => {
  queryForm.value.pageNum = pageNum;
  initRoleList();
};
</script>

<template>
  <div class="app-container">
    <el-row :gutter="20" class="header">
      <el-col :span="7">
        <el-input placeholder="请输入用户名..." v-model="queryForm.query" clearable></el-input>
      </el-col>
      <el-button type="primary" :icon="Search" @click="initRoleList">搜索</el-button>
      <el-button type="success" :icon="DocumentAdd" @click="handleDialogValue()">新增</el-button>
      <el-popconfirm title="您确定要删除这些记录吗？" @confirm="handleDelete(null)">
        <template #reference>
          <el-button type="danger" :disabled="delBtnStatus" :icon="Delete">批量删除</el-button>
        </template>
      </el-popconfirm>
    </el-row>
    <el-table :data="tableData" stripe style="width: 100%" @selection-change="handleSelectionChange" empty-text="暂无数据">
      <el-table-column type="selection" width="55"/>
      <el-table-column prop="name" label="角色名" width="100" align="center"/>
      <el-table-column prop="code" label="权限字符" width="200" align="center"/>
      <el-table-column prop="create_time" label="创建时间" width="200" align="center"/>
      <el-table-column prop="remark" label="备注" />
      <el-table-column prop="action" label="操作" width="400" fixed="right" align="center" >
        <template v-slot="scope">
          <el-button type="primary" :icon="Tools" @click="handleMenuDialogValue(scope.row.id)">分配权限</el-button>
          <el-button v-if="scope.row.code!='admin'" type="primary" :icon="Edit" @click="handleDialogValue(scope.row.id)"/>
          <el-popconfirm v-if="scope.row.code!='admin'" title="您确定要删除这条记录吗？" @confirm="handleDelete(scope.row.id)">
            <template #reference>
              <el-button type="danger" :icon="Delete"/>
            </template>
          </el-popconfirm>
        </template>
      </el-table-column>


    </el-table>
    <el-pagination
      v-model:current-page="queryForm.pageNum"
      v-model:page-size="queryForm.pageSize"
      :page-sizes="[10, 20, 30, 40]"
      layout="total,sizes, prev, pager, next,jumper"
      :total="total"
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
    />
    <Dialog v-model="dialogVisible" :dialogVisible="dialogVisible" :id="id" :dialogTitle="dialogTitle"
    @initRoleList="initRoleList"></Dialog>
    <MenuDialog v-model="menuDialogVisible" :menuDialogVisible="menuDialogVisible" :id="id"
                @initRoleList="initRoleList"></MenuDialog>

  </div>
</template>

<style scoped lang="scss">

</style>