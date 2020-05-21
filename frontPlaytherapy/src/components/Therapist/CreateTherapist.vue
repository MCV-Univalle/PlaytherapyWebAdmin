<template>  
    <div>
        <Navigation />
        <main :style="{marginTop: '90px'}">              
            <mdb-container>
                <mdb-row class="mt-5 justify-content-start">
                    <h4 class="demo-title"><strong>Registrar terapeuta</strong></h4>      
                </mdb-row>
                <hr />   
                <section class="demo-section"> 
                    <section>
                        <form class="needs-validation" novalidate @submit="checkForm">
                            <div class="col-md-12 mb-6">
                                <label for="id_type">Tipo de identificación</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.id_type" 
                                        placeholder="Tipo de identificación" 
                                        required>
                                    <option value="1">Cédula de ciudadanía</option>
                                    <option value="2">Tarjeta de identidad</option>
                                    <option value="3">Cédula de extranjería</option>
                                    <option value="3">Número de pasaporte</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el tipo de identificación.
                                </div>
                            </div>
                            <div class="col-md-12 mb-6">
                                <label for="username">Número de identificación</label>
                                <input type="text" 
                                    class="form-control" 
                                    name="username" 
                                    placeholder="Número de identificación" 
                                    v-model.trim="form.username" 
                                    required>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor ingrese el número de identificación.
                                </div>
                            </div>
                            <div class="col-md-12 mb-6">
                                <label for="name">Nombre</label>
                                <input type="text" 
                                    class="form-control" 
                                    name="name" 
                                    placeholder="Nombre" 
                                    v-model.trim="form.name" 
                                    required>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor ingrese el nombre.
                                </div>
                            </div>
                            <div class="col-md-12 mb-6">
                                <label for="lastname">Apellido</label>
                                <input type="text" 
                                    class="form-control" 
                                    name="lastname" 
                                    placeholder="Apellido" 
                                    v-model.trim="form.lastname" 
                                    required>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor ingrese el apellido.
                                </div>
                            </div>
                            <div class="col-md-12 mb-6">
                                <label for="genre">Género</label>
                                <select class="browser-default custom-select" 
                                        placeholder="Sexo" 
                                        v-model.trim="form.genre" 
                                        required>
                                    <option value="1">Femenino</option>
                                    <option value="2">Masculino</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el género.
                                </div>
                            </div>              
                            <div class="col-md-12 mb-6">
                                <label for="email">Correo electrónico</label>
                                <input type="text" 
                                        class="form-control" 
                                        name="email" 
                                        placeholder="Correo electrónico" 
                                        v-model.trim="form.email" 
                                        required>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor ingrese el correo electrónico.
                                </div>
                            </div>
                            <div class="col-md-12 mb-6">
                                <label for="password">Contraseña</label>
                                <input type="password" 
                                    class="form-control" 
                                    name="password" 
                                    placeholder="Contraseña" 
                                    minlength="8" 
                                    v-model.trim="form.password" 
                                    required>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor ingrese la contraseña de mínimo 8 dígitos.
                                </div>
                            </div>
                            <div class="col-md-12 mb-6">
                                <label for="password">Confirmar contraseña</label>
                                <input type="conformPassword" 
                                    class="form-control" 
                                    name="confirmPassword" 
                                    placeholder="Confirmar contraseña" 
                                    minlength="8" 
                                    v-model.trim="form.password" 
                                    required>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor ingrese nuevamente la contraseña.
                                </div>
                            </div>
                            <div class="text-center mt-4">
                                <mdb-btn color="info" type="submit" variant="success">Registrar</mdb-btn>
                                <a href="/home" class="btn btn-light black-text">Cancelar</a>
                            </div>
                        </form>
                    </section>
                </section>
            </mdb-container>
        </main>  
    </div>          
</template>
<script>
    import axios from 'axios';
    import swal from 'sweetalert'
    import { mdbBtn, 
            mdbRow, 
            mdbInput,
            mdbContainer 
            } from "mdbvue";
    import Navigation from '@/components/Navigation/Navigation';

    export default {
        name: "InputsPage",
        components: {
            mdbBtn,
            mdbRow,
            mdbInput,
            mdbContainer,
            Navigation,
        },
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
                const path= 'http://localhost:8000/auth/users/'
                    console.log(this.form.name)
                    console.log(this.form.password)
                    console.log(this.form.name)

                axios.post(path, this.form).then((response)=>{
                    this.form.name = response.data.username
                    //this.form.lastname = response.data.last_name
                    this.form.password = response.data.password
                    //this.form.username = response.data.username
                    this.form.email = response.data.email 
                    //this.form.id_type = response.data.id_type
                    //this.form.name = response.data.name 
                    //this.form.lastname = response.data.lastname
                    //this.form.genre = response.data.genre           
                    swal("Therapeuta creado exitosamente.", "", "success")
            })
                .catch((error)=>{
                    swal("No se ha podido crear el Terapeuta.", "", "error")
                    console.log(error)
                })
            }, 
            checkForm(event) {
            event.target.classList.add('was-validated');
            this.onSubmit(event);

            },              
        },
        created(){
        }    
    }
</script>

<style scoped>
    .demo-section {
        align-items: center;
        display: flex;
        justify-content: center;
        padding: 20px 0;
    }
    .demo-section > section {
        border: 1px solid #e0e0e0;
        padding: 15px;
        width: 80%;
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
    h2 {
        font-weight: normal;
    }    
    label{
        margin-top: 20px;
        margin-bottom: 4px;
    }
</style>