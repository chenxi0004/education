// import { createStore } from 'vuex'
//
// export default createStore({
//   state: {
//     editableTabsValue:'/index',
//     editableTabs:[
//       {
//         title:'首页',
//         name:'/index'
//       }
//     ]
//   },
//   getters: {
//   },
//   mutations: {
//     ADD_TABS:(state,tab)=>{
//       if(state.editableTabs.findIndex(e=>e.name===tab.path)===-1){
//         state.editableTabs.push({
//           title: tab.name,
//           name: tab.path
//             }
//         )
//       }
//       state.editableTabsValue=tab.path
//     },
//     RESET_TAB:(state)=>{
//       state.editableTabsValue='/index'
//       state.editableTabs=[
//         {
//           title: '首页',
//           name: '/index'
//         }
//       ]
//     }
//   },
//   actions: {
//   },
//   modules: {
//   }
// })



import { createStore } from 'vuex';

export default createStore({
  state: {
    editableTabsValue: '/index',
    editableTabs: [
      {
        title: '首页',
        name: '/index',
      },
    ],
    user: null, // 用户信息字段
    role:null,
  },
  getters: {
  },
  // getters: {
  //   // 添加一个 getter 来获取当前用户信息
  //   getCurrentUser: (state) => {
  //     return state.user;
  //   },
  // },
  mutations: {
    ADD_TABS(state, tab) {
      if (state.editableTabs.findIndex(e => e.name === tab.path) === -1) {
        state.editableTabs.push({
          title: tab.name,
          name: tab.path,
        });
      }
      state.editableTabsValue = tab.path;
    },
    RESET_TAB(state) {
      state.editableTabsValue = '/index';
      state.editableTabs = [
        {
          title: '首页',
          name: '/index',
        },
      ];
    },
    SET_USER(state, user) {
      state.user = user; // 将用户信息保存到 Vuex 状态中
    },
    CLEAR_USER(state) {
      state.user = null; // 清除 Vuex 中的用户信息
    },
    CLEAR_ROLE(state){
      state.role=null;
    },
    SET_ROLE(state,role){
      state.role=role;
    },

  },
  actions: {
    setUser({ commit }, user) {
      commit('SET_USER', user);
    },
    setRole({commit},role){
      commit('SET_ROLE',role)
    },
    clearUser({ commit }) {
      commit('CLEAR_USER');
      // localStorage.removeItem('token'); // 清除本地存储中的 Token
      // localStorage.removeItem('refresh'); // 清除本地存储中的刷新 Token
      // sessionStorage.removeItem('token'); // 清除会话存储中的 Token
      // sessionStorage.removeItem('refresh'); // 清除会话存储中的刷新 Token
      // sessionStorage.removeItem('currentUser'); // 清除会话存储中的用户信息
      // sessionStorage.removeItem('menuList'); // 清除会话存储中的菜单列表
    },
    clearRole({commit}){
      commit('CLEAR_ROLE');
    },
  },
  modules: {
  },
});
