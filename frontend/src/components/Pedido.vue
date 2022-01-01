<template>
<div>
  Su pedido actual:
  <li v-for="elemento in pedido" :key="elemento">
    {{elemento}}
  </li>
</div>
</template>

<script>
export default {
  name: "Pedido",
  props: {pedido: Array,
  },
}
</script>

<style scoped>

</style>