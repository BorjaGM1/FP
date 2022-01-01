<template>
<div>
  <button @click="elegir_bebida('Cola')">Cola</button>
  <button @click="elegir_bebida('Limon')">Limon</button>
  <button @click="elegir_bebida('Naranja')">Naranja</button>
  <br/>

  <button @click="atras()">Atras</button>
</div>
</template>

<script>
export default {
  name: "MenuBebida",
  methods: {
    elegir_bebida: function (tipo){
      this.$emit("nueva-bebida",tipo)
    },
    atras: function() {
      this.$emit("atras")
    }
  }
}
</script>

<style scoped>

</style>