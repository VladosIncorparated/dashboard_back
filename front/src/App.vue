<template>
  <div :style="{  height: '100vh' }">
    <Logs/>
  </div>
</template>

<script>
  import Logs from './components/Logs.vue';

  export default {
    components:{
      Logs,
    },

    data() {
      return {
        
      }
    },
  }
</script>