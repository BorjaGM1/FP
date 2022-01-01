<template>
  <div>
    <MenuBebida
        @nueva-bebida="nueva_bebida"
        @atras="atras"
        v-if="current_menu === 'MenuBebida'"
    ></MenuBebida>
    <MenuBurguer
        @nueva-burguer="nueva_burguer"
        @atras="atras"
        v-else-if="current_menu === 'MenuBurguer'"
    ></MenuBurguer>
    <TipoMenu @elegir-menu="ir_a" v-else></TipoMenu>
  </div>
</template>

<script>
import TipoMenu from "./TipoMenu";
import MenuBebida from "./MenuBebida";
import MenuBurguer from "./MenuBurguer";
export default {
  name: "MenuPrincipal",
  data: function () {
    return {
      current_menu: "",
    };
  },
  components: { TipoMenu, MenuBebida, MenuBurguer },
  methods: {
    ir_a: function (tipo) {
      this.current_menu = tipo;
    },
    atras: function () {
      this.current_menu = "";
    },
    nueva_burguer: function (value) {
      this.current_menu = "";
      console.log(value);
      this.$emit("nuevo-pedido", `Burguer de ${value}`);
    },
    nueva_bebida: function (value) {
      this.current_menu = "";
      console.log(value);
      this.$emit("nuevo-pedido", `Bebida de ${value}`);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>