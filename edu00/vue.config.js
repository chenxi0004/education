// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true
// })
// module.exports = {
//   devServer: {
//     port: 8080, // 设置为固定的端口号
//     open:true
//   }
// };
// const webpack=require('webpack');
//
// const path=require('path')
// function resolve(dir){
//   return path.join(__dirname,dir)
// }
//
// module.exports={
//   lintOnSave:false,
//   chainWebpack(config){
//     //设置svg-sprite-loader，config为webpack配置对象，config.module表示一个具名规则，用来修改规则
//     config.module
//       //规则
//         .rule('svg')
//       //忽略
//         .exclude.add(resolve('src/icons'))
//       //结束
//         .end()
//     config.module
//         .rule('icons')
//       //正则，解析.svg格式文件
//         .test(/\.svg$/)
//       //解析的文件
//         .include.add(resolve('src/icons'))
//         .end()
//       //新增解析的loader
//         .use('svg-sprite-loader')
//       //具体loader
//         .loader('svg-sprite-loader')
//       //loader的配置
//         .options({symbolId: 'icon-[name]'})
//       //结束
//         .end()
//     config
//         .plugin('ignore')
//         .use(new webpack.ContextReplacementPlugin(/moment[/\\]locale$/,/zh-cn$/))
//     config.module
//         .rule('icons')
//         .test(/\.svg$/)
//         .include.add(resolve('src/icons'))
//         .end()
//         .use('svg-sprite-loader')
//         .loader('svg-sprite-loader')
//         .options({symbolId: 'icon-[name]'})
//         .end()
//   }
// }

const path = require('path');
const { defineConfig } = require('@vue/cli-service');

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    port: 8080,
    open: true
  },
  lintOnSave: false,
  chainWebpack(config) {
    // 排除默认的 svg 处理规则
    config.module.rule('svg').exclude.add(resolve('src/icons')).end();

    // 添加 svg-sprite-loader 规则
    config.module
      .rule('icons')
      .test(/\.svg$/)
      .include.add(resolve('src/icons'))
      .end()
      .use('svg-sprite-loader')
      .loader('svg-sprite-loader')
      .options({ symbolId: 'icon-[name]' })
      .end();
  }
});

function resolve(dir) {
  return path.join(__dirname, dir);
}