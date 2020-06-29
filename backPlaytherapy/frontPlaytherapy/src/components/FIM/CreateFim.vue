<template>  
    <div>
        <Navigation />
        <main :style="{marginTop: '90px'}">              
            <mdb-container>
                <mdb-row class="mt-5 justify-content-start">
                    <h4 class="demo-title"><strong>Medida de independencia funcional</strong></h4>      
                </mdb-row>
                <hr />   
                <section class="demo-section">
                    <section>
                        <form class="needs-validation" novalidate @submit="checkForm">                            
                            <div class="col-md-12 mb-6">                                                     
                                <label class="margin-label" for="date">Fecha</label>
                                <input type="date" 
                                        name="date" 
                                        class="form-control" 
                                        v-model.trim="form.date" 
                                        required>  
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor ingrese la fecha
                                </div>
                            </div>
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="goal">Meta</label>
                                <div class="custom-control custom-checkbox lg" >
                                    <input type="checkbox" 
                                        class="custom-control-input" 
                                        id="customControlValidation1"
                                        v-model.trim="form.goal"
                                        >
                                    <label class="custom-control-label lg" for="customControlValidation1"></label>
                                </div>                           
                            </div>
                            <mdb-row class="mt-3 align-items-center justify-content-start">
                                <h4 class="demo-title text-center"><strong>Movimiento</strong></h4>
                            </mdb-row>
                            <hr />
                            <h6 class="demo-title-small"><strong>Autocuidado</strong></h6>
                            <hr />
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="eat">Comer</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.eat" 
                                        placeholder="Comida" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de comer
                                </div>
                            </div>                            
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="personal_clean">Arreglo personal</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.personal_clean" 
                                        placeholder="Limpieza personal" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de arreglo personal
                                </div>
                            </div>  
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="bath">Bañarse/Ducharse</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.bath"     
                                        placeholder="Bañarse/Ducharse" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de bañarse/ducharse
                                </div>
                            </div> 
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="dress_undress_sup">Vestirse/Desvertirse superior</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.dress_undress_sup"  
                                        placeholder="Vestirse/Desvertirse Superior" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de vestirse/desvertirse superior
                                </div>
                            </div> 
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="dress_undress_inf">Vestirse/Desvertirse inferior</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.dress_undress_inf" 
                                        placeholder="Vestirse/Desvertirse Inferior" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de vestirse/desvertirse inferior
                                </div>
                            </div>  
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="bathUse">Uso del baño</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.bathUse" 
                                        placeholder="Uso del baño" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de uso del baño
                                </div>
                            </div> 
                            <h6 class="demo-title-small"><strong>Control de esfínteres</strong></h6>
                            <hr />            
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="control_dregs">Control de heces</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.control_dregs" 
                                        placeholder="Control de heces" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de control de heces
                                </div>
                            </div> 
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="control_urine">Control de orina</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.control_urine" 
                                        placeholder="Control de orina" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de control de orina.                                </div>
                            </div> 
                            <h6 class="demo-title-small"><strong>Movilidad</strong></h6>
                            <hr />  
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="tras_bed_chair">Traslado de la cama a silla o silla de ruedas</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.tras_bed_chair" 
                                        placeholder="Cama, silla y silla de ruedas" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de traslado de la cama a silla o silla de ruedas.
                                </div>
                            </div>  
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="tras_bath">Traslado al baño</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.tras_bath" 
                                        placeholder="Baño" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de traslado al baño
                                </div>
                            </div>              
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="tras_shower">Traslado en bañera o ducha</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.tras_shower" 
                                        placeholder="Ducha" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de traslado en bañera o ducha
                                </div>
                            </div> 
                            <h6 class="demo-title-small"><strong>Ambulación</strong></h6>
                            <hr />  
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="run_crawl_chair">Caminar/desplazarse en silla de ruedas y gateo</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.run_crawl_chair" 
                                        placeholder="Marcha, silla de ruedas y gateo" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de caminar/desplazarse en silla de ruedas y gateo
                                </div>
                            </div> 
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="steps">Subir y bajar escaleras</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.steps" 
                                        placeholder="Gradas" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de subir y bajar escaleras
                                </div>
                            </div>                             
                            <mdb-row class="mt-3 align-items-center justify-content-start">
                                <h4 class="demo-title text-center"><strong>Reconocimiento</strong></h4>
                            </mdb-row> 
                            <hr />
                            <h6 class="demo-title-small"><strong>Comunicación</strong></h6>
                            <hr />
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="compresion">Compresión</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.compresion" 
                                        placeholder="Compresión" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de compresión
                                </div>
                            </div>            
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="expresion">Expresión</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.expresion" 
                                        placeholder="Expresión" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de expresión
                                </div>
                            </div> 
                            <h6 class="demo-title-small"><strong>Conocimiento social</strong></h6>
                            <hr />
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="social_inter">Interacción social</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.social_inter" 
                                        placeholder="Interacción social" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de interacción social
                                </div>
                            </div> 
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="problem_solve">Resolver problema</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.problem_solve" 
                                        placeholder="Resolver problema" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de resolver problema
                                </div>
                            </div>  
                            <div class="col-md-12 mb-6">
                                <label class="margin-label" for="memory">Memoria</label>
                                <select class="browser-default custom-select" 
                                        v-model.trim="form.memory" 
                                        placeholder="Memoria" 
                                        required>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                </select>
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el valor de memoria
                                </div>
                            </div>  
                            <div class="text-center mt-4">
                                <mdb-btn color="info" type="submit" variant="success">Registrar</mdb-btn>
                                <a href="/patient" class="btn btn-light black-text">Cancelar</a>
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
    import { mdbContainer, mdbBtn, mdbRow, mdbInput } from "mdbvue";
    import Navigation from '@/components/Navigation/Navigation';

    export default {
        name: "InputsPage",
        components: {
            mdbContainer,
            mdbBtn,
            mdbRow,
            mdbInput,
            Navigation,
        },
        data(){
            return {
                patientID: this.$route.params.patientID,
                form: {
                    name: ''
                },
                patient: []

            }
        },
        methods: {
            onSubmit(event){
                event.preventDefault()
                const path= 'http://localhost:8000/api/v1.0/FIM/'
                var postData = {
                        date : this.form.date,                
                        goal : this.form.goal,
                        patient: this.patient.id,
                        eat : this.form.eat,
                        personal_clean : this.form.personal_clean,
                        bath : this.form.bath,
                        dress_undress_sup : this.form.dress_undress_sup ,
                        dress_undress_inf : this.form.dress_undress_inf,
                        bathUse : this.form.bathUse,
                        control_dregs : this.form.control_dregs,
                        control_urine : this.form.control_urine,
                        tras_bed_chair : this.form.tras_bed_chair,
                        tras_bath : this.form.tras_bath,
                        tras_shower : this.form.tras_shower ,
                        run_crawl_chair : this.form.run_crawl_chair,
                        steps : this.form.steps,
                        compresion : this.form.compresion,
                        expresion : this.form.expresion,
                        social_inter : this.form.social_inter,
                        problem_solve : this.form.problem_solve,
                        memory : this.form.memory
                        
                };
                axios.post(path, postData).then((response)=>{
                swal("FIM del paciente " + this.patient.name + " creado exitosamente.", "", "success")
            })
                .catch((error)=>{
                    swal("No se ha podido crear el FIM.", "", "error")
                    console.log(error)
                })
            },
            getPatient (){
                const path= `http://localhost:8000/api/v1.0/patient/${this.patientID}/`;
            
                axios.get(path).then((response) =>{
                    this.patient = response.data
                })
                .catch((error)=>{
                    console.log(error)
                })
            },
            checkForm(event) {
            event.target.classList.add('was-validated');
            this.onSubmit(event);
            
            },              
        },
        created(){
            this.getPatient();
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
        font-weight: 400;
        margin-bottom: 0;
        padding-left: 15px;
    }   
    .demo-title-small {
        color: #9e9e9e;
        font-weight: 400;
        margin-bottom: -10px;
        margin-top: 30px;
    }  
    .margin-label{
        margin-top: 20px;
        margin-bottom: 4px;
    } 
</style>