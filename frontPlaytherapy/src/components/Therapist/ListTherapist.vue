<template>
    <div class="container">
        <div class="row">
            <div class="col">
                <h2>Listado de Terapeutas registrados.</h2>
                <b-button size="sm" :to="{name: 'CreateTherapist'}" variant="primary">
                    Crear entidad medica.
                </b-button>
                <div class="col-md-12">
                    <b-table striped hover :items="therapist" :fields="fields">

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
            therapistId: this.$route.params.therapistId,
            fields: [
                { key : 'id_type', label:'Tipo identificación'},
                { key : 'username', label:'Numero de identificación'},
                { key : 'first_name', label:'Nombre'},
                { key : 'last_name', label:'Apellido'},
                { key : 'genre', label:'Sexo'},
                { key : 'email', label:'Correo electronico'},
                { key : 'action', label:''}
            ],
            therapist: []
        }
    },
    methods: {
        getTherapist(){
            const path = `${process.env.BASE_URI}therapist/`
            axios.get(path).then((response) =>{
                this.therapist = response.data
            })
            .catch((error)=>{
                console.log(error)
            })
        }
    },
    created(){
        this.getTherapist()
    }
}
</script>