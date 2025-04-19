<!--<template>-->
<!--  <div>-->
<!--    <div v-for="comment in comments" :key="comment.comment_id" class="comment-item">-->
<!--      <div class="comment-header">-->
<!--        <p><strong>{{ comment.user_id }}</strong> ({{ comment.user_role }}): {{ comment.content }}</p>-->
<!--        <p>时间: {{ comment.created_time }}</p>-->
<!--        &lt;!&ndash; 回复按钮 &ndash;&gt;-->
<!--        <el-button v-if="!comment.replying" @click="replyComment(comment)">回复</el-button>-->
<!--        &lt;!&ndash; 回复输入框 &ndash;&gt;-->
<!--        <div v-else>-->
<!--          <el-input-->
<!--            type="textarea"-->
<!--            v-model="comment.replyContent"-->
<!--            placeholder="请输入回复内容"-->
<!--          ></el-input>-->
<!--          <el-button type="primary" @click="submitReply(comment)">提交回复</el-button>-->
<!--          <el-button @click="cancelReply(comment)">取消</el-button>-->
<!--        </div>-->
<!--      </div>-->
<!--      &lt;!&ndash; 递归渲染子评论 &ndash;&gt;-->
<!--      <div v-if="comment.replies && comment.replies.length > 0" class="replies">-->
<!--        <comment-tree :comments="comment.replies" @reply-comment="$emit('reply-comment', $event)" @submit-reply="$emit('submit-reply', $event)" @cancel-reply="$emit('cancel-reply', $event)"></comment-tree>-->
<!--      </div>-->
<!--    </div>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--export default {-->
<!--  name: 'CommentTree',-->
<!--  props: {-->
<!--    comments: Array-->
<!--  },-->
<!--  methods: {-->
<!--    replyComment(comment) {-->
<!--      this.$emit('reply-comment', comment);-->
<!--    },-->
<!--    submitReply(comment) {-->
<!--      this.$emit('submit-reply', comment);-->
<!--    },-->
<!--    cancelReply(comment) {-->
<!--      this.$emit('cancel-reply', comment);-->
<!--    }-->
<!--  }-->
<!--};-->
<!--</script>-->

<!--<style scoped>-->
<!--.comment-item {-->
<!--  margin-bottom: 10px;-->
<!--  border-bottom: 1px solid #ccc;-->
<!--  padding-bottom: 10px;-->
<!--}-->

<!--.replies {-->
<!--  margin-left: 20px; /* 缩进 */-->
<!--  margin-top: 5px;-->
<!--  border-left: 2px solid #ccc; /* 添加边框以增强视觉效果 */-->
<!--  padding-left: 10px;-->
<!--}-->
<!--</style>-->






<!--<template>-->
<!--  <div>-->
<!--    <div v-for="comment in comments" :key="comment.comment_id" class="comment-item">-->
<!--      <div class="comment-header">-->
<!--        <p><strong>{{ comment.user_id }}</strong> ({{ comment.user_role }}): {{ comment.content }}</p>-->
<!--        <p>时间: {{ comment.created_time }}</p>-->
<!--        &lt;!&ndash; 回复按钮 &ndash;&gt;-->
<!--        <el-button v-if="!comment.replying" class="reply-btn" @click="replyComment(comment)">回复</el-button>-->
<!--        &lt;!&ndash; 回复输入框 &ndash;&gt;-->
<!--        <div v-else class="reply-input">-->
<!--          <el-input-->
<!--            type="textarea"-->
<!--            v-model="comment.replyContent"-->
<!--            placeholder="请输入回复内容"-->
<!--            class="reply-textarea"-->
<!--          ></el-input>-->
<!--          <div class="reply-actions">-->
<!--            <el-button type="primary" class="submit-reply-btn" @click="submitReply(comment)">提交回复</el-button>-->
<!--            <el-button class="cancel-reply-btn" @click="cancelReply(comment)">取消</el-button>-->
<!--          </div>-->
<!--        </div>-->
<!--        &lt;!&ndash; 折叠/展开按钮 &ndash;&gt;-->
<!--        <el-button v-if="comment.level >= 2&& comment.replies && comment.replies.length > 0" class="toggle-btn" @click="toggleExpand(comment)">-->
<!--          {{ comment.expanded ? '折叠' : '展开' }}-->
<!--        </el-button>-->
<!--      </div>-->
<!--      &lt;!&ndash; 递归渲染子评论 &ndash;&gt;-->
<!--      <div v-if="comment.replies && comment.replies.length > 0 && comment.expanded" class="replies">-->
<!--        <comment-tree :comments="comment.replies" @reply-comment="$emit('reply-comment', $event)" @submit-reply="$emit('submit-reply', $event)" @cancel-reply="$emit('cancel-reply', $event)" @toggle-expand="$emit('toggle-expand', $event)"></comment-tree>-->
<!--      </div>-->
<!--    </div>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--export default {-->
<!--  name: 'CommentTree',-->
<!--  props: {-->
<!--    comments: Array-->
<!--  },-->
<!--  methods: {-->
<!--    replyComment(comment) {-->
<!--      this.$emit('reply-comment', comment);-->
<!--    },-->
<!--    submitReply(comment) {-->
<!--      this.$emit('submit-reply', comment);-->
<!--    },-->
<!--    cancelReply(comment) {-->
<!--      this.$emit('cancel-reply', comment);-->
<!--    },-->
<!--    toggleExpand(comment) {-->
<!--      this.$emit('toggle-expand', comment);-->
<!--    }-->
<!--  }-->
<!--};-->
<!--</script>-->

<!--<style scoped>-->
<!--.comment-item {-->
<!--  margin-bottom: 10px;-->
<!--  border-bottom: 1px solid #f0f0f0;-->
<!--  padding-bottom: 10px;-->
<!--}-->

<!--.replies {-->
<!--  margin-left: 20px; /* 缩进 */-->
<!--  margin-top: 5px;-->
<!--  border-left: 2px solid #f0f0f0; /* 添加边框以增强视觉效果 */-->
<!--  padding-left: 10px;-->
<!--}-->

<!--.reply-btn {-->
<!--  background: linear-gradient(135deg, #67c23a, #409eff);-->
<!--  color: white;-->
<!--  border: none;-->
<!--  border-radius: 4px;-->
<!--  padding: 5px 10px;-->
<!--  font-size: 12px;-->
<!--  cursor: pointer;-->
<!--  transition: background 0.3s ease;-->
<!--}-->

<!--.reply-btn:hover {-->
<!--  background: linear-gradient(135deg, #85ce61, #66b1ff);-->
<!--}-->

<!--.reply-btn:active {-->
<!--  background: linear-gradient(135deg, #5daf34, #3a8ee6);-->
<!--}-->

<!--.reply-input {-->
<!--  display: flex;-->
<!--  flex-direction: column;-->
<!--}-->

<!--.reply-textarea {-->
<!--  margin-bottom: 10px;-->
<!--  padding: 10px;-->
<!--  border: 2px solid #dcdfe6;-->
<!--  border-radius: 4px;-->
<!--  font-size: 14px;-->
<!--  color: #333;-->
<!--  background-color: #fff;-->
<!--  transition: border-color 0.3s ease;-->
<!--}-->

<!--.reply-textarea:focus {-->
<!--  border-color: #409eff;-->
<!--  outline: none;-->
<!--}-->

<!--.reply-actions {-->
<!--  display: flex;-->
<!--  justify-content: flex-end;-->
<!--}-->

<!--.submit-reply-btn, .cancel-reply-btn {-->
<!--  background: linear-gradient(135deg, #67c23a, #409eff);-->
<!--  color: white;-->
<!--  border: none;-->
<!--  border-radius: 4px;-->
<!--  padding: 5px 10px;-->
<!--  font-size: 12px;-->
<!--  cursor: pointer;-->
<!--  transition: background 0.3s ease;-->
<!--}-->

<!--.submit-reply-btn:hover, .cancel-reply-btn:hover {-->
<!--  background: linear-gradient(135deg, #85ce61, #66b1ff);-->
<!--}-->

<!--.submit-reply-btn:active, .cancel-reply-btn:active {-->
<!--  background: linear-gradient(135deg, #5daf34, #3a8ee6);-->
<!--}-->

<!--.cancel-reply-btn {-->
<!--  background: linear-gradient(135deg, #f56c6c, #ff7875);-->
<!--  margin-left: 10px;-->
<!--}-->

<!--.cancel-reply-btn:hover {-->
<!--  background: linear-gradient(135deg, #dd6161, #ff9b9d);-->
<!--}-->

<!--.cancel-reply-btn:active {-->
<!--  background: linear-gradient(135deg, #c85050, #ff6363);-->
<!--}-->

<!--.toggle-btn {-->
<!--  background: linear-gradient(135deg, #f0ad4e, #d39e00);-->
<!--  color: white;-->
<!--  border: none;-->
<!--  border-radius: 4px;-->
<!--  padding: 5px 10px;-->
<!--  font-size: 12px;-->
<!--  cursor: pointer;-->
<!--  transition: background 0.3s ease;-->
<!--}-->

<!--.toggle-btn:hover {-->
<!--  background: linear-gradient(135deg, #e0a839, #c18e00);-->
<!--}-->

<!--.toggle-btn:active {-->
<!--  background: linear-gradient(135deg, #b87f00, #a16a00);-->
<!--}-->
<!--</style>-->








<template>
  <div>
    <el-timeline>
      <el-timeline-item v-for="comment in comments" :key="comment.comment_id" :timestamp="comment.created_time" placement="top">
        <el-card class="comment-card">
          <div class="comment-header">
            <el-avatar :src="getUserAvatar(comment.user_id)" class="user-avatar" alt="用户头像" />
            <div class="user-info">
              <strong>{{ comment.user_id }}</strong>
              <span class="user-role">({{ comment.user_role }})</span>
              <p v-if="comment.reply_to">
                回复 <strong>{{ comment.reply_to }}</strong>:
              </p>
              <p v-else>
                在话题 <strong>{{ comment.topic }}</strong> 下评论:
              </p>
            </div>
          </div>
          <div class="comment-content">
            <p>{{ comment.content }}</p>
          </div>
          <div class="comment-actions">
            <el-button v-if="!comment.replying" class="reply-btn" @click="replyComment(comment)">回复</el-button>
            <div v-else class="reply-input">
              <el-input
                type="textarea"
                v-model="comment.replyContent"
                placeholder="请输入回复内容"
                class="reply-textarea"
              ></el-input>
              <div class="reply-actions">
                <el-button type="primary" class="submit-reply-btn" @click="submitReply(comment)">提交回复</el-button>
                <el-button class="cancel-reply-btn" @click="cancelReply(comment)">取消</el-button>
              </div>
            </div>
            <el-button v-if="comment.level >= 2 && comment.replies && comment.replies.length > 0" class="toggle-btn" @click="toggleExpand(comment)">
              {{ comment.expanded ? '折叠' : '展开' }}
            </el-button>
          </div>
        </el-card>
        <div v-if="comment.replies && comment.replies.length > 0 && comment.expanded" class="replies">
          <comment-tree :comments="comment.replies" @reply-comment="$emit('reply-comment', $event)" @submit-reply="$emit('submit-reply', $event)" @cancel-reply="$emit('cancel-reply', $event)" @toggle-expand="$emit('toggle-expand', $event)"></comment-tree>
        </div>
      </el-timeline-item>
    </el-timeline>
  </div>
</template>

<script>
import { getServerUrl } from "@/util/request";

export default {
  name: 'CommentTree',
  props: {
    comments: Array
  },
  methods: {
    replyComment(comment) {
      this.$emit('reply-comment', comment);
    },
    submitReply(comment) {
      this.$emit('submit-reply', comment);
    },
    cancelReply(comment) {
      this.$emit('cancel-reply', comment);
    },
    toggleExpand(comment) {
      this.$emit('toggle-expand', comment);
    },
    getUserAvatar(userId, defaultAvatar = 'default.png') {
      const user = this.$store.state.user;
      const serverUrl = getServerUrl();
      const squareUrl = `${serverUrl}media/userAvatar/${user.avatar || "default.jpg"}`;
      defaultAvatar = `./src/assets/styles/${defaultAvatar}`;
      if (user && user.avatar) {
        return squareUrl; // 返回用户头像
      } else {
        return defaultAvatar; // 返回默认头像
      }
    },
  }
};
</script>

<style scoped>
.comment-card {
  margin-bottom: 10px;
}

.comment-header {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.user-avatar {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  margin-right: 10px;
  vertical-align: middle;
}

.user-info {
  flex: 1;
}

.user-role {
  font-size: 12px;
  color: #666;
}

.comment-content {
  margin-bottom: 10px;
}

.comment-actions {
  display: flex;
  justify-content: space-between;
}

.reply-btn, .toggle-btn {
  background: linear-gradient(135deg, #67c23a, #409eff);
  color: white;
  border: none;
  border-radius: 4px;
  padding: 5px 10px;
  font-size: 12px;
  cursor: pointer;
  transition: background 0.3s ease;
}

.reply-btn:hover, .toggle-btn:hover {
  background: linear-gradient(135deg, #85ce61, #66b1ff);
}

.reply-btn:active, .toggle-btn:active {
  background: linear-gradient(135deg, #5daf34, #3a8ee6);
}

.reply-input {
  display: flex;
  flex-direction: column;
}

.reply-textarea {
  margin-bottom: 10px;
  padding: 10px;
  border: 2px solid #dcdfe6;
  border-radius: 4px;
  font-size: 14px;
  color: #333;
  background-color: #fff;
  transition: border-color 0.3s ease;
}

.reply-textarea:focus {
  border-color: #409eff;
  outline: none;
}

.reply-actions {
  display: flex;
  justify-content: flex-end;
}

.submit-reply-btn, .cancel-reply-btn {
  background: linear-gradient(135deg, #67c23a, #409eff);
  color: white;
  border: none;
  border-radius: 4px;
  padding: 5px 10px;
  font-size: 12px;
  cursor: pointer;
  transition: background 0.3s ease;
}

.submit-reply-btn:hover, .cancel-reply-btn:hover {
  background: linear-gradient(135deg, #85ce61, #66b1ff);
}

.submit-reply-btn:active, .cancel-reply-btn:active {
  background: linear-gradient(135deg, #5daf34, #3a8ee6);
}

.cancel-reply-btn {
  background: linear-gradient(135deg, #f56c6c, #ff7875);
  margin-left: 10px;
}

.cancel-reply-btn:hover {
  background: linear-gradient(135deg, #dd6161, #ff9b9d);
}

.cancel-reply-btn:active {
  background: linear-gradient(135deg, #c85050, #ff6363);
}
</style>