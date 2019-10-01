<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col">
                <h3>¿ Estas seguro que deseas eliminar este paciente?</h3>              
                <p>Nombre: {{this.element.name}}</p>
            
            </div> 
        </div> 
        <div class="row">
            <div class="col">
                <b-button v-on:click="deletePatient" variant="danger">Eliminar</b-button>
            </div>
        </div>        
    </div> 
</template>

<script>
import axios from 'axios';
import swal from 'sweetalert'

export default {
    data(){
        return{
            patientId: this.$route.params.patientId,
            element: {
                name: ''
            }
        }
    },
    methods:{
        getPatient (){
            const path= `${process.env.BASE_URI}patient/${this.patientId}/` 
        
            axios.get(path).then((response)=>{
                this.element.name = response.data.name
            })
            .catch((error)=>{
                console.log(error)
            })
        },
        deletePatient(){
            const path= `${process.env.BASE_URI}patient/${this.patientId}/` 
            axios.delete(path).then((response)=>{
                location.href = '/patient'
                swal("Paciente eliminado exitosamente", "", "success")
            })
            .catch((error)=>{
                console.log(error)
                swal("No es posible eliminar el paciente", "", "error")
            })
        }       
    },
    created(){
        this.getPatient()
    }
}
</script>