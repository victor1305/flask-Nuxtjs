<template>
  <div class="container">
    <h1 class="title">Gestor de Empresas de Transporte</h1>
    <a class="button btn-add" @click="isModalActive=true">
      <strong>Añadir Empresa</strong>
    </a>
    <b-modal :active.sync="isModalActive">
      <form action="" v-on:submit.prevent="create_partner">
          <div class="modal-card" style="width: auto">
          <header class="modal-card-head">
              <p class="modal-card-title">Añadir una Empresa</p>
          </header>
          <section class="modal-card-body">
              <b-field label="Empresa">
                  <b-input
                      type="text"
                      v-model="name"
                      required>
                  </b-input>
              </b-field>
              <b-field label="Dirección">
                  <b-input
                      type="text" 
                      v-model="address"
                      required>
                  </b-input>
              </b-field>
              <b-field label="Teléfono">
                  <b-input
                      type="number" 
                      v-model="phone"
                      required>
                  </b-input>
              </b-field>
              <b-field label="Web">
                  <b-input
                      type="text" 
                      v-model="web"
                      required>
                  </b-input>
              </b-field>
          </section>
          <footer class="modal-card-foot">
              <button class="button is-primary">Añadir</button>
          </footer>
          </div>
      </form>
    </b-modal>
    <div class="card-container" v-if="partners.length > 0">
      <div class = "form-order-container">
        <b-form inline action="" v-on:submit.prevent="get_partners" class = "form-order">
          <b-form-select v-model="selected" :options="options" size="sm" class = "select-order"></b-form-select>
          <button class = "order-bnt">Ordenar</button>
        </b-form>
      </div>
    <v-row
    >
      <Card
        v-for = "partner of partners"
        v-bind:key = "partner.id"
        class = "mb-5"
        :name = "partner.name"
        :address = "partner.address"
        :phone = "partner.phone"
        :web = "partner.web"
        :created = "partner.created"
      >
        <template v-slot:button>
          <a class="button btn-delete" v-on:click="delete_partner(partner.id)">Borrar</a>
        </template>
      </Card>
    </v-row>
    </div>
  </div>
</template>

<script>

import axios from 'axios'
import Card from '../components/Card.vue'

export default {

  components: {
    Card
  },

  head() {
    return {
      title: 'Gestión de Transportes | Home',
      meta: [
        {
          hid: "description",
          name: "description",
          content: "Página para gestionar las empresas de transporte"
        }
      ]
    }
  },

  data () {
    return{
      partners: [

      ],
      isModalActive: false,
      name: "",
      address: "",
      phone: "",
      web: "",
      selected: null,
      options: [
        { value: null, text: '----Ordenar por----' },
        { value: 'az', text: 'Nombre (A-Z)' },
        { value: 'za', text: 'Nombre (Z-A)' },
        { value: 'newfirst', text: 'Fecha (Ascendente)' },
        { value: 'oldFirst', text: 'Fecha (Descendente)' }
      ]
    }
  },  

  methods: {

    get_partners() {
      return this.$axios.post('/', {
            order: this.selected
        })
        .then(response => {
          this.partners = response.data
      })

      .catch(error => {
        console.log(error)
      })
    },

    create_partner() {
      return this.$axios.post('/new', {
          name: this.name,
          address: this.address,
          phone: this.phone,
          web: this.web
      })
      .then( () => {
          this.name = '',
          this.address = '',
          this.phone = '',
          this.web = '',
          this.isModalActive = false
          this.get_partners()
      })
      .catch(error => console.log(error))
    },

    delete_partner(id) {
      return this.$axios.delete(`/${id}`)
      .then(() => this.get_partners())
      .catch(error => console.log(error))
    }
  },

  created () {
    this.get_partners()
    
  }
}
</script>

<style>
.container {
  margin: 0 auto;
  min-height: 100vh;
  text-align: center;
  
}

.card-container {
  margin-top: 4%;
}

.btn-add:hover {
  text-decoration: none;
  color: #3b8070;
}

.btn-delete {
  border-color: #3b8070;
}

.btn-delete:hover {
  text-decoration: none;
  color: red;
  border-color: red;
}

.title {
  font-family:
    'Quicksand',
    'Source Sans Pro',
    -apple-system,
    BlinkMacSystemFont,
    'Segoe UI',
    Roboto,
    'Helvetica Neue',
    Arial,
    sans-serif;
  display: block;
  color: #35495e;
  padding: 2%;
}

.form-order-container {
  width: 300px;
  margin-bottom: 3%;
  display: flex
}

.select-order {
  width: 170px;
}

.order-bnt {
  margin-left: 10px;
  width: 70px;
  font-size: 0.75rem;
  background-color: white;
  border-color: #dbdbdb;
  border-width: 1px;
  justify-content: center;
  padding-bottom: calc(0.5em - 1px);
  padding-left: 1em;
  padding-right: 1em;
  padding-top: calc(0.5em - 1px);
  text-align: center;
  border-radius: 7%;
}

.order-bnt:hover {
  color: #3b8070;
  border: 1px solid #35495e;
}


</style>
