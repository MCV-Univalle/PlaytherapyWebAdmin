<template>  
    <div>
        <Navigation />
        <main :style="{marginTop: '90px'}">              
            <mdb-container>
                <mdb-row class="mt-5 justify-content-start">
                    <h4 class="demo-title"><strong>Actualizar tipo de diagnóstico </strong></h4>      
                </mdb-row>
                <hr />  
                <section class="demo-section">
                    <section>
                        <form class="needs-validation" novalidate @submit="checkForm">                            
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
                            <div class="text-center mt-4">
                                <mdb-btn color="info" type="submit" variant="success">Actualizar</mdb-btn>
                                <a href="/typeDiagnostic" class="btn btn-light black-text">Cancelar</a> 
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
            mdbCol, 
            mdbDatatable,
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
                typeDiagnosticID: this.$route.params.typeDiagnosticID,
                form: {
                    name: ''
                }
            }
        },
    methods: {
        onSubmit(event){
                event.preventDefault()
                const path= `http://localhost:8000/api/v1.0/typeDiagnostic/${this.typeDiagnosticID}/`;
                axios.put(path, this.form).then((response)=>{
                    this.form.name = response.data.name;
                    swal("Tipo de diagnostico actualizado exitosamente.", "", "success")
            })
                .catch((error)=>{
                    swal("No se ha podido actualizar el tipo de diagnostico.", "", "error")
                    console.log(error);
                })
            },
        getTypeDiagnostic(){
            const path= `http://localhost:8000/api/v1.0/typeDiagnostic/${this.typeDiagnosticID}/`;
                axios.get(path, this.form).then((response)=>{
                    this.form.name = response.data.name;
                    console.log(response);
            })
        },
        checkForm(event) {
            event.target.classList.add('was-validated');
            this.onSubmit(event);

        }            
    },
    created(){
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