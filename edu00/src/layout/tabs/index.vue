<!--<template>-->
<!--  <div style="margin-bottom: 20px">-->
<!--    <el-button size="small" @click="addTab(editableTabsValue)">-->
<!--      add tab-->
<!--    </el-button>-->
<!--  </div>-->
<!--  <el-tabs-->
<!--    v-model="editableTabsValue"-->
<!--    type="card"-->
<!--    class="demo-tabs"-->
<!--    closable-->
<!--    @tab-remove="removeTab"-->
<!--  >-->
<!--    <el-tab-pane-->
<!--      v-for="item in editableTabs"-->
<!--      :key="item.name"-->
<!--      :label="item.title"-->
<!--      :name="item.name"-->
<!--    >-->
<!--      {{ item.content }}-->
<!--    </el-tab-pane>-->
<!--  </el-tabs>-->
<!--</template>-->

<!--<script lang="js" setup>-->
<!--import { ref } from 'vue'-->

<!--let tabIndex = 2-->
<!--const editableTabsValue = ref('2')-->
<!--const editableTabs = ref([-->
<!--  {-->
<!--    title: 'Tab 1',-->
<!--    name: '1',-->
<!--    content: 'Tab 1 content',-->
<!--  },-->
<!--  {-->
<!--    title: 'Tab 2',-->
<!--    name: '2',-->
<!--    content: 'Tab 2 content',-->
<!--  },-->
<!--])-->

<!--const addTab = (targetName) => {-->
<!--  const newTabName = `${++tabIndex}`-->
<!--  editableTabs.value.push({-->
<!--    title: 'New Tab',-->
<!--    name: newTabName,-->
<!--    content: 'New Tab content',-->
<!--  })-->
<!--  editableTabsValue.value = newTabName-->
<!--}-->
<!--const removeTab = (targetName) => {-->
<!--  const tabs = editableTabs.value-->
<!--  let activeName = editableTabsValue.value-->
<!--  if (activeName === targetName) {-->
<!--    tabs.forEach((tab, index) => {-->
<!--      if (tab.name === targetName) {-->
<!--        const nextTab = tabs[index + 1] || tabs[index - 1]-->
<!--        if (nextTab) {-->
<!--          activeName = nextTab.name-->
<!--        }-->
<!--      }-->
<!--    })-->
<!--  }-->

<!--  editableTabsValue.value = activeName-->
<!--  editableTabs.value = tabs.filter((tab) => tab.name !== targetName)-->
<!--}-->
<!--</script>-->

<!--<style>-->
<!--.demo-tabs > .el-tabs__content {-->
<!--  padding: 32px;-->
<!--  color: #6b778c;-->
<!--  font-size: 32px;-->
<!--  font-weight: 600;-->
<!--}-->
<!--</style>-->


<template>
  <el-tabs
    v-model="editableTabsValue"
    type="card"
    class="demo-tabs"
    closable
    @tab-remove="removeTab"
    @tab-click="clickTab"
  >
    <el-tab-pane
      v-for="item in editableTabs"
      :key="item.name"
      :label="item.title"
      :name="item.name"
    >
    </el-tab-pane>
  </el-tabs>
</template>

<script lang="js" setup>
import { ref,watch } from 'vue'
import store from "@/store";

import { useRouter } from 'vue-router';
const router = useRouter();
const editableTabsValue = ref(store.state.editableTabsValue)
const editableTabs = ref(store.state.editableTabs)

// const addTab = (targetName) => {
//   const newTabName = `${++tabIndex}`
//   editableTabs.value.push({
//     title: 'New Tab',
//     name: newTabName,
//     content: 'New Tab content',
//   })
//   editableTabsValue.value = newTabName
// }
const removeTab = (targetName) => {
  const tabs = editableTabs.value
  let activeName = editableTabsValue.value
  if (activeName === targetName) {
    tabs.forEach((tab, index) => {
      if (tab.name === targetName) {
        const nextTab = tabs[index + 1] || tabs[index - 1]
        if (nextTab) {
          activeName = nextTab.name
        }
      }
    })
  }

  editableTabsValue.value = activeName
  editableTabs.value = tabs.filter((tab) => tab.name !== targetName)
  store.state.editableTabsValue=editableTabsValue.value
  store.state.editableTabs=editableTabs.value
  router.push({path:activeName})
}

const clickTab=(target)=>{
  router.push({name:target.props.label})
}

const refreshTabs=()=>{
  editableTabs.value=store.state.editableTabs
  editableTabsValue.value=store.state.editableTabsValue
}
watch(store.state,()=>{
  refreshTabs()
} , {
    deep:true,
    immediate:true
  })

//个人中心页面顶部填充
</script>

<style>
.demo-tabs > .el-tabs__content {
  padding: 32px;
  color: #6b778c;
  font-size: 32px;
  font-weight: 600;
}
.el-tabs--card>.el-tabs__header.el-tabs__item.is-avtive{
  background-color: lightgray;
}
.el-main{
  padding: 0px;
}


.el-tabs__content{
  padding: 0px !important;;


}

</style>
