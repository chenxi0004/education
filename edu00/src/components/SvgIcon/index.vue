<!--<script setup>-->
<!--import {computed} from "vue";-->
<!--const props=defineProps({-->
<!--  icon:{-->
<!--    type:String,-->
<!--    required:true-->
<!--  }-->
<!--})-->
<!--const iconName=computed(()=>{-->
<!--  return `#icon-${props.icon}`-->
<!--})-->
<!--</script>-->

<!--<template>-->
<!--  <svg class="svg-icon" aria-hidden="true">-->
<!--    <use :xlink:href="iconName"></use>-->
<!--  </svg>-->
<!--</template>-->

<!--<style scoped lang="scss">-->
<!--  .svg-icon{-->
<!--    width: 1em;-->
<!--    height: 1em;-->
<!--    vertical-align: -0.15em;-->
<!--    fill: currentColor;-->
<!--    overflow: hidden;-->
<!--  }-->
<!--</style>-->

<!--<template>-->
<!--  <svg class="svg-icon" :class="className" aria-hidden="true">-->
<!--    <use :xlink:href="iconName"></use>-->
<!--  </svg>-->
<!--</template>-->

<!--<script>-->
<!--export default {-->
<!--  name: "SvgIcon",-->
<!--  props: {-->
<!--    name: {-->
<!--      type: String,-->
<!--      required: true,-->
<!--    },-->
<!--    className: {-->
<!--      type: String,-->
<!--      default: "",-->
<!--    },-->
<!--  },-->
<!--  computed: {-->
<!--    iconName() {-->
<!--      return `#${this.name}`;-->
<!--    },-->
<!--  },-->
<!--};-->
<!--</script>-->

<!--<style scoped>-->
<!--.svg-icon {-->
<!--  width: 1em;-->
<!--  height: 1em;-->
<!--  vertical-align: -0.15em;-->
<!--  fill: currentColor;-->
<!--  overflow: hidden;-->
<!--}-->
<!--</style>-->


<template>
  <svg :class="svgClass" aria-hidden="true">
    <use :xlink:href="iconName"></use>
  </svg>
</template>

<script>
export default {
  name: 'SvgIcon',
  props: {
    iconClass: {
      type: String,
      required: true
    },
    className: {
      type: String,
      default: ''
    }
  },
  computed: {
    iconName() {
      return `#icon-${this.iconClass}`;
    },
    svgClass() {
      return this.className ? `svg-icon ${this.className}` : 'svg-icon';
    }
  }
};
</script>

<style scoped>
.svg-icon {
  width: 1em;
  height: 1em;
  vertical-align: -0.15em;
  fill: currentColor;
  overflow: hidden;
}
</style>