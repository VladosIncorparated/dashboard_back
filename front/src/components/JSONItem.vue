<template>
    <div>
      <ul>
        <li v-for="(value, key) in menuItems" :key="key">
          {{ key }}
          <ul v-if="Array.isArray(value)|| typeof (value) === 'object'">
            <JSONItem :menu-items="value"></JSONItem>
          </ul>
          <p v-else>{{ value }}</p>
        </li>
      </ul>
    </div>
  </template>
  
<script>
    export default {
        props: ['menuItems'],
        components: {
            JSONItem: () => import('./JSONItem.vue'),
        },
    };
</script>