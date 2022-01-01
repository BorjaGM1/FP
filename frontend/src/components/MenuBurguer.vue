<template>
  <div>
    <button @click="elegir_burguer('Pollo')">Pollo</button>
    <button @click="elegir_burguer('Ternera')">Ternera</button>
    <button @click="elegir_burguer('Vacuno')">Vacuno</button>
    <br />
    <button @click="atras()">Atras</button>
  </div>
</template>

<script>
export default {
  name: "MenuBurguer",
  methods: {
    elegir_burguer: function (tipo) {
      console.log(tipo);
      this.$emit("nueva-burguer", tipo);
    },
    atras: function () {
      this.$emit("atras");
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>