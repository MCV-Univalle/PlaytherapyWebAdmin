<template>  
    <div>
        <Navigation />
        <main :style="{marginTop: '90px'}">              
            <mdb-container>
                <mdb-row class="mt-5 justify-content-start">
                    <h4 class="demo-title"><strong>Actualizar diagnóstico</strong></h4>      
                </mdb-row>
                <hr />  
                <section class="demo-section">
                    <section>
                        <form class="needs-validation" novalidate @submit="checkFormD">                            
                            <div class="col-md-12 mb-6">
                                <label for="code">Código</label>
                                <input type="text" 
                                        class="form-control" 
                                        name="username" 
                                        placeholder="Código de diagnóstico"
                                        v-model.trim="form.code" required>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor ingrese el código del diagnóstico.
                                </div>
                            </div>                        
                            <div class="col-md-12 mb-6">
                                <label for="name">Nombre</label>
                                <input type="text" 
                                        class="form-control" 
                                        name="name" 
                                        placeholder="Nombre" 
                                        v-model.trim="form.name" required>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor ingrese el nombre.
                                </div>
                            </div>
                            <div class="col-md-12 mb-6  col-sm-12">                            
                                <label for="typeDiagnostic">Tipo de diagnóstico</label>                                
                                    <select typeDiagnostic 
                                            class="browser-default custom-select" 
                                            id="inputGroupSelect04" 
                                            v-model.trim="form.type_diagnostic" 
                                            placeholder="Tipo de diagnóstico" 
                                            aria-label="Example select with button addon" 
                                            required>
                                        <template slot:first>
                                            <option :value="null" disabled>-- Por favor seleccione un tipo de diagnóstico --</option>
                                        </template>
                                            <option v-for="typeDiagnostic in typeDiagnostic" 
                                                    :key="typeDiagnostic.id" 
                                                    :value="typeDiagnostic.id" >{{ typeDiagnostic.name }} 
                                            </option>
                                    </select>             
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el tipo de diagnóstico.
                                </div>
                            </div> 
                            <div class="text-center mt-4">
                                <mdb-btn color="info" type="submit" variant="success">Actualizar</mdb-btn>
                                <a href="/diagnostic" class="btn btn-light black-text">Cancelar</a> 
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
    import swal from 'sweetalert';
    import { mdbContainer, 
            mdbBtn, 
            mdbIcon, 
            mdbRow, 
            mdbInput,
            mdbDatatable,
            mdbCol, 
    } from "mdbvue";
    import Navigation from '@/components/Navigation/Navigation';

    export default {
        name: "InputsPage",
        components: {
            mdbContainer,
            mdbBtn,
            mdbIcon,
            mdbRow,
            mdbInput,
            mdbCol, 
            mdbDatatable,
            Navigation
        },
        data(){

           return {
                diagnosticID: this.$route.params.diagnosticID,
                form: {
                    code: '',
                    name: '',
                },
                typeDiagnostic: [],            
                selected: null
            }
        },
        methods: {
            onSubmit(event){
                event.preventDefault()
                const path= `http://localhost:8000/api/v1.0/diagnostic/${this.diagnosticID}/`;
                axios.put(path, this.form).then((response)=>{
                    this.form.code = response.data.code;
                    this.form.type_diagnostic = response.data.type_diagnostic;
                    this.form.name = response.data.name;
                    swal("Diagnostico actualizado exitosamente.", "", "success")
            }).catch((error)=>{
                    console.log(error);
                    swal("No se ha podido actualizar el diagnostico", "", "error")
                })
            },
        getDiagnostic(){
            const path= `http://localhost:8000/api/v1.0/diagnostic/${this.diagnosticID}/`;
                axios.get(path, this.form).then((response)=>{
                    this.form.code = response.data.code;
                    this.form.name = response.data.name;
                    this.form.type_diagnostic = response.data.type_diagnostic;
                    console.log(response)
            }).catch((error)=>{
                    console.log(error)
            })},
        getTypeDiagnostic(){
                const path= 'http://localhost:8000/api/v1.0/typeDiagnostic/' 
            
                axios.get(path).then((response) =>{
                    this.typeDiagnostic = response.data
                })
                .catch((error)=>{
                    console.log(error)
                })
            },
        checkFormD(event) {
            event.target.classList.add('was-validated');
            this.onSubmit(event);

        }              
        },
        created(){
            this.getDiagnostic();
            this.getTypeDiagnostic();
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
    label{
        margin-top: 20px;
        margin-bottom: 4px;
    } 
</style>