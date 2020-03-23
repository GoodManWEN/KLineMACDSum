<template>
  <div>
    <div class="notification is-primary fllss">
      <b-button type="is-primary"
          inverted
          outlined
          :disabled="btndsb"
          :loading="false"
          @click="clicked"
          style="margin-left:40px">
          发送！
      </b-button>
    </div>
    <div class='fllss' style="margin-left:50px;margin-right:50px;width:50%;">
      <b-message 
      :title="result" 
      :type="ttype"
      :active.sync="isActive"
      aria-close-label="Close message"
      >
        <span v-if="show == 1">
        代码: {{stocknum_show}}
        <br>
        类型: {{typess[radio]}}
        <br>
        开始日期: {{stdate}}
        <br>
        截止日期: {{eddate}}
        <br>
        开始时间: {{sttime}}
        <br>
        截止时间: {{edtime}}
        <br>
        结果: 
        <span style="color:red"> 红: {{red}} </span>
        <span style="color:green"> 绿: {{green}} </span>   
        <span style="color:blue"> 总和: {{blue}} </span>  
        </span>
        <span v-if="show == 2">
          错误信息: <br>{{errmsg}}
        </span>
      </b-message>
    </div>
  </div>
</template>

<script>
import { log } from 'util'
export default {
  name: 'emits',
  data() {
    return {
      isActive:false,
      typess:{
        '5':"5分钟线",
        '15':"15分钟线",
        '30':"30分钟线",
        '60':"60分钟线",
        'd':"日线",
        'w':"周线",
        'm':"月线",
      },
      btndsb:true,
      red:"",
      greem:"",
      blue:"",
      ttype:undefined,
      result:"",
      show:0,
      errmsg:"",
      isLoading:false,
      stocknum_show:"",
    }
  },
  props:{
    stocknum:{
      type:String,
      default:''
    },
    radio:{
      type:String,
      default:'d'
    },
    sttime:{
      type:String,
      default:'09:30'
    },
    edtime:{
      type:String,
      default:'15:00'
    },
    stdate:{
      type:String,
      default:'2020-01-01'
    },
    eddate:{
      type:String,
      default:'2020-01-01'
    },
  },
  methods:{
    clicked(){
      // console.log(JSON)
      // JSON.stringify({})
      this.isLoading = true
      this.$emit('emitclicked',this.isLoading)
      this.axios({
        url:'/macdapi',
        method:"post",
        data:{
          stocknum:this.stocknum,
          radio:this.radio,
          sttime:this.sttime,
          edtime:this.edtime,
          stdate:this.stdate,
          eddate:this.eddate,
        }
      }).then(res => {
        this.isActive = true
        this.isLoading = false
        this.$emit('loadingchanged',this.isLoading)
        this.stocknum_show = this.stocknum
        if (res.data.success == 1) {
          this.ttype = 'is-success'
          this.result = "Success"
          this.show = 1
          this.red = res.data.data.red
          this.green = res.data.data.green
          this.blue = res.data.data.sum
        } else {
          this.ttype = 'is-danger'
          this.result = "Error"
          this.show = 2
          this.errmsg = res.data.msg
        }
      })
    }
  },
  watch:{
    stocknum(val){
      if (val.length == 6 && !isNaN(val)) {
        this.btndsb = false
      } else {
        this.btndsb = true
      }
    }
  }
}
</script>

<style scoped>
.fllss{
  float:left;
  width:100%;
  padding-right:50px;
  margin-bottom:50px;
}
</style>
