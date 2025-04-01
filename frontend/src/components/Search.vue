<template>
    <div>
      <input v-model="busca" placeholder="Digite o nome da operadora" />
      <button @click="buscarOperadora">Buscar</button>
  
      <ul>
        <li v-for="operadora in operadoras" :key="operadora.id">
          {{ operadora.nome }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        busca: "",
        operadoras: [],
      };
    },
    methods: {
      async buscarOperadora() {
        const response = await axios.get(`http://127.0.0.1:8000/buscar?nome=${this.busca}`);
        this.operadoras = response.data;
      },
    },
  };
  </script>
  