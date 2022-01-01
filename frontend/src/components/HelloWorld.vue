<template>
  <div>
    <MenuPrincipal @nuevo-pedido="nuevo_pedido"></MenuPrincipal>
    --------
    <Pedido v-bind:pedido="pedido"></Pedido>
    <button @click="reiniciar_pedido">Reiniciar pedido</button>
  </div>
</template>

<script>
import Pedido from "./Pedido";
import MenuPrincipal from "./MenuPrincipal";

export default {
  name: "Contenedor",
  data: function () {
    return {
      pedido: [],
    };
  },
  components: {
    Pedido,
    MenuPrincipal,
  },
  methods: {
    nuevo_pedido: function (value) {
      console.log(value);
      this.pedido.push(`${value}`);
    },
    reiniciar_pedido: function () {
      this.pedido = [];
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>