<!--<script setup>-->
<!--import {defineEmits,defineProps,ref,watch} from "vue";-->
<!--import requestUtil from "@/util/request";-->
<!--import {ElMessage} from "element-plus";-->
<!--import axios from "axios";-->

<!--const tableData=ref([])-->

<!--const props=defineProps({-->
<!--  id:{-->
<!--    type:Number,-->
<!--    default:-1,-->
<!--    required:true-->
<!--  },-->
<!--  dialogTitle:{-->
<!--    type:String,-->
<!--    default:'',-->
<!--    required:true-->
<!--  },-->
<!--  dialogVisible:{-->
<!--    type:Boolean,-->
<!--    default:false,-->
<!--    required:true-->
<!--  }-->
<!--  ,-->
<!--  tableData:{-->
<!--    type:Array,-->
<!--    default:[],-->
<!--    required:true-->
<!--  }-->
<!--})-->

<!--const form=ref({-->
<!--  id:-1,-->
<!--  parent_id:'',-->
<!--  menu_type:"M",-->
<!--  icon:'',-->
<!--  name:'',-->
<!--  perms:'',-->
<!--  path:'',-->
<!--  component:'',-->
<!--  order_num:1,-->
<!--  remark:''-->
<!--})-->

<!--const rules=ref({-->
<!--  parentId:[{required:true,message:'请选择上级菜单'}],-->
<!--  name:[{required:true,message:'菜单名称不能为空',trigger:"blur"}]-->
<!--})-->

<!--const formRef=ref(null)-->

<!--const initFormData=async (id)=>{-->
<!--  const res=await requestUtil.get(`menu/action?id=${id}`);-->
<!--  form.value=res.data.menu;-->
<!--  console.log(res.data.menu)-->
<!--}-->

<!--watch(-->
<!--    ()=>props.dialogVisible,-->
<!--    ()=>{-->
<!--      let id=props.id;-->
<!--      if(id!=-1){-->
<!--        initFormData(id)-->
<!--      }else {-->
<!--        form.value={-->
<!--          id:-1,-->
<!--          parent_id:'',-->
<!--          menu_type:"M",-->
<!--          icon:'',-->
<!--          name:'',-->
<!--          perms:'',-->
<!--          path:'',-->
<!--          component:'',-->
<!--          order_num:1,-->
<!--          remark:''-->
<!--        }-->
<!--      }-->
<!--    }-->
<!--)-->

<!--const emits=defineEmits(['update:modelValue','initMenuList'])-->

<!--const handleClose=()=>{-->
<!--  emits('update:modelValue',false)-->
<!--}-->

<!--const handleConfirm = () => {-->
<!--  formRef.value.validate(async (valid) => {-->
<!--    if (valid) {-->
<!--      let result = await axios.post('http://localhost:8000/menu/save', form.value);-->
<!--      let data = result.data;-->
<!--      if (data.code == 200) {-->
<!--        ElMessage.success("操作成功！");-->
<!--        formRef.value.resetFields();-->
<!--        emits('initMenuList');-->
<!--        handleClose();-->
<!--      } else {-->
<!--        ElMessage.error(data.msg);-->
<!--      }-->
<!--    } else {-->
<!--      console.log("fail");-->
<!--    }-->
<!--  });-->
<!--};-->

<!--// import { onUnmounted } from "vue";-->
<!--//-->
<!--// const resizeObserver = new ResizeObserver(() => {-->
<!--//   // 处理尺寸变化的逻辑-->
<!--// });-->
<!--//-->
<!--// onUnmounted(() => {-->
<!--//   resizeObserver.disconnect(); // 停止观察所有元素-->
<!--// });-->
<!--</script>-->

<!--<template>-->
<!--  <el-dialog-->
<!--      model-value="dialogVisible"-->
<!--      :title="dialogTitle"-->
<!--      width="30%"-->
<!--      @close="handleClose">-->
<!--    <el-form ref="formRef" :model="form" :rules="rules" label-width="100px">-->
<!--      <el-form-item label="上级菜单" prop="parent_id">-->
<!--        <el-select v-model="form.parent_id" placeholder="请选择上级菜单">-->
<!--          <template v-for="item in tableData">-->
<!--            <el-option :label="item.name" :value="item.id"></el-option>-->
<!--            <template v-for="child in item.children">-->
<!--              <el-option :label="child.name" :value="child.id">-->
<!--                <span>{{"  &#45;&#45;"+child.name}}</span>-->
<!--              </el-option>-->
<!--            </template>-->
<!--          </template>-->
<!--        </el-select>-->
<!--      </el-form-item>-->
<!--      <el-form-item label="菜单类型" prop="menu_type" label-width="100px">-->
<!--        <el-radio-group v-model="form.menu_type">-->
<!--          <el-radio :label="'M'">目录</el-radio>-->
<!--          <el-radio :label="'C'">菜单</el-radio>-->
<!--        </el-radio-group>-->
<!--      </el-form-item>-->
<!--      <el-form-item label="菜单图标" prop="icon">-->
<!--        <el-input v-model="form.icon"/>-->
<!--      </el-form-item>-->
<!--      <el-form-item label="菜单名称" prop="name">-->
<!--        <el-input v-model="form.name"/>-->
<!--      </el-form-item>-->
<!--      <el-form-item label="权限标识" prop="perms">-->
<!--        <el-input v-model="form.perms"/>-->
<!--      </el-form-item>-->
<!--      <el-form-item label="路径路由" prop="component">-->
<!--        <el-input v-model="form.path"/>-->
<!--      </el-form-item>-->
<!--      <el-form-item label="组件路径" prop="component">-->
<!--        <el-input v-model="form.component"/>-->
<!--      </el-form-item>-->
<!--      <el-form-item label="显示顺序" prop="order_num">-->
<!--        <el-input-number v-model="form.order_num" :min="1" label="显示顺序"></el-input-number>-->
<!--      </el-form-item>-->
<!--      <el-form-item label="备注" prop="remark">-->
<!--        <el-input v-model="form.remark"/>-->
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
<script setup>
import { defineEmits, defineProps, ref, watch } from "vue";
import requestUtil from "@/util/request";
import { ElMessage } from "element-plus";
import axios from "axios";

const tableData = ref([]);

const props = defineProps({
  id: {
    type: Number,
    default: -1,
    required: true
  },
  dialogTitle: {
    type: String,
    default: "",
    required: true
  },
  dialogVisible: {
    type: Boolean,
    default: false,
    required: true
  },
  tableData: {
    type: Array,
    default: () => [],
    required: true
  }
});

const form = ref({
  id: -1,
  parent_id: "",
  menu_type: "M",
  icon: "",
  name: "",
  perms: "",
  path: "",
  component: "",
  order_num: 1,
  remark: ""
});

const rules = ref({
  parentId: [{ required: true, message: "请选择上级菜单" }],
  name: [{ required: true, message: "菜单名称不能为空", trigger: "blur" }]
});

const formRef = ref(null);

const initFormData = async (id) => {
  const res = await requestUtil.get(`menu/action?id=${id}`);
  form.value = res.data.menu;
  console.log(res.data.menu);
};

watch(
  () => props.dialogVisible,
  () => {
    let id = props.id;
    if (id !== -1) {
      initFormData(id);
    } else {
      form.value = {
        id: -1,
        parent_id: "",
        menu_type: "M",
        icon: "",
        name: "",
        perms: "",
        path: "",
        component: "",
        order_num: 1,
        remark: ""
      };
    }
  }
);

const emits = defineEmits(["update:modelValue", "initMenuList"]);

const handleClose = () => {
  emits("update:modelValue", false);
};

const handleConfirm = () => {
  formRef.value.validate(async (valid) => {
    if (valid) {
      // let result = await axios.post("http://localhost:8000/menu/save", form.value);
      let result = await requestUtil.post("http://localhost:8000/menu/save", form.value);
      let data = result.data;
      console.log(data)
      if (data.code == 200) {
        ElMessage.success("操作成功！");
        formRef.value.resetFields();
        emits("initMenuList");
        handleClose();
      } else {
        ElMessage.error(data.msg);
      }
    } else {
      console.log("fail");
    }
  });
};
// const handleConfirm = () => {
//   formRef.value.validate(async (valid) => {
//     if (valid) {
//       try {
//         let result = await axios.post("http://localhost:8000/menu/save", form.value);
//         let data = result.data;
//         if (data.code == 200) {
//           ElMessage.success("操作成功！");
//           formRef.value.resetFields();
//           emits("initMenuList");
//           handleClose();
//         } else {
//           ElMessage.error(data.msg || "操作失败");
//         }
//       } catch (error) {
//         console.error("请求失败：", error);
//         ElMessage.error("请求失败，请稍后再试");
//       }
//     } else {
//       console.log("fail");
//     }
//   });
// };
// 扁平化函数,Dialog组件中用于显示上级菜单的el-select组件绑定的数据是tableData，但tableData是一个树形结构（包含children属性），
// 而el-select默认不支持树形结构的选项。因此，上级菜单的内容无法正确显示要正确显示上级菜单的内容，需要将树形结构的tableData扁平化为一个扁平的选项列表。
// 可以通过递归函数将树形结构转换为扁平结构，然后绑定到el-select
const flattenOptions = (treeData) => {
  const result = [];
  const flatten = (data, prefix = "") => {
    data.forEach((item) => {
      result.push({
        label: prefix + item.name,
        value: item.id
      });
      if (item.children && item.children.length) {
        flatten(item.children, prefix + "  --");
      }
    });
  };
  flatten(treeData);
  return result;
};

const flatTableData = ref([]);

watch(
  () => props.tableData,
  () => {
    flatTableData.value = flattenOptions(props.tableData);
  },
  { immediate: true }
);
</script>
<template>
  <el-dialog
    :model-value="dialogVisible"
    :title="dialogTitle"
    width="30%"
    @close="handleClose"
  >
    <el-form
      ref="formRef"
      :model="form"
      :rules="rules"
      label-width="100px"
    >
      <el-form-item label="上级菜单" prop="parent_id">
        <el-select v-model="form.parent_id" placeholder="请选择上级菜单">
          <el-option
            v-for="item in flatTableData"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          ></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="菜单类型" prop="menu_type" label-width="100px">
        <el-radio-group v-model="form.menu_type">
          <el-radio :label="'M'">目录</el-radio>
          <el-radio :label="'C'">菜单</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="菜单图标" prop="icon">
        <el-input v-model="form.icon" />
      </el-form-item>
      <el-form-item label="菜单名称" prop="name">
        <el-input v-model="form.name" />
      </el-form-item>
      <el-form-item label="权限标识" prop="perms">
        <el-input v-model="form.perms" />
      </el-form-item>
      <el-form-item label="路径路由" prop="component">
        <el-input v-model="form.path" />
      </el-form-item>
      <el-form-item label="组件路径" prop="component">
        <el-input v-model="form.component" />
      </el-form-item>
      <el-form-item label="显示顺序" prop="order_num">
        <el-input-number
          v-model="form.order_num"
          :min="1"
          label="显示顺序"
        ></el-input-number>
      </el-form-item>
      <el-form-item label="备注" prop="remark">
        <el-input v-model="form.remark" />
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