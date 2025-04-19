<!-- QuestionCard.vue -->
<template>
  <el-card :body-style="{ padding: '10px' }">
    <div v-html="question.content"></div>

    <!-- 单选题 -->
    <template v-if="question.question_type === 'single_choice'">
      <el-radio-group v-model="selectedAnswer">
        <el-radio
          v-for="(option, index) in question.options"
          :key="index"
          :label="option"
        />
      </el-radio-group>
    </template>

    <!-- 多选题 -->
    <template v-else-if="question.question_type === 'multiple_choice'">
      <el-checkbox-group v-model="selectedAnswer">
        <el-checkbox
          v-for="(option, index) in question.options"
          :key="index"
          :label="option"
        />
      </el-checkbox-group>
    </template>

    <!-- 判断题 -->
    <template v-else-if="question.question_type === 'true_false'">
      <el-radio-group v-model="selectedAnswer">
        <el-radio label="true">正确</el-radio>
        <el-radio label="false">错误</el-radio>
      </el-radio-group>
    </template>

    <!-- 填空题 -->
    <template v-else-if="question.question_type === 'fill_blank'">
      <el-input
        v-model="selectedAnswer"
        type="textarea"
        :rows="3"
      />
    </template>

    <!-- 问答题 -->
    <template v-else-if="question.question_type === 'essay'">
      <el-input
        v-model="selectedAnswer"
        type="textarea"
        :rows="5"
      />
    </template>
  </el-card>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  question: { type: Object, required: true },
  modelValue: { default: '' }
})

const emit = defineEmits(['update:modelValue'])

const selectedAnswer = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value)
})
</script>