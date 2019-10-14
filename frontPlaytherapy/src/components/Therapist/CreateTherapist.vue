<template>
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Registrar Terapeuta {{form.name}}.</h2>              
            </div> 
        </div>       
        <div class="row">
            <div class="col">
                <div class="card">
                    <div class="card-body">
                        <form @submit="onSubmit"> 
                            <div class="form-group row">
                                <label for="name" class="col-sm-2 col-from-label">Nombre</label>
                                
                                <div class="col-sm-6">
                                    <b-form-input  type="text" placeholder="Nombre" name="name" class="form-control" v-model.trim="form.name"></b-form-input> 
                                </div>                                                                      
                            </div>
                            <div class="form-group row">
                                <label for="lastname" class="col-sm-2 col-from-label">Apellido</label>
                                
                                <div class="col-sm-6">
                                    <b-form-input  type="text" placeholder="Apellido" name="lastname" class="form-control" v-model.trim="form.lastname"></b-form-input>                                  
                                </div>                                                                        
                            </div>  
                            <div class="form-group row">
                                <label for="id_type" class="col-sm-2 col-from-label">Tipo de identificación</label>        
                                <div class="col-sm-6">
                                    <b-form-select class="mb-3" v-model.trim="form.id_type">
                                        <option >Cédula de ciudadania</option>
                                        <option >Tarjeta de identidad</option>
                                        <option >Número de pasaporte</option>
                                        <option >Cédula de extranjeria</option>
                                    </b-form-select>                                      
                                </div>                                                                      
                            </div>   
                            <div class="form-group row">
                                <label for="username" class="col-sm-2 col-from-label">Numero de identificación</label>
                                
                                <div class="col-sm-6">
                                    <b-form-input type="text" placeholder="Numero de identificación" name="username" class="form-control" v-model.trim="form.username"></b-form-input>  
                                </div>                                                                      
                            </div>                                            
                            <div class="form-group row">
                                <label for="genre" class="col-sm-2 col-from-label">Sexo</label>        
                                <div class="col-sm-6">
                                    <b-form-select class="mb-3" v-model.trim="form.genre">
                                        <option >Masculino</option>
                                        <option >Femenino</option>
                                    </b-form-select>                                      
                                </div>                                                                      
                            </div> 
                            <div class="form-group row">
                                <label for="email" class="col-sm-2 col-from-label">Correo electronico</label>                              
                                <div class="col-sm-6">
                                    <b-form-input  type="text" placeholder="Correo Electronico" name="email" class="form-control" v-model.trim="form.email"></b-form-input> 
                                </div>                                                                      
                            </div>   
                            <div class="form-group row">
                                <label for="contraseña" class="col-sm-2 col-from-label">Contraseña</label>
                                <div class="col-sm-6">
                                    <b-form-input  type="password" placeholder="Contraseña" name="password" minlength="8" class="form-control" v-model.trim="form.contraseña"></b-form-input>                                  
                                </div>                                                                                                       
                            </div>
                             <div class="rows">
                                <div class="col text-left">
                                    <b-button type="submit" variant="success">Crear</b-button>
                                    <b-button class="btn-large-space" :to="{ name: 'ListPatient' }">Cancelar</b-button>
                                </div>
                        </div>
                        </form>                      
                    </div>
                </div>
            </div>
        </div>
    </div>   
</template>
<script>
import axios from 'axios';
import swal from 'sweetalert'
export default {
    data(){
        return {
            form: {
                name: ''
            }
        }
    },
    methods: {
        onSubmit(event){
            event.preventDefault()
            const path= `${process.env.BASE_URI}therapist/` 
            alert("voy")
            axios.post(path, this.form).then((response)=>{
                alert("2")
                this.form.name = response.data.first_name
                this.form.lastname = response.data.last_name
                this.form.contraseña = response.data.password
                this.form.username = response.data.username
                this.form.email = response.data.email 
                this.form.id_type = response.data.id_type
                this.form.name = response.data.name 
                this.form.lastname = response.data.lastname
                this.form.genre = response.data.genre
                console.log(this.form.name)
                console.log(this.form.lastname)
                console.log(this.form.contraseña)
                console.log(this.form.id_type)
                console.log(this.form.username)
                console.log(this.form.email)
                console.log(this.form.lastname)
                console.log(this.form.genre)            
                swal("Therapeuta creado exitosamente.", "", "success")
           })
            .catch((error)=>{
                swal("No se ha podido crear el Terapeuta.", "", "error")
                console.log(error)
            })
        },              
    },
    created(){
    }    
}
</script>