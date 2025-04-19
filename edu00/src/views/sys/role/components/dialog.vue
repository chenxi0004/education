<!--<script setup>-->
<!--import {defineEmits,defineProps,ref,watch} from "vue";-->
<!--import requestUtil,{getServerUrl} from "@/util/request";-->
<!--import {ElMessage} from "element-plus";-->
<!--import axios from "axios";-->

<!--const props=defineProps(-->
<!--    {-->
<!--      id:{-->
<!--        type:Number,-->
<!--        default:-1,-->
<!--        required:true-->
<!--      },-->
<!--      dialogTitle:{-->
<!--        type:String,-->
<!--        default:'',-->
<!--        required:true-->
<!--      },-->
<!--      dialogVisible:{-->
<!--        type:Boolean,-->
<!--        default:false,-->
<!--        required:true-->
<!--      }-->
<!--  }-->
<!--)-->
<!--const form=ref({-->
<!--  id:-1,-->
<!--  name:"",-->
<!--  code:"",-->
<!--  remark:""-->
<!--})-->
<!--//-->
<!--// const checkRolename = async (rule, value, callback) => {-->
<!--//   if (form.value.id == -1) {-->
<!--//     try {-->
<!--//       const res = await axios.post(`http://localhost:8000/role/check`, { name: form.value.name,code:form.value.code });-->
<!--//       if (res.data.code == 500) {-->
<!--//         callback(new Error("角色名已存在！"));-->
<!--//       } else {-->
<!--//         callback();-->
<!--//       }-->
<!--//     } catch (error) {-->
<!--//       console.error("检查角色名时发生错误：", error);-->
<!--//       callback(new Error("检查角色名时发生错误，请稍后再试。"));-->
<!--//     }-->
<!--//   } else {-->
<!--//     callback();-->
<!--//   }-->
<!--// };-->



<!--const rules = ref({-->
<!--      name: [-->
<!--        { required: true, message: '请输入角色名称' },-->
<!--        // { min: 2, max: 20, message: '角色名称长度应在 2 到 20 个字符之间', trigger: 'blur' },-->
<!--        // { pattern: /^[a-zA-Z0-9_\u4e00-\u9fa5]+$/, message: '角色名称只能包含字母、数字、下划线或汉字', trigger: 'blur' },-->
<!--        // { validator: checkRolename, trigger: 'blur' }-->
<!--      ],-->
<!--      code: [-->
<!--        { required: true, message: '请输入权限字符'},-->
<!--        // { min: 2, max: 50, message: '权限字符长度应在 2 到 50 个字符之间', trigger: 'blur' },-->
<!--        // { pattern: /^[a-zA-Z0-9_]+$/, message: '权限字符只能包含字母、数字或下划线', trigger: 'blur' },-->
<!--      ],-->
<!--    });-->

<!--const formRef = ref(null);-->

<!--const initFormData = async (id) => {-->
<!--  const res = await requestUtil.get(`role/action?id=${id}`);-->
<!--  form.value = res.data.role;-->
<!--};-->

<!--watch(-->
<!--    ()=>props.dialogVisible,-->
<!--    ()=>{-->
<!--      let id=props.id;-->
<!--      if(id!=-1){-->
<!--        initFormData(id)-->
<!--      }else {-->
<!--        form.value={-->
<!--          id:-1,-->
<!--          name:"",-->
<!--          code:"",-->
<!--          remark:""-->
<!--        }-->
<!--      }-->
<!--    }-->
<!--)-->
<!--// watch(-->
<!--//   () => props.id,-->
<!--//   (newId) => {-->
<!--//     if (newId !== -1) {-->
<!--//       initFormData(newId);-->
<!--//     } else {-->
<!--//       form.value = {-->
<!--//         id: -1,-->
<!--//         name: "",-->
<!--//         code: "",-->
<!--//         remark: ""-->
<!--//       };-->
<!--//     }-->
<!--//   }-->
<!--// );-->
<!--const emits=defineEmits(['update:modelValue','initRoleList'])-->

<!--const handleClose = () => {-->
<!--  emits('update:modelValue', false);-->
<!--};-->

<!--const handleConfirm = () => {-->
<!--  formRef.value.validate(async (valid) => {-->
<!--    if (valid) {-->
<!--      let result = await axios.post('http://localhost:8000/role/save', form.value);-->
<!--      let data = result.data;-->
<!--      if (data.code == 200) {-->
<!--        ElMessage.success("操作成功！");-->
<!--        formRef.value.resetFields();-->
<!--        emits('initRoleList');-->
<!--        handleClose();-->
<!--      } else {-->
<!--        ElMessage.error(data.msg);-->
<!--      }-->
<!--    } else {-->
<!--      console.log("fail");-->
<!--    }-->
<!--  });-->
<!--};-->
<!--</script>-->

<!--<template>-->
<!--  <el-dialog-->
<!--      model-value="dialogVisible"-->
<!--      :title="dialogTitle"-->
<!--      width="30%"-->
<!--      @close="handleClose">-->
<!--    <el-form ref="formRef" :model="form" :rules="rules" label-width="100px">-->
<!--      <el-form-item label="角色名" prop="name">-->
<!--&lt;!&ndash;        <el-input v-model="form.name" :disabled="form.id==-1?false:'disabled'"/>&ndash;&gt;-->
<!--        <el-input v-model="form.name"/>-->
<!--      </el-form-item>-->
<!--      <el-form-item label="权限字符" prop="code">-->
<!--        <el-input v-model="form.code"/>-->
<!--      </el-form-item>-->
<!--      <el-form-item label="备注" prop="remark">-->
<!--        <el-input v-model="form.remark" type="textarea" :rows="4"/>-->
<!--      </el-form-item>-->
<!--    </el-form>-->
<!--    <template #footer>-->
<!--      <span class="dialog-footer">-->
<!--        <el-button type="primary" @click="handleConfirm">确认</el-button>-->
<!--        <el-button @click="handleClose">取消</el-button>-->
<!--      </span>-->
<!--    </template>-->
<!--  </el-dialog>-->
<!--</template>-->

<!--<style scoped lang="scss">-->

<!--</style>-->

<template>
  <el-dialog
      :model-value="dialogVisible"
      :title="dialogTitle"
      width="30%"
      @close="handleClose">
    <el-form v-if="formLoaded" ref="formRef" :model="form" :rules="rules" label-width="100px">
      <el-form-item label="角色名" prop="name">
        <el-input v-model="form.name"/>
      </el-form-item>
      <el-form-item label="权限字符" prop="code">
        <el-input v-model="form.code"/>
      </el-form-item>
      <el-form-item label="备注" prop="remark">
        <el-input v-model="form.remark" type="textarea" :rows="4"/>
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

<script setup>
import {defineEmits, defineProps, ref, watch, onUnmounted} from "vue";
import requestUtil from "@/util/request";
import {ElMessage} from "element-plus";
import axios from "axios";

const props = defineProps({
  id: {
    type: Number,
    default: -1,
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

const form = ref({
  id: -1,
  name: "",
  code: "",
  remark: ""
});

const formLoaded = ref(false);

const rules = ref({
  name: [
    {required: true, message: '请输入角色名称'}
  ],
  code: [
    {required: true, message: '请输入权限字符'}
  ]
});

const formRef = ref(null);

const initFormData = async (id) => {
  try {
    const res = await requestUtil.get(`role/action?id=${id}`);
    // const res = await requestUtil.get("role/action?id="+id);
    console.log(res.data.role)
    form.value = res.data.role || {
      id: -1,
      name: "",
      code: "",
      remark: ""
    };
    formLoaded.value = true; // 数据加载完成
  } catch (error) {
    console.error("加载表单数据失败：", error);
    form.value = {
      id: -1,
      name: "",
      code: "",
      remark: ""
    };
    formLoaded.value = true; // 确保模板渲染
  }
};

watch(
    () => props.dialogVisible,
    (newVal) => {
      if (newVal && props.id !== -1) {
        initFormData(props.id);
      } else {
        form.value = {
          id: -1,
          name: "",
          code: "",
          remark: ""
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
        // let result = await axios.post('http://localhost:8000/role/save', form.value);
        let result = await requestUtil.post('http://localhost:8000/role/save', form.value);
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

<style scoped lang="scss">
</style>