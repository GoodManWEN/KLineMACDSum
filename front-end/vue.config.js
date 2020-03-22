module.exports = {
  devServer:{
    host:"localhost",
    port:8080,
    https:false,
    open:false,
    proxy:{
      "/macdapi":{
        target:"http://127.0.0.1:8081/macdapi",
        changeOrigin:true,
        pathRewrite:{
          '^/macdapi':''
        }
      }
    }   
  }
}