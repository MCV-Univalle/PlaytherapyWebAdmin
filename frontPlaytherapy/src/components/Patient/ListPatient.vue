<template>
    <div class="container">
        <div class="row">
            <div class="col">
                <h2>Listado de pacientes registrados.</h2>
                <b-button size="sm" :to="{name: 'CreateEntity'}" variant="primary">
                    Crear entidad medica.
                </b-button>
                <div class="col-md-12">
                    <b-table striped hover :items="patient" :fields="fields">

                        <template v-slot:cell(action)="row" slote-scope="data">
                            <b-button size="sm" variant="primary" >
                                Editar
                            </b-button>
                            <b-button size="sm" variant="danger"  >
                                Eliminar
                            </b-button>
                         </template>

                    </b-table>
                </div>
            </div> 
        </div>
    </div>   
</template>

<script>
import axios from 'axios';

export default {
    data(){
        return{
            patientId: this.$route.params.patientId,
            fields: [
                { key : 'id_type', label:'Tipo identificación'},
                { key : 'id_num', label:'Numero de identificación'},
                { key : 'name', label:'Nombre'},
                { key : 'lastname', label:'Apellido'},
                { key : 'genre', label:'Sexo'},
                { key : 'occupation', label:'Ocupación'},
                { key : 'birthday', label:'Fecha de nacimiento'},
                { key : 'entity', label:'Entidad'},
                { key : 'list_diagnostic', label:'Diagnostico'},
                { key : 'action', label:''}
            ],
            patient: [],
            diagnostic: []
        }
    },
    methods: {
        getPatient(){
            console.log("voy")
            const path = `${process.env.BASE_URI}patient/`
            axios.get(path).then((response) =>{
                this.patient = response.data
            })
            .catch((error)=>{
                console.log(error)
            })
        }
    },
    created(){
        this.getPatient()
    }
}
</script>