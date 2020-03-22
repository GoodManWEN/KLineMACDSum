<template>
  <section>
    <b-loading :is-full-page="true" 
    :active.sync="isLoading" :can-cancel="false"></b-loading>
  </section>
</template>

<script>
export default {
  name:"loading",
  data() {
    return {
        isFullPage: true
    }
  },
  props:{
    isLoading:{
      type:Boolean,
      default:false,
    }
  },
  methods: {
      openLoading() {
          this.isLoading = true
          setTimeout(() => {
              this.isLoading = false
          }, 1 * 1000)
      }
  }
  }
</script>

<style scoped>
</style>
