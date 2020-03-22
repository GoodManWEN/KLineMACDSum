<template>
  <div>
    <div class="fllss">
    <b-field label="开始时间">
      <b-slider rounded
                v-model="sttime"
                :min='0'
                :max="1000"
                :tooltip="false"
                size="is-large"
      ></b-slider>
      
    </b-field>
    <b-tag type="is-dark" size="is-large"
    >
      {{sttime_time}}
      </b-tag>
    </div>
    <div class="fllss">
      <b-field label="截止时间">
      <b-slider rounded
                v-model="edtime"
                :min='0'
                :max="1000"
                :tooltip="false"
                size="is-large"
      ></b-slider>
      </b-field>
      <b-tag type="is-dark" size="is-large"
              >
        {{edtime_time}}
      </b-tag>
    </div>
  </div>
</template>

<script>
import { log } from 'util'
export default {
  name: 'timel',
  data() {
    return {
      sttime:0,
      edtime:1000,
      sttime_time:"09:30",
      edtime_time:"15:00",
    }
  },
  props:{
    radio:{
      type:String
    },
    samedate:{
      type:Boolean,
      default:true
    }
  },
  watch:{
    sttime(val){
      if (this.samedate) {
        if (val > this.edtime) {
          this.edtime = val
        }
      }
      let floats = val * 24
      let hb = Math.floor(floats / 3000)
      let rb = Math.floor((floats % 3000) / 100)
      let rls = ['09','10','10','11','13','13','14','14','15']
      let jls = [30,0,30,0,0,30,0,30,0]
      let kl = jls[hb] + rb
      let jl = ''
      if (kl < 10) {
        jl = '0' + String(kl)
      } else {
        jl = String(kl)
      }
      this.sttime_time = rls[hb] +':'+ jl
      this.$emit('sttimechanged',this.sttime_time)
    },
    edtime(val) {
      if (this.samedate) {
        if (val < this.sttime) {
          this.sttime = val
        }
      }
      let floats = val * 24
      let hb = Math.floor(floats / 3000)
      let rb = Math.floor((floats % 3000) / 100)
      let rls = ['09','10','10','11','13','13','14','14','15']
      let jls = [30,0,30,0,0,30,0,30,0]
      let kl = jls[hb] + rb
      let jl = ''
      if (kl < 10) {
        jl = '0' + String(kl)
      } else {
        jl = String(kl)
      }
      this.edtime_time = rls[hb] +':'+ jl
      this.$emit('edtimechanged',this.edtime_time)
    },
    radio(val){
      if (val == 'd' || val == 'w' || val == 'm') {
        this.sttime = 0
        this.edtime = 1000
      }
    }
  }
}
</script>

<style scoped>
.fllss{
  float:left;
  width:50%;
  padding-right:50px;
  padding-left:5px;
  margin-bottom:50px;
}
</style>
