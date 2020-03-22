<template>
  <div>
  <section>
    <div class="block">
      <b-radio v-model="radio"
          name="name"
          native-value="5">
          5分钟线
      </b-radio>
      <b-radio v-model="radio"
          name="name"
          native-value="15">
          15分钟线
      </b-radio>
      <b-radio v-model="radio"
          name="name"
          native-value="30">
          30分钟线
      </b-radio>
      <b-radio v-model="radio"
          name="name"
          native-value="60">
          60分钟线
      </b-radio>
      <b-radio v-model="radio"
          name="name"
          native-value="d">
          日线
      </b-radio>
      <b-radio v-model="radio"
          name="name"
          native-value="w">
          周线
      </b-radio>
      <b-radio v-model="radio"
          name="name"
          native-value="m">
          月线
      </b-radio>
    </div>
  </section>
  </div>
</template>

<script>
export default {
  name: 'radios',
  data() {
    return {
        radio: 'd'
    }
  },
  watch:{
    radio(){
      this.$emit('radiochanged',this.radio)
    }
  }
}
</script>

<style scoped>
</style>
