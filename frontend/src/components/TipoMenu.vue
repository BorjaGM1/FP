<template>
  <div>
    <button @click="elegir_menu('MenuBurguer')">Ir a burguers</button>
    <button @click="elegir_menu('MenuBebida')">Ir a bebidas</button>
  </div>
</template>

<script>
export default {
  name: "TipoMenu",
  methods: {
    elegir_menu: function (tipo) {
      this.$emit("elegir-menu", tipo);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>