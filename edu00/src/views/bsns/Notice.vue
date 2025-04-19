<template>
  <div class="notification-container">
    <h1 class="notification-title">🔔 通知中心</h1>
    <ul class="notification-list">
      <li
        v-for="notification in notifications"
        :key="notification.notification_id"
        class="notification-item"
        :class="{ 'read': notification.is_read }"
      >
        <div class="notification-content">
          <p class="message">{{ notification.message }}</p>
          <div class="timestamp">{{ formatDate(notification.created_at) }}</div>
        </div>
        <button
          class="mark-read-btn"
          @click="markAsRead(notification.notification_id)"
          :disabled="notification.is_read"
        >
          {{ notification.is_read ? '已读' : '标记为已读' }}
        </button>
      </li>
    </ul>
  </div>
</template>

<script>
// 原有script部分保持不变，添加日期格式化方法
import {onMounted, ref} from "vue";
import {useStore} from "vuex";
import axios from "axios";

export default {
  props: ['studentId'],
  setup(props) {
    const notifications = ref([]);
    const store = useStore();
    const user= store.state.user;
    const studentId = user.student_or_teacher_id;

    const fetchNotifications = async () => {
      const response = await axios.get(`http://localhost:8002/interact/notifications/`, {
        params: { student_id: studentId }
      });
      notifications.value = response.data;
    };

    const markAsRead = async (notificationId) => {
      await axios.patch(`http://localhost:8002/interact/notifications/${notificationId}/`, {
        is_read: true
      });
      fetchNotifications();
    };

    onMounted(fetchNotifications);

    return {
      notifications,
      markAsRead,
    };
  },
  methods: {
    formatDate(dateString) {
      const date = new Date(dateString);
      return date.toLocaleDateString('zh-CN', {
        hour: '2-digit',
        minute: '2-digit',
        hour12: true
      });
    }
  }
}
</script>

<style scoped>
.notification-container {
  max-width: 800px;
  margin: 2rem auto;
  padding: 0 1rem;
}

.notification-title {
  color: #2c3e50;
  text-align: center;
  margin-bottom: 2rem;
  font-size: 2.5rem;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
}

.notification-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.notification-item {
  background: white;
  border-radius: 15px;
  padding: 1.5rem;
  margin-bottom: 1rem;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  transition: transform 0.2s ease;
  position: relative;
}

.notification-item:hover {
  transform: translateX(10px);
}

.notification-item.read {
  background: #f8f9fa;
  opacity: 0.9;
}

.notification-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.message {
  color: #2c3e50;
  font-size: 1.1rem;
  line-height: 1.6;
  margin: 0;
  flex-grow: 1;
}

.timestamp {
  color: #666;
  font-size: 0.9rem;
  white-space: nowrap;
}

.mark-read-btn {
  background: #42b983;
  color: white;
  border: none;
  padding: 0.6rem 1.5rem;
  border-radius: 25px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.mark-read-btn:hover:not(:disabled) {
  background: #33a06f;
  transform: scale(1.05);
}

.mark-read-btn:disabled {
  background: #cccccc;
  cursor: not-allowed;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .notification-container {
    margin: 1rem;
    padding: 0;
  }

  .notification-title {
    font-size: 2rem;
  }

  .notification-item {
    padding: 1rem;
    margin-bottom: 0.8rem;
  }

  .message {
    font-size: 1rem;
  }

  .mark-read-btn {
    padding: 0.5rem 1rem;
    font-size: 0.9rem;
  }
}
</style>