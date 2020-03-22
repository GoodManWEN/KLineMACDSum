<template>
  <div>
    <div class="fllss">
      <b-field label="开始日期">
      <b-datepicker
        v-model="stdate"
        placeholder="2020/01/01"
        icon="calendar-today"
        editable>
      </b-datepicker>
      </b-field>
    </div>
    <div class="fllss">
      <b-field label="截止日期">
      <b-datepicker
        v-model='eddate'
        placeholder="2020/12/31"
        icon="calendar-today"
        editable>
      </b-datepicker>
      </b-field>
    </div>
  </div>
</template>

<script>
import { log } from 'util'
export default {
  name: 'dates',
  data() {
    return {
      stdate:new Date(),
      eddate:new Date(),
      stdatestr:"2020-01-01",
      eddatestr:"2020-01-01",
    }
  },
  props:{
    radio:{
      type:String
    }
  },
  watch:{
    stdate(val){
      let days = this.PrefixZero(val.getDate(), 2)
      let months = this.PrefixZero(val.getMonth() + 1, 2)
      let years = this.PrefixZero(val.getFullYear(), 4)
      this.stdatestr = years + '-' + months + '-' + days
      this.$emit('stdatechanged',this.stdatestr)
    },
    eddate(val){
      let days = this.PrefixZero(val.getDate(), 2)
      let months = this.PrefixZero(val.getMonth() + 1, 2)
      let years = this.PrefixZero(val.getFullYear(), 4)
      this.eddatestr = years + '-' + months + '-' + days
      this.$emit('eddatechanged',this.eddatestr)
    },
    isequal(val){
      this.$emit('isequalchanged',this.isequal)
    },
    radio(val){
    }
  },
  computed:{
    phst () {
      return this.stdatestr.replace(/-/,'/').replace(/-/,'/')
    },
    phed () {
      return this.eddatestr.replace(/-/,'/').replace(/-/,'/')
    },
    isequal() {
      return this.stdatestr == this.eddatestr
    }
  },
  methods:{
    PrefixZero(num, n) {
      return (Array(n).join(0) + num).slice(-n);
    }
  }
}
</script>

<style scoped>
.fllss{
  float:left;
  width:50%;
  padding-right:50px;
  margin-bottom:50px;
}
</style>
