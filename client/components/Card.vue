<template>
  <v-card class="mx-auto card">
    <v-card-title class = "card-title">{{name}}</v-card-title>
    <v-card-text>{{address}}</v-card-text>
    <v-card-text>Tel: {{phone}}</v-card-text>
    <v-card-text>{{web}}</v-card-text>
    <v-card-text>Añadido el: {{created}}</v-card-text>
    <v-card-actions>
        <v-spacer></v-spacer>
        <slot name="button"></slot>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: ["name", "address", "phone", "web", "id", "created"]
};
</script>

<style>

.card {
    width: 200px;
}

.card-title {
    color: #35495e;
}

</style>