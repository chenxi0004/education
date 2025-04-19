<script setup>

import {Delete, DocumentAdd, Edit} from "@element-plus/icons-vue";
import {ref} from "vue";
import requestUtil,{getServerUrl} from "@/util/request";
import {ElMessage,ElMessageBox} from "element-plus";
import Dialog from "@/views/sys/menu/components/dialog.vue";
import axios from "axios";
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
const tableData=ref([])

const id=ref(-1)

const dialogVisible=ref(false)

const dialogTitle=ref('')

const handleDialogValue=(menuId)=>{
  if (menuId){
    id.value=menuId;
    dialogTitle.value="菜单修改"
  }else {
    id.value=-1;
    dialogTitle.value="菜单添加"
  }
  dialogVisible.value=true
}

const handleDelete=async (id)=>{
  console.log(id)
  // const res=await axios.delete(`http://localhost:8000/menu/action?id=${id}` )
  const res=await requestUtil.del(`http://localhost:8000/menu/action?id=${id}` )
  if (res.data.code==200){
    ElMessage({
      type:"success",
      message:'操作成功！'
    })
    initMenuList();
  }else {
    ElMessage({
      type:'error',
      message:res.data.msg
    })
  }
}

const initMenuList =async ()=>{
  const res=await requestUtil.get("menu/treeList");
  tableData.value=res.data.treeList;
}

initMenuList()

</script>

<template>
  <div class="app-container">
    <el-row class="header">
      <el-button type="success" :icon="DocumentAdd" @click="handleDialogValue()">新增</el-button>
    </el-row>
    <el-table :data="tableData" style="width: 100%;margin-bottom: 20px" row-key="id" border stripe default-expand-all :tree-props="{children:'children',hasChildren:'hasChildren'}">
      <el-table-column prop="name" label="菜单名称" width="180"/>
      <el-table-column prop="icon" label="图标" width="70" align="center">
        <template v-slot="scope">
          <el-icon>
            <svg-icon :icon-class="scope.row.icon"/>
          </el-icon>
        </template>
      </el-table-column>
      <el-table-column prop="order_num" label="排序" width="70" align="center"/>
      <el-table-column prop="perms" label="权限标识" width="200"/>
      <el-table-column prop="path" label="组件路径" width="180"/>
      <el-table-column prop="menu_type" label="菜单类型" width="120" align="center">
        <template v-slot="scope">
          <el-tag size="small" v-if="scope.row.menuType==='M'" type="danger" effect="dark">目录</el-tag>
          <el-tag size="small" v-else-if="scope.row.menuType==='C'" type="success" effect="dark">菜单</el-tag>
        </template>
      </el-table-column>
      <el-table-column prop="create_time" label="创建时间" align="center"/>
      <el-table-column prop="action" label="操作" width="300" fixed="right" align="center">
        <template v-slot="scope">
          <el-button type="primary" :icon="Edit" @click="handleDialogValue(scope.row.id)"/>
          <el-popconfirm title="您确定要删除这条记录吗？" @confirm="handleDelete(scope.row.id)">
            <template #reference>
              <el-button type="danger" :icon="Delete"/>
            </template>
          </el-popconfirm>
        </template>
      </el-table-column>
    </el-table>
    <Dialog v-model="dialogVisible" :tableData="tableData" :dialogVisible="dialogVisible" :id="id" :dialogTitle="dialogTitle"
            @initMenuList="initMenuList"></Dialog>
  </div>
</template>

<style scoped lang="scss">

</style>