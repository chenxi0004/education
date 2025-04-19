<!--<script setup>-->
<!--import {Search,Delete,DocumentAdd,Edit,Tools,RefreshRight} from '@element-plus/icons-vue'-->
<!--import {ref} from "vue";-->
<!--import requestUtil,{getServerUrl} from "@/util/request"-->
<!--import {ElMessage} from "element-plus";-->
<!--import axios from "axios";-->
<!--import Dialog from "@/views/sys/user/components/dialog.vue";-->
<!--import RoleDialog from "@/views/sys/user/components/roleDialog.vue";-->
<!--const tableData=ref([])-->

<!--const total = ref(0);-->

<!--const queryForm=ref({-->
<!--  query:'',-->
<!--  student_or_teacher_id: '', // 新增学生/教师编号搜索-->
<!--  pageNum:1,-->
<!--  pageSize:10-->
<!--})-->

<!--const dialogVisible=ref(false)-->

<!--const dialogTitle=ref("")-->

<!--const id=ref(-1)-->

<!--const delBtnStatus=ref(true)-->

<!--const multipleSelection=ref([])-->

<!--const sysRoleList=ref([])-->
<!--const roleDialogVisible=ref(false)-->

<!--const handleSelectionChange=(selection)=>{-->
<!--  console.log("勾选了")-->
<!--  console.log(selection)-->
<!--  multipleSelection.value=selection;-->
<!--  delBtnStatus.value=selection.length==0;-->
<!--}-->

<!--// const handleBatchGrantRole = () => {-->
<!--//   if (multipleSelection.value.length === 0) {-->
<!--//     ElMessage.error("请先选择用户");-->
<!--//     return;-->
<!--//   }-->
<!--//   const userIds = multipleSelection.value.map((user) => user.id);-->
<!--//   // 弹出角色选择对话框，传入用户ID列表-->
<!--//   openRoleDialog(userIds);-->
<!--// };-->

<!--// const initUserList=async ()=>{-->
<!--//   // result=await requestUtil.post("user/save",form.value);-->
<!--//   const res=await axios.post('http://localhost:8000/user/search',queryForm.value)-->
<!--//   tableData.value=res.data.userList-->
<!--//   console.log(res.data)-->
<!--// }-->
<!--const initUserList = async () => {-->
<!--  try {-->
<!--    const res = await axios.post('http://localhost:8000/user/search', queryForm.value);-->
<!--    // const res = await axios.post('http://localhost:8000/user/search', {-->
<!--    //   query: queryForm.value.query,-->
<!--    //   student_or_teacher_id: queryForm.value.student_or_teacher_id,-->
<!--    //   pageNum: queryForm.value.pageNum,-->
<!--    //   pageSize: queryForm.value.pageSize-->
<!--    // });-->
<!--    tableData.value = res.data.users || [];-->
<!--    total.value = res.data.total || 0;-->
<!--  } catch (error) {-->
<!--    if (error.response) {-->
<!--      // 请求成功但状态码不在 2xx 范围-->
<!--      console.error("错误状态码:", error.response.status);-->
<!--      console.error("错误数据:", error.response.data);-->
<!--      ElMessage.error("服务器内部错误，请稍后再试。");-->
<!--    } else if (error.request) {-->
<!--      // 请求发出但没有收到响应-->
<!--      console.error("请求已发出但没有收到响应。");-->
<!--      ElMessage.error("请求失败，请检查网络连接。");-->
<!--    } else {-->
<!--      // 在设置请求时发生了错误-->
<!--      console.error("设置请求时发生错误:", error.message);-->
<!--      ElMessage.error("请求失败，请检查网络连接。");-->
<!--    }-->
<!--  }-->
<!--};-->


<!--const handleDelete = async (id) => {-->
<!--  var ids = [];-->
<!--  if (id) {-->
<!--    ids.push(id);-->
<!--  } else {-->
<!--    multipleSelection.value.forEach(row => {-->
<!--      ids.push(row.id);-->
<!--    });-->
<!--  }-->
<!--  try {-->
<!--    // const res = await axios.delete(`http://localhost:8000/user/action`, { data: { id: ids } });-->
<!--    const res = await axios.delete(`http://localhost:8000/user/action?id=${ids.join(',')}`);-->
<!--    if (res.data.code == 200) {-->
<!--      ElMessage({-->
<!--        type: 'success',-->
<!--        message: '操作成功！'-->
<!--      });-->
<!--      initUserList();-->
<!--    } else {-->
<!--      ElMessage({-->
<!--        type: 'error',-->
<!--        message: res.data.msg,-->
<!--      });-->
<!--    }-->
<!--  } catch (error) {-->
<!--    if (error.response) {-->
<!--      ElMessage({-->
<!--        type: 'error',-->
<!--        message: error.response.data.msg || '服务器内部错误，请稍后再试。'-->
<!--      });-->
<!--    } else {-->
<!--      ElMessage({-->
<!--        type: 'error',-->
<!--        message: '请求失败，请检查网络连接。'-->
<!--      });-->
<!--    }-->
<!--  }-->
<!--};-->

<!--// const handleBatchRoleDialog = () => {-->
<!--//   const userIds = multipleSelection.value.map(user => user.id);-->
<!--//   const roleIds = form.value.checkedRoles; // 获取已选中的角色ID-->
<!--//   axios.post('http://localhost:8000/user/batchGrantRole', { userIds, roleIds })-->
<!--//     .then(response => {-->
<!--//       if (response.data.code === 200) {-->
<!--//         ElMessage.success("批量分配权限成功！");-->
<!--//         initUserList();-->
<!--//       } else {-->
<!--//         ElMessage.error(response.data.msg);-->
<!--//       }-->
<!--//     })-->
<!--//     .catch(error => {-->
<!--//       ElMessage.error("批量分配权限失败，请检查网络连接。");-->
<!--//     });-->
<!--// };-->

<!--const handleSizeChange=(pageSize)=>{-->
<!--  queryForm.value.pageNum=1;-->
<!--  queryForm.value.pageSize=pageSize;-->
<!--  initUserList()-->
<!--}-->

<!--const handleCurrentChange=(pageNum)=>{-->
<!--  queryForm.value.pageNum=pageNum;-->
<!--  initUserList()-->
<!--}-->

<!--const handleDialogValue=(userId)=>{-->
<!--  if (userId){-->
<!--    id.value=userId;-->
<!--    dialogTitle.value="用户修改"-->
<!--  }else {-->
<!--    id.value=-1;-->
<!--    dialogTitle.value="用户添加"-->
<!--  }-->
<!--  dialogVisible.value=true-->
<!--}-->

<!--const handleResetPassword=async (id)=>{-->
<!--  const res=await requestUtil.get(`user/resetPassword?id=${id}`)-->
<!--   if (res.data.code == 200) {-->
<!--      ElMessage({-->
<!--        type: 'success',-->
<!--        message: '操作成功！'-->
<!--      });-->
<!--      initUserList();-->
<!--    } else {-->
<!--      ElMessage({-->
<!--        type: 'error',-->
<!--        message: res.data.msg,-->
<!--      });-->
<!--    }-->
<!--}-->

<!--// const statusChangeHandle=async (row)=>{-->
<!--//   let res=await axios.post('http://localhost:8000/user/status',{id:row.id,status:row.status});-->
<!--//      if (res.data.code == 200) {-->
<!--//       ElMessage({-->
<!--//         type: 'success',-->
<!--//         message: '操作成功！'-->
<!--//       });-->
<!--//-->
<!--//     } else {-->
<!--//       ElMessage({-->
<!--//         type: 'error',-->
<!--//         message: res.data.msg,-->
<!--//       });-->
<!--//       initUserList();-->
<!--//     }-->
<!--// }-->
<!--const statusChangeHandle = async (row) => {-->
<!--  try {-->
<!--    let res = await axios.post('http://localhost:8000/user/status', { id: row.id, status: row.status });-->
<!--    if (res.data.code == 200) {-->
<!--      ElMessage({-->
<!--        type: 'success',-->
<!--        message: '操作成功！'-->
<!--      });-->
<!--      initUserList(); // 在状态变更成功时重新加载用户列表-->
<!--    } else {-->
<!--      ElMessage({-->
<!--        type: 'error',-->
<!--        message: res.data.msg,-->
<!--      });-->
<!--      initUserList(); // 在状态变更失败时重新加载用户列表-->
<!--    }-->
<!--  } catch (error) {-->
<!--    if (error.response) {-->
<!--      console.error("错误状态码:", error.response.status);-->
<!--      console.error("错误数据:", error.response.data);-->
<!--      ElMessage.error("服务器内部错误，请稍后再试。");-->
<!--    } else if (error.request) {-->
<!--      console.error("请求已发出但没有收到响应。");-->
<!--      ElMessage.error("请求失败，请检查网络连接。");-->
<!--    } else {-->
<!--      console.error("设置请求时发生错误:", error.message);-->
<!--      ElMessage.error("请求失败，请检查网络连接。");-->
<!--    }-->
<!--    initUserList(); // 在请求失败时重新加载用户列表-->
<!--  }-->
<!--};-->

<!--const handleRoleDialogValue=(userId,roleList)=>{-->
<!--  // console.log("roleList:",roleList)-->
<!--  // console.log("id:",id)-->
<!--  id.value=userId;-->
<!--  sysRoleList.value=roleList;-->
<!--  roleDialogVisible.value=true-->
<!--}-->

<!--initUserList()-->

<!--</script>-->

<!--<template>-->
<!--  <div class="app-container">-->
<!--    <el-row :gutter="20" class="header">-->
<!--      <el-col :span="7">-->
<!--        <el-input placeholder="请输入用户名或学生/教师编号..." v-model="queryForm.query" clearable></el-input>-->
<!--      </el-col>-->
<!--      <el-button type="primary" :icon="Search" @click="initUserList">搜索</el-button>-->
<!--      <el-button type="success" :icon="DocumentAdd" @click="handleDialogValue()">新增</el-button>-->
<!--      <el-popconfirm title="您确定要删除这些记录吗？" @confirm="handleDelete(null)">-->
<!--        <template #reference>-->
<!--          <el-button type="danger" :disabled="delBtnStatus" :icon="Delete">批量删除</el-button>-->
<!--        </template>-->
<!--      </el-popconfirm>-->
<!--      <el-button-->
<!--        type="primary"-->
<!--        :disabled="multipleSelection.value.length === 0"-->
<!--        @click="handleRoleDialogValue(scope.row.id,scope.row.roleList)">-->
<!--        批量分配权限-->
<!--      </el-button>-->
<!--    </el-row>-->
<!--    <el-table :data="tableData" stripe style="width: 100%" @selection-change="handleSelectionChange" empty-text="暂无数据">-->
<!--      <el-table-column type="selection" width="55"/>-->
<!--      <el-table-column prop="avatar" label="头像" width="80" align="center" >-->
<!--        <template v-slot="scope">-->
<!--          <img :src="getServerUrl()+'media/userAvatar/'+scope.row.avatar" width="50" height="50"/>-->
<!--        </template>-->
<!--      </el-table-column>-->
<!--      <el-table-column prop="username" label="用户名" width="100" align="center"/>-->
<!--      <el-table-column prop="roles" label="拥有角色" width="200" align="center">-->
<!--        <template v-slot="scope">-->
<!--          <el-tag size="small" type="warning" v-for="item in scope.row.roleList">{{item.name}}</el-tag>-->
<!--        </template>-->
<!--      </el-table-column>-->
<!--      <el-table-column prop="student_or_teacher_id" label="学生/教师编号" width="200" align="center" />-->
<!--      <el-table-column prop="email" label="邮箱" width="200" align="center" />-->
<!--      <el-table-column prop="phonenumber" label="手机号码" width="120" align="center" />-->
<!--      <el-table-column prop="status" label="状态？" width="200" align="center">-->
<!--        <template v-slot="{row}">-->
<!--          <el-switch v-model="row.status" @change="statusChangeHandle(row)" active-text="正常"-->
<!--          inactive-text="禁用" :active-value="1" :inactive-value="0"></el-switch>-->
<!--        </template>-->
<!--      </el-table-column>-->
<!--      <el-table-column prop="create_time" label="创建时间" width="200" align="center" />-->
<!--      <el-table-column prop="login_time" label="最后登录时间" width="200" align="center" />-->
<!--      <el-table-column prop="remark" label="备注" />-->
<!--      <el-table-column prop="action" label="操作" width="400" fixed="right" align="center">-->
<!--        <template v-slot="scope">-->
<!--          <el-button type="primary" :icon="Tools" @click="handleRoleDialogValue(scope.row.id,scope.row.roleList)">分配角色</el-button>-->
<!--          <el-popconfirm v-if="scope.row.username!='py0'" title="您确定要对这个用户重置密码吗？" @confirm="handleResetPassword(scope.row.id)">-->
<!--            <template #reference>-->
<!--              <el-button type="warning" :icon="RefreshRight">重置密码</el-button>-->
<!--            </template>-->
<!--          </el-popconfirm>-->
<!--          <el-button type="primary" v-if="scope.row.username!='py0'" :icon="Edit" @click="handleDialogValue(scope.row.id)"></el-button>-->
<!--          <el-popconfirm v-if="scope.row.username!='py0'" title="您确定要删除这条记录吗？" @confirm="handleDelete(scope.row.id)">-->
<!--            <template #reference>-->
<!--              <el-button type="danger" :icon="Delete"/>-->
<!--            </template>-->
<!--          </el-popconfirm>-->



<!--        </template>-->
<!--      </el-table-column>-->

<!--    </el-table>-->
<!--    <el-pagination-->
<!--      v-model:current-page="queryForm.pageNum"-->
<!--      v-model:page-size="queryForm.pageSize"-->
<!--      :page-sizes="[10, 20, 30, 40]"-->
<!--      layout="total,sizes, prev, pager, next,jumper"-->
<!--      :total="total"-->
<!--      @size-change="handleSizeChange"-->
<!--      @current-change="handleCurrentChange"-->
<!--    />-->
<!--    <Dialog v-model="dialogVisible" :dialogVisible="dialogVisible" :id="id" :dialogTitle="dialogTitle"-->
<!--    @initUserList="initUserList"></Dialog>-->
<!--    <RoleDialog v-model="roleDialogVisible" :sysRoleList="sysRoleList" :roleDialogVisible="roleDialogVisible" :id="id"-->
<!--                @initUserList="initUserList"></RoleDialog>-->
<!--  </div>-->

<!--</template>-->

<!--<style scoped lang="scss">-->
<!--.app-container {-->
<!--  padding: 20px;-->
<!--  background-color: #f0f2f5;-->
<!--  min-height: 100vh;-->
<!--  display: flex;-->
<!--  flex-direction: column;-->
<!--  align-items: center;-->

<!--  .el-table {-->
<!--    width: 100%;-->
<!--    margin-bottom: 20px;-->
<!--    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);-->
<!--    border-radius: 8px;-->
<!--    overflow: hidden;-->
<!--    max-height: 600px; /* 设置最大高度 */-->
<!--    overflow-y: auto; /* 垂直方向超出时显示滚动条 */-->
<!--    overflow-x: auto; /* 水平方向超出时显示滚动条 */-->
<!--  }-->

<!--  .el-pagination {-->
<!--    float: right;-->
<!--    padding: 20px;-->
<!--    box-sizing: border-box;-->
<!--    width: 100%;-->
<!--    text-align: center;-->
<!--    margin-top: 20px;-->
<!--  }-->
<!--  .el-tag&#45;&#45;small {-->
<!--    margin-left: 5px;-->
<!--  }-->
<!--}-->
<!--</style>-->











<!--<script setup>-->
<!--import {Search,Delete,DocumentAdd,Edit,Tools,RefreshRight} from '@element-plus/icons-vue'-->
<!--import {ref} from "vue";-->
<!--import requestUtil,{getServerUrl} from "@/util/request"-->
<!--import {ElMessage} from "element-plus";-->
<!--import axios from "axios";-->
<!--import Dialog from "@/views/sys/user/components/dialog.vue";-->
<!--import RoleDialog from "@/views/sys/user/components/roleDialog.vue";-->
<!--const tableData=ref([])-->

<!--const total = ref(0);-->

<!--const queryForm=ref({-->
<!--  query:'',-->
<!--  pageNum:1,-->
<!--  pageSize:10-->
<!--})-->

<!--const dialogVisible=ref(false)-->

<!--const dialogTitle=ref("")-->

<!--const id=ref(-1)-->

<!--const delBtnStatus=ref(true)-->

<!--const multipleSelection=ref([])-->

<!--const sysRoleList=ref([])-->
<!--const roleDialogVisible=ref(false)-->

<!--const handleSelectionChange=(selection)=>{-->
<!--  console.log("勾选了")-->
<!--  console.log(selection)-->
<!--  multipleSelection.value=selection;-->
<!--  delBtnStatus.value=selection.length==0;-->
<!--}-->
<!--// const initUserList=async ()=>{-->
<!--//   // result=await requestUtil.post("user/save",form.value);-->
<!--//   const res=await axios.post('http://localhost:8000/user/search',queryForm.value)-->
<!--//   tableData.value=res.data.userList-->
<!--//   console.log(res.data)-->
<!--// }-->
<!--const initUserList = async () => {-->
<!--  try {-->
<!--    const res = await axios.post('http://localhost:8000/user/search', queryForm.value);-->
<!--    tableData.value = res.data.users || [];-->
<!--    total.value = res.data.total || 0;-->
<!--  } catch (error) {-->
<!--    if (error.response) {-->
<!--      // 请求成功但状态码不在 2xx 范围-->
<!--      console.error("错误状态码:", error.response.status);-->
<!--      console.error("错误数据:", error.response.data);-->
<!--      ElMessage.error("服务器内部错误，请稍后再试。");-->
<!--    } else if (error.request) {-->
<!--      // 请求发出但没有收到响应-->
<!--      console.error("请求已发出但没有收到响应。");-->
<!--      ElMessage.error("请求失败，请检查网络连接。");-->
<!--    } else {-->
<!--      // 在设置请求时发生了错误-->
<!--      console.error("设置请求时发生错误:", error.message);-->
<!--      ElMessage.error("请求失败，请检查网络连接。");-->
<!--    }-->
<!--  }-->
<!--};-->


<!--const handleDelete = async (id) => {-->
<!--  var ids = [];-->
<!--  if (id) {-->
<!--    ids.push(id);-->
<!--  } else {-->
<!--    multipleSelection.value.forEach(row => {-->
<!--      ids.push(row.id);-->
<!--    });-->
<!--  }-->
<!--  try {-->
<!--    // const res = await axios.delete(`http://localhost:8000/user/action`, { data: { id: ids } });-->
<!--    const res = await axios.delete(`http://localhost:8000/user/action?id=${ids.join(',')}`);-->
<!--    if (res.data.code == 200) {-->
<!--      ElMessage({-->
<!--        type: 'success',-->
<!--        message: '操作成功！'-->
<!--      });-->
<!--      initUserList();-->
<!--    } else {-->
<!--      ElMessage({-->
<!--        type: 'error',-->
<!--        message: res.data.msg,-->
<!--      });-->
<!--    }-->
<!--  } catch (error) {-->
<!--    if (error.response) {-->
<!--      ElMessage({-->
<!--        type: 'error',-->
<!--        message: error.response.data.msg || '服务器内部错误，请稍后再试。'-->
<!--      });-->
<!--    } else {-->
<!--      ElMessage({-->
<!--        type: 'error',-->
<!--        message: '请求失败，请检查网络连接。'-->
<!--      });-->
<!--    }-->
<!--  }-->
<!--};-->



<!--const handleSizeChange=(pageSize)=>{-->
<!--  queryForm.value.pageNum=1;-->
<!--  queryForm.value.pageSize=pageSize;-->
<!--  initUserList()-->
<!--}-->

<!--const handleCurrentChange=(pageNum)=>{-->
<!--  queryForm.value.pageNum=pageNum;-->
<!--  initUserList()-->
<!--}-->

<!--const handleDialogValue=(userId)=>{-->
<!--  if (userId){-->
<!--    id.value=userId;-->
<!--    dialogTitle.value="用户修改"-->
<!--  }else {-->
<!--    id.value=-1;-->
<!--    dialogTitle.value="用户添加"-->
<!--  }-->
<!--  dialogVisible.value=true-->
<!--}-->

<!--const handleResetPassword=async (id)=>{-->
<!--  const res=await requestUtil.get(`user/resetPassword?id=${id}`)-->
<!--   if (res.data.code == 200) {-->
<!--      ElMessage({-->
<!--        type: 'success',-->
<!--        message: '操作成功！'-->
<!--      });-->
<!--      initUserList();-->
<!--    } else {-->
<!--      ElMessage({-->
<!--        type: 'error',-->
<!--        message: res.data.msg,-->
<!--      });-->
<!--    }-->
<!--}-->

<!--// const statusChangeHandle=async (row)=>{-->
<!--//   let res=await axios.post('http://localhost:8000/user/status',{id:row.id,status:row.status});-->
<!--//      if (res.data.code == 200) {-->
<!--//       ElMessage({-->
<!--//         type: 'success',-->
<!--//         message: '操作成功！'-->
<!--//       });-->
<!--//-->
<!--//     } else {-->
<!--//       ElMessage({-->
<!--//         type: 'error',-->
<!--//         message: res.data.msg,-->
<!--//       });-->
<!--//       initUserList();-->
<!--//     }-->
<!--// }-->
<!--const statusChangeHandle = async (row) => {-->
<!--  try {-->
<!--    let res = await axios.post('http://localhost:8000/user/status', { id: row.id, status: row.status });-->
<!--    if (res.data.code == 200) {-->
<!--      ElMessage({-->
<!--        type: 'success',-->
<!--        message: '操作成功！'-->
<!--      });-->
<!--      initUserList(); // 在状态变更成功时重新加载用户列表-->
<!--    } else {-->
<!--      ElMessage({-->
<!--        type: 'error',-->
<!--        message: res.data.msg,-->
<!--      });-->
<!--      initUserList(); // 在状态变更失败时重新加载用户列表-->
<!--    }-->
<!--  } catch (error) {-->
<!--    if (error.response) {-->
<!--      console.error("错误状态码:", error.response.status);-->
<!--      console.error("错误数据:", error.response.data);-->
<!--      ElMessage.error("服务器内部错误，请稍后再试。");-->
<!--    } else if (error.request) {-->
<!--      console.error("请求已发出但没有收到响应。");-->
<!--      ElMessage.error("请求失败，请检查网络连接。");-->
<!--    } else {-->
<!--      console.error("设置请求时发生错误:", error.message);-->
<!--      ElMessage.error("请求失败，请检查网络连接。");-->
<!--    }-->
<!--    initUserList(); // 在请求失败时重新加载用户列表-->
<!--  }-->
<!--};-->

<!--const handleRoleDialogValue=(userId,roleList)=>{-->
<!--  // console.log("roleList:",roleList)-->
<!--  // console.log("id:",id)-->
<!--  id.value=userId;-->
<!--  sysRoleList.value=roleList;-->
<!--  roleDialogVisible.value=true-->
<!--}-->

<!--initUserList()-->

<!--</script>-->

<!--<template>-->
<!--  <div class="app-container">-->
<!--    <el-row :gutter="20" class="header">-->
<!--      <el-col :span="7">-->
<!--        <el-input placeholder="请输入用户名..." v-model="queryForm.query" clearable></el-input>-->
<!--      </el-col>-->
<!--      <el-button type="primary" :icon="Search" @click="initUserList">搜索</el-button>-->
<!--      <el-button type="success" :icon="DocumentAdd" @click="handleDialogValue()">新增</el-button>-->
<!--      <el-popconfirm title="您确定要删除这些记录吗？" @confirm="handleDelete(null)">-->
<!--        <template #reference>-->
<!--          <el-button type="danger" :disabled="delBtnStatus" :icon="Delete">批量删除</el-button>-->
<!--        </template>-->
<!--      </el-popconfirm>-->
<!--    </el-row>-->
<!--    <el-table :data="tableData" stripe style="width: 100%" @selection-change="handleSelectionChange" empty-text="暂无数据">-->
<!--      <el-table-column type="selection" width="55"/>-->
<!--      <el-table-column prop="avatar" label="头像" width="80" align="center" >-->
<!--        <template v-slot="scope">-->
<!--          <img :src="getServerUrl()+'media/userAvatar/'+scope.row.avatar" width="50" height="50"/>-->
<!--        </template>-->
<!--      </el-table-column>-->
<!--      <el-table-column prop="username" label="用户名" width="100" align="center"/>-->
<!--      <el-table-column prop="roles" label="拥有角色" width="200" align="center">-->
<!--        <template v-slot="scope">-->
<!--          <el-tag size="small" type="warning" v-for="item in scope.row.roleList">{{item.name}}</el-tag>-->
<!--        </template>-->
<!--      </el-table-column>-->
<!--      <el-table-column prop="student_or_teacher_id" label="学生/教师编号" width="200" align="center" />-->
<!--      <el-table-column prop="email" label="邮箱" width="200" align="center" />-->
<!--      <el-table-column prop="phonenumber" label="手机号码" width="120" align="center" />-->
<!--      <el-table-column prop="status" label="状态？" width="200" align="center">-->
<!--        <template v-slot="{row}">-->
<!--          <el-switch v-model="row.status" @change="statusChangeHandle(row)" active-text="正常"-->
<!--          inactive-text="禁用" :active-value="1" :inactive-value="0"></el-switch>-->
<!--        </template>-->
<!--      </el-table-column>-->
<!--      <el-table-column prop="create_time" label="创建时间" width="200" align="center" />-->
<!--      <el-table-column prop="login_time" label="最后登录时间" width="200" align="center" />-->
<!--      <el-table-column prop="remark" label="备注" />-->
<!--      <el-table-column prop="action" label="操作" width="400" fixed="right" align="center">-->
<!--        <template v-slot="scope">-->
<!--          <el-button type="primary" :icon="Tools" @click="handleRoleDialogValue(scope.row.id,scope.row.roleList)">分配角色</el-button>-->
<!--          <el-popconfirm v-if="scope.row.username!='py0'" title="您确定要对这个用户重置密码吗？" @confirm="handleResetPassword(scope.row.id)">-->
<!--            <template #reference>-->
<!--              <el-button type="warning" :icon="RefreshRight">重置密码</el-button>-->
<!--            </template>-->
<!--          </el-popconfirm>-->
<!--          <el-button type="primary" v-if="scope.row.username!='py0'" :icon="Edit" @click="handleDialogValue(scope.row.id)"></el-button>-->
<!--          <el-popconfirm v-if="scope.row.username!='py0'" title="您确定要删除这条记录吗？" @confirm="handleDelete(scope.row.id)">-->
<!--            <template #reference>-->
<!--              <el-button type="danger" :icon="Delete"/>-->
<!--            </template>-->
<!--          </el-popconfirm>-->



<!--        </template>-->
<!--      </el-table-column>-->

<!--    </el-table>-->
<!--    <el-pagination-->
<!--      v-model:current-page="queryForm.pageNum"-->
<!--      v-model:page-size="queryForm.pageSize"-->
<!--      :page-sizes="[10, 20, 30, 40]"-->
<!--      layout="total,sizes, prev, pager, next,jumper"-->
<!--      :total="total"-->
<!--      @size-change="handleSizeChange"-->
<!--      @current-change="handleCurrentChange"-->
<!--    />-->
<!--    <Dialog v-model="dialogVisible" :dialogVisible="dialogVisible" :id="id" :dialogTitle="dialogTitle"-->
<!--    @initUserList="initUserList"></Dialog>-->
<!--    <RoleDialog v-model="roleDialogVisible" :sysRoleList="sysRoleList" :roleDialogVisible="roleDialogVisible" :id="id"-->
<!--                @initUserList="initUserList"></RoleDialog>-->
<!--  </div>-->

<!--</template>-->

<!--<style scoped lang="scss">-->
<!--.app-container {-->
<!--  padding: 20px;-->
<!--  background-color: #f0f2f5;-->
<!--  min-height: 100vh;-->
<!--  display: flex;-->
<!--  flex-direction: column;-->
<!--  align-items: center;-->

<!--  .el-table {-->
<!--    width: 100%;-->
<!--    margin-bottom: 20px;-->
<!--    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);-->
<!--    border-radius: 8px;-->
<!--    overflow: hidden;-->
<!--    max-height: 600px; /* 设置最大高度 */-->
<!--    overflow-y: auto; /* 垂直方向超出时显示滚动条 */-->
<!--    overflow-x: auto; /* 水平方向超出时显示滚动条 */-->
<!--  }-->

<!--  .el-pagination {-->
<!--    float: right;-->
<!--    padding: 20px;-->
<!--    box-sizing: border-box;-->
<!--    width: 100%;-->
<!--    text-align: center;-->
<!--    margin-top: 20px;-->
<!--  }-->
<!--  .el-tag&#45;&#45;small {-->
<!--    margin-left: 5px;-->
<!--  }-->
<!--}-->
<!--</style>-->




<script setup>
import {Search,Delete,DocumentAdd,Edit,Tools,RefreshRight} from '@element-plus/icons-vue'
import {ref} from "vue";
import requestUtil,{getServerUrl} from "@/util/request"
import {ElMessage} from "element-plus";
import axios from "axios";
import Dialog from "@/views/sys/user/components/dialog.vue";
import RoleDialog from "@/views/sys/user/components/roleDialog.vue";
import BatchroleDialog from "@/views/sys/user/components/batchroleDialog.vue";
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
//             ElMessage.error('Token 刷新失败，请重新登录。');
//             return Promise.reject(error);
//         });
//     }
//     return Promise.reject(error);
// });


const tableData=ref([])

const total = ref(0);

const queryForm=ref({
  query:'',
  pageNum:1,
  pageSize:10
})

const dialogVisible=ref(false)

const dialogTitle=ref("")

const id=ref(-1)

const delBtnStatus=ref(true)

const multipleSelection=ref([])

const sysRoleList=ref([])
const roleDialogVisible=ref(false)
const BatchRoleDialogVisible=ref(false)
const selectedUserIds = ref([]); // 选中的用户ID数组

const handleSelectionChange=(selection)=>{
  multipleSelection.value=selection;
  delBtnStatus.value=selection.length==0;
}
const initUserList = async () => {
  try {
    const res = await axios.post('http://localhost:8000/user/search', queryForm.value);
    tableData.value = res.data.users || [];
    total.value = res.data.total || 0;
  } catch (error) {
    if (error.response) {
      // 请求成功但状态码不在 2xx 范围
      console.error("错误状态码:", error.response.status);
      console.error("错误数据:", error.response.data);
      ElMessage.error("服务器内部错误，请稍后再试。");
    } else if (error.request) {
      // 请求发出但没有收到响应
      console.error("请求已发出但没有收到响应。");
      ElMessage.error("请求失败，请检查网络连接。");
    } else {
      // 在设置请求时发生了错误
      console.error("设置请求时发生错误:", error.message);
      ElMessage.error("请求失败，请检查网络连接。");
    }
  }
};


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
    // const res = await axios.delete(`http://localhost:8000/user/action`, { data: { id: ids } });
    const res = await axios.delete(`http://localhost:8000/user/action?id=${ids.join(',')}`);
    if (res.data.code == 200) {
      ElMessage({
        type: 'success',
        message: '操作成功！'
      });
      initUserList();
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



const handleSizeChange=(pageSize)=>{
  queryForm.value.pageNum=1;
  queryForm.value.pageSize=pageSize;
  initUserList()
}

const handleCurrentChange=(pageNum)=>{
  queryForm.value.pageNum=pageNum;
  initUserList()
}

const handleDialogValue=(userId)=>{
  if (userId){
    id.value=userId;
    dialogTitle.value="用户修改"
  }else {
    id.value=-1;
    dialogTitle.value="用户添加"
  }
  dialogVisible.value=true
}

const handleResetPassword=async (id)=>{
  const res=await requestUtil.get(`user/resetPassword?id=${id}`)
   if (res.data.code == 200) {
      ElMessage({
        type: 'success',
        message: '操作成功！'
      });
      initUserList();
    } else {
      ElMessage({
        type: 'error',
        message: res.data.msg,
      });
    }
}

const statusChangeHandle = async (row) => {
  try {
    let res = await axios.post('http://localhost:8000/user/status', { id: row.id, status: row.status });
    if (res.data.code == 200) {
      ElMessage({
        type: 'success',
        message: '操作成功！'
      });
      initUserList(); // 在状态变更成功时重新加载用户列表
    } else {
      ElMessage({
        type: 'error',
        message: res.data.msg,
      });
      initUserList(); // 在状态变更失败时重新加载用户列表
    }
  } catch (error) {
    if (error.response) {
      console.error("错误状态码:", error.response.status);
      console.error("错误数据:", error.response.data);
      ElMessage.error("服务器内部错误，请稍后再试。");
    } else if (error.request) {
      console.error("请求已发出但没有收到响应。");
      ElMessage.error("请求失败，请检查网络连接。");
    } else {
      console.error("设置请求时发生错误:", error.message);
      ElMessage.error("请求失败，请检查网络连接。");
    }
    initUserList(); // 在请求失败时重新加载用户列表
  }
};

const handleRoleDialogValue=(Id,roleList)=>{
  // console.log("roleList:",roleList)
  // console.log("id:",id)
  id.value=Id;
  sysRoleList.value=roleList;
  roleDialogVisible.value=true
}
const openRoleDialogForBatch = () => {
  if (multipleSelection.value.length === 0) {
    ElMessage.error("请先选择用户！");
    return;
  }
  selectedUserIds.value = multipleSelection.value.map((user) => user.id);
  BatchRoleDialogVisible.value = true;
};
initUserList()

</script>

<template>
  <div class="app-container">
    <el-row :gutter="20" class="header">
      <el-col :span="7">
        <el-input placeholder="请输入用户名..." v-model="queryForm.query" clearable></el-input>
      </el-col>
      <el-button type="primary" :icon="Search" @click="initUserList">搜索</el-button>
      <el-button type="success" :icon="DocumentAdd" @click="handleDialogValue()">新增</el-button>
      <el-button type="primary" :disabled="multipleSelection.length === 0" @click="openRoleDialogForBatch()">批量分配角色</el-button>
      <el-popconfirm title="您确定要删除这些记录吗？" @confirm="handleDelete(null)">
        <template #reference>
          <el-button type="danger" :disabled="delBtnStatus" :icon="Delete">批量删除</el-button>
        </template>
      </el-popconfirm>
    </el-row>
    <el-table :data="tableData" stripe style="width: 100%" @selection-change="handleSelectionChange" empty-text="暂无数据">
      <el-table-column type="selection" width="55"/>
      <el-table-column prop="avatar" label="头像" width="80" align="center" >
        <template v-slot="scope">
          <img :src="getServerUrl()+'media/userAvatar/'+scope.row.avatar" width="50" height="50"/>
        </template>
      </el-table-column>
      <el-table-column prop="username" label="用户名" width="100" align="center"/>
      <el-table-column prop="roles" label="拥有角色" width="200" align="center">
        <template v-slot="scope">
          <el-tag size="small" type="warning" v-for="item in scope.row.roleList">{{item.name}}</el-tag>
        </template>
      </el-table-column>
      <el-table-column prop="student_or_teacher_id" label="学生/教师编号" width="200" align="center" />
      <el-table-column prop="email" label="邮箱" width="200" align="center" />
      <el-table-column prop="phonenumber" label="手机号码" width="120" align="center" />
      <el-table-column prop="status" label="状态？" width="200" align="center">
        <template v-slot="{row}">
          <el-switch v-model="row.status" @change="statusChangeHandle(row)" active-text="正常"
          inactive-text="禁用" :active-value="1" :inactive-value="0"></el-switch>
        </template>
      </el-table-column>
      <el-table-column prop="create_time" label="创建时间" width="200" align="center" />
      <el-table-column prop="login_time" label="最后登录时间" width="200" align="center" />
      <el-table-column prop="remark" label="备注" />
      <el-table-column prop="action" label="操作" width="400" fixed="right" align="center">
        <template v-slot="scope">
          <el-button type="primary" :icon="Tools" @click="handleRoleDialogValue(scope.row.id,scope.row.roleList)">分配角色</el-button>
          <el-popconfirm v-if="scope.row.username!='py0'" title="您确定要对这个用户重置密码吗？" @confirm="handleResetPassword(scope.row.id)">
            <template #reference>
              <el-button type="warning" :icon="RefreshRight">重置密码</el-button>
            </template>
          </el-popconfirm>
          <el-button type="primary" v-if="scope.row.username!='py0'" :icon="Edit" @click="handleDialogValue(scope.row.id)"></el-button>
          <el-popconfirm v-if="scope.row.username!='py0'" title="您确定要删除这条记录吗？" @confirm="handleDelete(scope.row.id)">
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
    @initUserList="initUserList"></Dialog>
    <RoleDialog v-model="roleDialogVisible" :sysRoleList="sysRoleList" :roleDialogVisible="roleDialogVisible" :id="id"
                @initUserList="initUserList"></RoleDialog>
    <BatchroleDialog v-model="BatchRoleDialogVisible" :userIds="selectedUserIds" :sysRoleList="sysRoleList" :roleDialogVisible="roleDialogVisible"
                @initUserList="initUserList"></BatchroleDialog>
  </div>

</template>

<style scoped lang="scss">
.app-container {
  padding: 20px;
  background-color: #f0f2f5;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;

  .el-table {
    width: 100%;
    margin-bottom: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
    overflow: hidden;
    max-height: 600px; /* 设置最大高度 */
    overflow-y: auto; /* 垂直方向超出时显示滚动条 */
    overflow-x: auto; /* 水平方向超出时显示滚动条 */
  }

  .el-pagination {
    float: right;
    padding: 20px;
    box-sizing: border-box;
    width: 100%;
    text-align: center;
    margin-top: 20px;
  }
  .el-tag--small {
    margin-left: 5px;
  }
}
</style>