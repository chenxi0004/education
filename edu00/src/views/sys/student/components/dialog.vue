
<script setup>
import axios from "axios";
import {defineEmits, defineProps, ref, watch, onUnmounted} from "vue";
import requestUtil from "@/util/request";
import {ElMessage} from "element-plus";

const props = defineProps({
  student_id: {
    type: String,
    default: "",
    required: true
  },
  dialogTitle: {
    type: String,
    default: '',
    required: true
  },
  dialogVisible: {
    type: Boolean,
    default: false,
    required: true
  }
});

const form=ref({
  student_id: "",
  student_name: "",
  gender: "",
  school: "",
  phone_number: "",
})


const formLoaded = ref(false);

const rules = ref({
  student_id:[{
    required:true,message:'请输入学生编号'
  }],
  student_name: [
    {required: true, message: '请输入学生姓名'}
  ],
  school: [
    {required: true, message: '请输入学校名称'}
  ]
});

const formRef = ref(null);
const initFormData = async () => {
  if (props.student_id) { // 确保使用 props.student_id
    try {
      const res = await requestUtil.get(`permission/action?student_id=${props.student_id}`);
      form.value = res.data.role || {
        student_id: "",
        student_name: "",
        gender: "",
        school: "",
        phone_number: "",
      };
      formLoaded.value = true; // 数据加载完成
    } catch (error) {
      console.error("加载表单数据失败：", error);
      form.value = {
        student_id: "",
        student_name: "",
        gender: "",
        school: "",
        phone_number: "",
      };
      formLoaded.value = true; // 确保模板渲染
    }
  } else {
    form.value = {
      student_id: "",
      student_name: "",
      gender: "",
      school: "",
      phone_number: "",
    };
    formLoaded.value = true; // 确保模板渲染
  }
};
watch(
  () => props.dialogVisible,
  (newVal) => {
    if (newVal) { // 如果对话框打开
      initFormData();
    }
  }
);
watch(
    () => props.dialogVisible,
    (newVal) => {
      if (newVal && props.student_id !== -1) {
        initFormData(props.student_id);
      } else {
        form.value = {
          student_id: "",
          student_name: "",
          gender: "",
          school: "",
          phone_number: "",
        };
        formLoaded.value = true; // 确保模板渲染
      }
    }
);

const emits = defineEmits(['update:modelValue', 'initRoleList']);

const handleClose = () => {
  emits('update:modelValue', false);
};

const handleConfirm = () => {
  formRef.value.validate(async (valid) => {
    if (valid) {
      try {
        // let result = await axios.post('http://localhost:8000/permission/save', form.value);
        let result = await requestUtil.post('http://localhost:8000/permission/save', form.value);
        let data = result.data;
        if (data.code == 200) {
          ElMessage.success("操作成功！");
          formRef.value.resetFields();
          emits('initRoleList');
          handleClose();
        } else {
          ElMessage.error(data.msg);
        }
      } catch (error) {
        console.error("提交表单时发生错误：", error);
        ElMessage.error("提交表单时发生错误，请稍后再试。");
      }
    } else {
      console.log("fail");
    }
  });
};

onUnmounted(() => {
  formRef.value = null;
});
</script>


<template>
    <!-- 新增/编辑对话框 -->
    <el-dialog
      :model-value="dialogVisible"
      :title="dialogTitle"
      width="30%"
      @close="handleClose">
      <el-form :model="form" ref="formRef" :rules="rules" label-width="100px">
        <el-form-item label="学生编号">
          <el-input v-model="form.student_id" placeholder="学生编号"></el-input>
        </el-form-item>
        <el-form-item label="学生姓名">
          <el-input v-model="form.student_name" placeholder="学生姓名"></el-input>
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