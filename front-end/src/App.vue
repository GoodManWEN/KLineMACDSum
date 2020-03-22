<template>
  <div id="app">
    <div class='div1-ttls' style="margin-top:10px;">
      <h1> 计算MACD </h1>
      <radios @radiochanged="childchanged($event)" />
    </div>
    <div class="div1-ttls" style="margin-right:50px">
      <b-field label="股票代码" 
               :type="inputtype"
               :message="inputmsg"
               >
        <b-input  placeholder="600000"
                  @blur="inputblured"
                  v-model="stocknum"
        ></b-input>
      </b-field>
    </div>
    <div class='div1-ttls'>
      <dates 
      @stdatechanged="stdatec"
      @eddatechanged="eddatec"
      @isequalchanged="eqc"
      :radio="cradio"/>
    </div>
    <div class='div1-ttls'>
      <timel 
      @sttimechanged="sttimec"
      @edtimechanged="edtimec"
      :samedate="samedate"
      :radio="cradio"
      />
    </div>
    <div class='div1-ttls' style="margin-left:0;margin-right:0">
      <emits
      :stocknum="stocknum"
      :radio="cradio"
      :sttime="sttime"
      :edtime="edtime"
      :stdate="stdate"
      :eddate="eddate"
      />
    </div>
    
  </div>
</template>

<script>
import radios from './components/radios'
import timel from './components/timel'
import dates from './components/dates'
import emits from './components/emits'

export default {
  name: 'App',
  components: {
    radios,
    timel,
    dates,
    emits
  },
  data(){
    return {
      stocknum:"",
      inputtype:"false",
      inputmsg:"",
      cradio:'d',
      samedate:true,
      sttime:"09:30",
      edtime:"15:00",
      stdate:"2020-01-01",
      eddate:"2020-01-01"
    }
  },
  methods:{
    childchanged(data){
      this.cradio = data
    },
    stdatec(data){
      this.stdate = data
    },
    eddatec(data){
      this.eddate = data
    },
    eqc(data){
      this.samedate = data
    },
    sttimec(data){
      this.sttime = data
    },
    edtimec(data){
      this.edtime = data
    },
    inputblured(){
      if (this.stocknum.length == 6 && !isNaN(this.stocknum)) {
        this.inputtype = "is-success"
        this.inputmsg = ""
      } else {
        this.inputtype = "is-danger"
        this.inputmsg = "必须输入6位股票代码"
      }
    },
  }
}
</script>

<style scoped>
.div1-ttls{
  margin-left:60px;
  margin-bottom:20px;
}
.div1-ttls h1{
  font-size:60px;
  margin-bottom:20px
}
</style>
