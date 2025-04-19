import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementPlus from 'element-plus'
import zhCn from "element-plus/es/locale/lang/zh-cn";
import 'element-plus/dist/index.css'
import '@/assets/styles/reset.css'
import '@/assets/styles/border.css'
import SvgIcon from '@/icons'
// createApp(App).use(store).use(router).use(ElementPlus,{locale:zhCn,}).mount('#app')
const app = createApp(App)
SvgIcon(app);
app.use(store)
app.use(router)
app.use(ElementPlus)
app.use(ElementPlus, {locale: zhCn,})
app.mount('#app')


// 通过 requestAnimationFrame 确保回调函数在浏览器重绘之前执行，从而减少性能问题
const _ResizeObserver = window.ResizeObserver;
window.ResizeObserver = class ResizeObserver extends _ResizeObserver {
  constructor(callback) {
    const optimizedCallback = (...args) => {
      requestAnimationFrame(() => {
        requestAnimationFrame(() => {
          callback(...args);
        });
      });
    };
    super(optimizedCallback);
  }
};



