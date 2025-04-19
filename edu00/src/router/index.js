// import { createRouter, createWebHashHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'
//
// const routes = [
//   {
//     path: '/',
//     name: '主页',
//     // component: HomeView
//     component: () => import( '../layout/index.vue'),
//     redirect:'/index',
//     children:[{
//       path:'/index',
//       name:'首页',
//       component:()=>import('../views/index/index.vue')
//     },{
//     path: '/sys/user',
//     name: '用户管理',
//     component: () => import( '../views/sys/user/index.vue')
//   },
//   {
//     path: '/sys/role',
//     name: '角色管理',
//     component: () => import( '../views/sys/role/index.vue')
//   },
//   {
//     path: '/sys/menu',
//     name: '菜单管理',
//     component: () => import( '../views/sys/menu/index.vue')
//   },
//   {
//     path: '/bsns/course',
//     name: '课程管理',
//     component: () => import( '../views/bsns/Course.vue')
//   },
//         {
//     path: '/bsns/interact',
//     name: '互动管理',
//     component: () => import( '../views/bsns/Interact.vue')
//   },
//     {
//     path: '/uerCenter',
//     name: '个人中心',
//     component: () => import( '../views/userCenter/index.vue')
//   },
//     ]
//   },
//   // {
//   //   path: '/about',
//   //   name: 'about',
//   //   // route level code-splitting
//   //   // this generates a separate chunk (about.[hash].js) for this route
//   //   // which is lazy-loaded when the route is visited.
//   //   component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
//   // }
//   {
//     path: '/login',
//     name: 'login',
//     component: () => import( '../views/Login.vue')
//   },
//     {
//     path: '/register',
//     name: 'register',
//     component: () => import( '../views/register.vue')
//   },
//   {
//     path: '/activate/:uid/:token',
//     name: 'ActivateAccount',
//     component: () => import('../views/ActivateAccount.vue')
//   }
//
// ]
//
// const router = createRouter({
//   history: createWebHashHistory(),
//   routes
// })
//
// router.beforeEach((to, from, next) => {
//   const token = window.sessionStorage.getItem('token');
//   const isLoginPage = to.path === '/login';
//   const isRegisterPage = to.path === '/register';
//   // const isActivatePage=to.name === 'ActivateAccount'
//   // const isActivatePage = to.fullPath.match(/^\/user\/activate\/[^/]+\/[^/]+/);// 匹配动态激活页面路径
//   // 定义不需要登录即可访问的页面
//   const isPublicPage=isLoginPage || isRegisterPage
//     if (!token && !isPublicPage) {
//     // 如果用户未登录且访问的不是公开页面，重定向到登录页面
//     next('/login');
//   } else {
//     // 如果用户已登录，或者访问的是公开页面，正常跳转
//     next();
//   }
//   // }
//
// });
//
// export default router






import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
    {
    path: '/login',
    name: 'login',
    component: () => import( '../views/Login.vue')
  },
    {
    path: '/register',
    name: 'register',
    component: () => import( '../views/register.vue')
  },
  {
    // path: '/user/activate/:uid/:token',
    path: '/activate/:uid/:token',
    name: 'ActivateAccount',
    component: () => import('../views/ActivateAccount.vue')
  },
  {
    path: '/',
    name: '主页',
    // component: HomeView
    component: () => import( '../layout/index.vue'),
    // redirect:'/index',
    children:[{
      path:'/index',
      name:'首页',
      component:()=>import('../views/index/index.vue')
    },{
    path: '/sys/user',
    name: '用户管理',
    component: () => import( '../views/sys/user/index.vue')
  },
  {
    path: '/sys/role',
    name: '角色管理',
    component: () => import( '../views/sys/role/index.vue')
  },
  {
    path: '/sys/menu',
    name: '菜单管理',
    component: () => import( '../views/sys/menu/index.vue')
  },
   {
    path: '/sys/student',
    name: '学生信息管理',
    component: () => import( '../views/sys/student/index.vue')
  },
    {
    path: '/sys/teacher',
    name: '教师信息管理',
    component: () => import( '../views/sys/teacher/index.vue')
  },
  {
    path: '/bsns/course',
    name: '课程管理',
    component: () => import( '../views/bsns/Course.vue')
  },
        {
    path: '/bsns/interact',
    name: '互动管理',
    component: () => import( '../views/bsns/Interact.vue')
  },
    {
    path: '/uerCenter',
    name: '个人中心',
    component: () => import( '../views/userCenter/index.vue')
  },
    {
      path: '/bsns/enroll/',
      name: '选课',
      component: ()=>import('../views/bsns/Enrollment.vue')
    },
    {
      path: '/bsns/progress/',
      name: '学习进度',
      component: ()=>import('../views/bsns/LearningProgress.vue')
    },
    {
      path: '/bsns/record/:courseId',
      name: '学习记录',
      component: ()=>import('../views/bsns/LearningRecord.vue')
    },
    {
      path: '/bsns/report',
      name: '报告',
      component: ()=>import('../views/bsns/Report.vue')
    },
        {
      path: '/bsns/material',
      name: '课程资料',
      component: ()=>import('../views/bsns/Material.vue')
    },
      {
      path: '/bsns/upload',
      name: '上传课程视频',
      component: ()=>import('../views/bsns/UploadVideo.vue')
    },
        {
      path: '/bsns/review',
      name: '审核课程资料',
      component: ()=>import('../views/bsns/Review.vue')
    },
        {
      path: '/bsns/videoreview',
      name: '审核课程视频',
      component: ()=>import('../views/bsns/VideoReview.vue')
    },
      {
      path: '/bsns/study',
      name: '课程学习',
      component: ()=>import('../views/bsns/Study.vue')
    },
        {
      path: '/bsns/coursedetail',
      name: '课程详情',
      component: ()=>import('../views/bsns/Detail.vue')
    }

    ]
  },

]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})
// const router = new VueRouter({
//   mode: 'history', // 使用 history 模式
//   routes: []
// });



router.beforeEach((to, from, next) => {
  const token = window.sessionStorage.getItem('token');
  const isLoginPage = to.path === '/login';
  const isRegisterPage = to.path === '/register';
  const isVideoLink = to.path.startsWith('/media/'); // 排除 /media/ 开头的路径
  const isActivatePage=to.name === 'ActivateAccount'
  // const isActivatePage = to.fullPath.match(/^\/user\/activate\/[^/]+\/[^/]+/);// 匹配动态激活页面路径
  // 定义不需要登录即可访问的页面
  const isPublicPages = isLoginPage || isRegisterPage || !(isActivatePage);
  const isPublicPage=isLoginPage || isRegisterPage
  // const isPublicPage = isLoginPage || isRegisterPage || isVideoLink;

    if (!token && !isPublicPage)
    {
    // 如果用户未登录且访问的不是公开页面，重定向到登录页面
    next('/login');
    // console.log('Redirecting to login:', isActivatePage);
  } else {
    // 如果用户已登录，或者访问的是公开页面，正常跳转
    next();
  }
  // }

});

export default router
