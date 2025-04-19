
<script setup>
import {defineEmits,defineProps,ref,watch} from "vue";
import requestUtil,{getServerUrl} from "@/util/request";
import {ElMessage} from "element-plus";
import axios from "axios";

const props = defineProps({
  userIds: {
    type: Array,
    default: () => [],
    required: true,
  },
  BatchRoleDialogVisible: {
    type: Boolean,
    default: false,
    required: true,
  },
  sysRoleList: {
    type: Array,
    default: () => [],
    required: true,
  },
});


const form = ref({
  userIds: props.userIds,
  checkedRoles: [],
});

const formRef = ref(null);

const initRoleList = async () => {
  const res = await axios.get("http://localhost:8000/role/listAll");
  form.value.roleList = res.data.roleList;
};

// const localUserIds = ref(props.userIds); // 创建一个本地状态
// watch(() => props.userIds, (newVal) => {
//   localUserIds.value = newVal; // 监听 props 的变化并更新本地状态
// });
// watch(
//     ()=>props.BatchRoleDialogVisible,
//     ()=>{
//       let id=props.userIds;
//       if (id!=[]){
//         form.value.checkedRoles=[]
//         props.sysRoleList.forEach(item=>{
//           form.value.checkedRoles.push(item.id);
//         })
//         initRoleList(id)
//       }
//     }
// )
watch(() => props.userIds, (newVal) => {
  form.value.userIds = newVal; // 监听 props.userIds 的变化并更新 form 中的值
});


watch(
  [() => props.BatchRoleDialogVisible, () => props.userIds],
  ([visible, userIds]) => {
    if (visible && userIds.length > 0) {
      form.value.userIds = userIds;
      // form.value.checkedRoles = [];
      props.sysRoleList.forEach(item => {
        form.value.checkedRoles.push(item.id);
      });
      initRoleList(); // 初始化角色列表
    }
  },
  { immediate: true }
);
const emits=defineEmits(['update:modelValue','initUserList'])
const handleConfirm = async () => {
  try {
    const result = await axios.post("http://localhost:8000/user/batchGrantRole", {
      userIds: form.value.userIds,
      roleIds: form.value.checkedRoles,
    });
    if (result.data.code === 200) {
      ElMessage.success("操作成功！");
      emits("update:modelValue", false);
      emits("initUserList");
    } else {
      ElMessage.error(result.data.msg);
    }
  } catch (error) {
    ElMessage.error("请求失败，请检查网络连接。");
  }
};

const handleClose = () => {
  emits("update:modelValue", false);
};


import { onMounted } from "vue";

onMounted(() => {
  console.log("初始化时的用户 ID:", props.userIds);
  if (props.userIds.length > 0) {
    form.value.userIds = props.userIds;
    form.value.checkedRoles = [];
    props.sysRoleList.forEach(item => {
      form.value.checkedRoles.push(item.id);
    });
    initRoleList();
  }
});


</script>

<template>
  <el-dialog :model-value="BatchRoleDialogVisible" title="分配角色" width="30%" @close="handleClose">
    <div v-if="form.userIds!=[]">
      正在为以下用户分配角色：<br>
      <el-tag v-for="userId in form.userIds" :key="userId" closable @close="removeUser(userId)">
        用户ID: {{ userId }}
      </el-tag>
    </div>
    <el-form ref="formRef" :model="form" label-width="100px">
      <el-checkbox-group v-model="form.checkedRoles">
        <el-checkbox v-for="role in form.roleList" :id="role.id" :key="role.id" :label="role.id" name="checkedRoles">
          {{role.name}}
        </el-checkbox>
      </el-checkbox-group>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button type="primary" @click="handleConfirm">确认</el-button>
        <el-button @click="handleClose">取消</el-button>
      </span>
    </template>
  </el-dialog>
</template>

<style scoped lang="scss">

</style>