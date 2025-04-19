import SvgIcon from '@/components/SvgIcon'

const svgrequired=require.context('./svg',false,/\.svg$/)
svgrequired.keys().forEach((item)=>svgrequired(item))

export default (app)=>{
    app.component('svg-icon',SvgIcon)
}
