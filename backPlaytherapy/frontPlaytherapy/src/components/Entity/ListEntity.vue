<template>  
  <div>
    <Navigation />
    <main :style="{marginTop: '90px'}">              
      <mdb-container>
        <mdb-row class="mt-5 justify-content-start">
            <h4 class="demo-title"><strong>Lista de entidades médicas</strong></h4>      
        </mdb-row>
        <hr />
        <div class="flex-center">  
          <section class="demo-section">
            <section>
              <div class="text-right mt-4">   
                <mdb-btn size="sm" tag="a" color="info" href="/entity/update" ><mdb-icon icon="user-edit" /> Editar</mdb-btn>               
                <mdb-btn size="sm" color="danger" @click="hidden=true"><mdb-icon icon="trash" /> Eliminar</mdb-btn>
              </div>
              <mdb-datatable
                :data="data"
                striped
                bordered
                arrows
                focus
                :display="5"
                responsive
                entriesTitle="Mostrar entradas"
                searchPlaceholder="Buscar"          
                noFoundMessage="Información no encontrada"
                showingText="Cantidad"
                :tfoot= false
              />                 
              <mdb-container @hidden="handleHidden">
                <mdb-modal centered :show="hidden" @close="hidden = false" warning>
                  <mdb-modal-header>
                    <mdb-modal-title center>Advertencia!</mdb-modal-title>
                  </mdb-modal-header>
                  <mdb-modal-body>
                    <mdb-row>                     
                      <mdb-col>
                        <p class="card-text"><strong>¿Desea eliminar la entidad médica {{}} ?</strong></p>
                      </mdb-col>
                    </mdb-row>
                  </mdb-modal-body>
                  <mdb-modal-footer center>
                    <mdb-btn color="warning" @click="hidden = false">Aceptar</mdb-btn>
                    <mdb-btn outline="warning" @click="hidden = false">Cancelar</mdb-btn>
                  </mdb-modal-footer>
                </mdb-modal>
              </mdb-container>          
            </section>                     
          </section>           
        </div>   
      </mdb-container>            
    </main>       
  </div>    
</template>

<script>
    import axios from 'axios';
    import {
        mdbDatatable,
        mdbBtn,
        mdbIcon,
        mdbRow,
        mdbContainer,
        mdbModal,
        mdbModalHeader,
        mdbModalTitle,
        mdbModalBody,
        mdbModalFooter,
    } from "mdbvue";
    import Navigation from '@/components/Navigation/Navigation';

  export default {
    components: {
      mdbDatatable,
      mdbBtn,
      mdbContainer,
      mdbIcon,
      mdbRow,
      Navigation,
      mdbModal,
      mdbModalHeader,
      mdbModalTitle,
      mdbModalBody,
      mdbModalFooter,
    },
    data() {
      return {
        columns: [],
        rows: [],
        hidden: false,
      };
    },
    computed: {
      data() {
        return {          
          columns: [
            {
              label: "Nombre",
              field: "name",
              sort: "asc"
            },
          ],
          rows: this.rows 
        };
      },
    },
    methods: {
      filterData(dataArr, keys) {
        let data = dataArr.map(entry => {
          let filteredEntry = {};
          keys.forEach(key => {
            if (key in entry) {
              filteredEntry[key] = entry[key];
            }
          });
          return filteredEntry;
        });
        return data;
      }
    },
    mounted(){
      fetch('http://localhost:8000/api/v1.0/entity/?format=json')
        .then(res => res.json())
        .then(json => {
          let keys = ['name'];
          let entries = this.filterData(json, keys);
          //columns
          console.log(json)
          this.columns = keys.map(key => {
            return {
              label: key,
              field: key,
            };
          });
          //rows
          entries.map(entry => this.rows.push(entry));        
        })
        .catch(err => console.log(err));
    }
  };
</script>

<style scoped>
    .demo-section {
        padding: 20px 0;
    }
    .demo-section > section {
        border: 1px solid #e0e0e0;
        padding: 15px;
    }
    .demo-section > h4 {
        font-weight: bold;
        margin-bottom: 20px;
    }
    .demo-title {
        color: #9e9e9e;
        font-weight: 700;
        margin-bottom: 0;
        padding-left: 15px;
    }  
</style>