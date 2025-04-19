//
// import axios from "axios";
// import qs from "qs";
// //创建axios实例
// let baseUrl="http://localhost:8000/";
// const httpService=axios.create({
//     baseURL:baseUrl,
//     timeout:3000
// });
// //添加请求和响应拦截器
// httpService.interceptors.request.use(function (config) {
//     config.headers.Authorization=window.sessionStorage.getItem('token');
//     return config
// },function (error){
//     return Promise.reject(error)
// });
// httpService.interceptors.response.use(function (response) {
//     return response
// },function (error) {
//     return Promise.reject(error)
// });
//
// //网络请求,get请求,url请求地址，params参数
// export function get(url,params={}){
//     return new Promise((resolve,reject)=>{
//         httpService({
//             url:url,
//             method:'get',
//             params:params
//         }).then(response=>{
//             resolve(response);
//         }).catch(error=>{
//             reject(error);
//         });
//     });
// }
// //post请求
// export function post(url,params={}){
// // export function post(url,data={}){
//     return new Promise((resolve,reject)=>{
//         httpService({
//             url:url,
//             method:'post',
//             // data: qs.stringify(data), // 使用 data 发送表单数据
//             params:params,
//             // params:qs.stringify(data),
//             // headers: {
//             //     // 'Content-Type': 'application/x-www-form-urlencoded',
//             //     'Content-Type': 'application/json'
//             // }
//         }).then(response=>{
//             console.log(response)
//             resolve(response);
//         }).catch(error=>{
//             console.log(error)
//             reject(error);
//         });
//     });
// }
//
//
//
// //delete
// export function del(url,params={}){
//     return new Promise((resolve,reject)=>{
//         httpService({
//             url:url,
//             method:'delete',
//             params:params
//         }).then(response=>{
//             console.log(response)
//             resolve(response);
//         }).catch(error=>{
//             console.log(error)
//             reject(error);
//         });
//     });
// }
// //文件上传
// export function fileUpload(url,params={}){
//     return new Promise((resolve,reject)=>{
//         httpService({
//             url:url,
//             method:'post',
//             data:params,
//             headers:{'Content-Type':'multipart/form-data'}
//         }).then(response=>{
//             resolve(response);
//         }).catch(error=>{
//             reject(error);
//         });
//     });
// }
//
// export function getServerUrl(){
//     return baseUrl;
// }
//
// export default {
//     get,
//     post,
//     del,
//     fileUpload,
//     getServerUrl
// }











import axios from "axios";
import qs from "qs";

// 创建axios实例
let baseUrl = "http://localhost:8000/";
const httpService = axios.create({
  baseURL: baseUrl,
  timeout: 3000,
});

// 添加请求拦截器
httpService.interceptors.request.use(
  (config) => {
    const token = window.sessionStorage.getItem("token");
    if (token) {
      config.headers["Authorization"] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// 添加响应拦截器
httpService.interceptors.response.use(
  (response) => {
    return response;
  },
  async (error) => {
    if (error.response.status === 401) {
      // 尝试使用refresh token刷新access token
      const refreshToken = window.sessionStorage.getItem("refresh");
      if (refreshToken) {
        try {
          const refreshResponse = await axios.post(
            `${baseUrl}user/token/refresh/`,
            { refresh: refreshToken },
            { headers: { "Content-Type": "application/json" } }
          );
          const newAccessToken = refreshResponse.data.access;
          window.sessionStorage.setItem("token", newAccessToken);

          // 更新请求头中的token并重新发送请求
          error.config.headers["Authorization"] = `Bearer ${newAccessToken}`;
          // return httpService(error.config);
        } catch (refreshError) {
          console.error("Refresh token failed:", refreshError);
          // 清除存储的token和refresh
          window.sessionStorage.removeItem("token");
          window.sessionStorage.removeItem("refresh");
          // 跳转到登录页面
          window.location.href = "/login";
        }
      }
    }
    return Promise.reject(error);
  }
);

// 网络请求封装
const request = (method, url, data = {}) => {
  return new Promise((resolve, reject) => {
    // httpService({
    //   url,
    //   method,
    //   data: method.toLowerCase() === "post" ? data : null,
    //   params: method.toLowerCase() !== "post" ? data : null,
    //   headers: {
    //     "Content-Type": method.toLowerCase() === "post" ? "application/json" : "application/x-www-form-urlencoded",
    //   },
    // })
    httpService({
      url,
      method,
      data: method.toLowerCase() === "post" || method.toLowerCase() === "put" ? data : null,
      // params: method.toLowerCase() !== "post" && method.toLowerCase() !== "put" ? data : null,
      params: method.toLowerCase() === "get" || method.toLowerCase() === "delete" ? data : null,
      headers: {
        "Content-Type": method.toLowerCase() === "post" || method.toLowerCase() === "put" ? "application/json" : "application/x-www-form-urlencoded",
      },
    })
      .then((response) => {
        resolve(response);
      })
      .catch((error) => {
        reject(error);
      });
  });
};

// GET 请求
export function get(url, params = {}) {
  return request("get", url, params);
}

// POST 请求
export function post(url, data = {}) {
  return request("post", url, data);
}
// PUT 请求（新增）
export function put(url, data = {}) {
  return request("put", url, data);
}
// DELETE 请求
export function del(url, params = {}) {
  return request("delete", url, params);
}

// 文件上传
export function fileUpload(url, data = {}) {
  return new Promise((resolve, reject) => {
    httpService({
      url,
      method: "post",
      data,
      headers: { "Content-Type": "multipart/form-data" },
    })
      .then((response) => {
        resolve(response);
      })
      .catch((error) => {
        reject(error);
      });
  });
}

export function getServerUrl() {
  return baseUrl;
}

export default {
  get,
  post,
  put, // 新增 put 方法
  del,
  fileUpload,
  getServerUrl,
};