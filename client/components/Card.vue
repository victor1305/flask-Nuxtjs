<template>
  <v-card class="mx-auto card">
    <v-card-title class = "card-title">{{name}}</v-card-title>
    <v-card-text class="v-card-text">Tel: {{phone}}</v-card-text>
    <v-card-text class="v-card-text">{{address}}</v-card-text>
    <v-card-text class="v-card-text">{{web}}</v-card-text>
    <v-card-text class="v-card-text-date">Añadido el:</v-card-text>
    <v-card-text class="v-card-text">{{created}}</v-card-text> 
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
    color: #35495e;;
}

.v-card-text {
    padding: 4px;
}

.v-card-text-date{
    padding-top: 4px;
    padding-bottom: 0px;
}
</style>