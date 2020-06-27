<template>  
    <div>
        <Navigation />
        <main :style="{marginTop: '90px'}">              
            <mdb-container>
                <mdb-row class="mt-5 justify-content-start">
                    <h4 class="demo-title"><strong>Registrar diagnóstico</strong></h4>      
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
                                <mdb-row>
                                    <mdb-col center class="col-md-11 col-sm-10 col-10">
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
                                    </mdb-col>
                                        <mdb-col class="col-md-1 col-sm-2 col-2">
                                            <a href="/entity/create" 
                                                class="btn-sm btn-info white-text d-block margin-buttom"
                                                data-toggle="tooltip" title="Añadir nuevo tipo de diagnóstico">
                                                <mdb-icon  class="margin-icon" icon="plus" />
                                            </a>                                        
                                        </mdb-col>
                                    </mdb-row>                          
                                <div class="valid-feedback">
                                    Excelente!
                                </div>
                                <div class="invalid-feedback">
                                    Por favor seleccione el tipo de diagnóstico.
                                </div>
                            </div> 
                            <div class="text-center mt-4">
                                <mdb-btn color="info" type="submit" variant="success">Registrar</mdb-btn>
                                <a href="/patient/create" class="btn btn-light black-text">Cancelar</a> 
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
                info: false,
                warning: false,
                form: {
                    name: ''
                },
                
                typeDiagnostic: [],            
                selected: null,
                
                columns: [],
                rows: []
                
            }
        },computed: {
            data() {
                return {
                columns: [{
                    label: "Nombre",
                    field: "name",
                    sort: "asc",
                    }
                ],
                rows: this.rows
                };
            },
        },
        methods: {
            onSubmit(event){
                event.preventDefault()
                const path= 'http://localhost:8000/api/v1.0/typeDiagnostic/';
                axios.post(path, this.form).then((response)=>{
                    this.form.nameTD = response.data.name;
                    swal("Tipo de diagnostico creado exitosamente.", "", "success")
            })
                .catch((error)=>{
                    swal("No se ha podido crear el tipo de diagnostico.", "", "error")
                    console.log(error);
                })
            },onSubmitD(event){
                event.preventDefault()
                const path= 'http://localhost:8000/api/v1.0/diagnostic/';
                axios.post(path, this.form).then((response)=>{
                    this.form.code = response.data.code;
                    this.form.type_diagnostic = response.data.type_diagnostic;
                    this.form.name = response.data.name;
                    swal("Tipo de diagnostico creado exitosamente.", "", "success")
            })
                .catch((error)=>{
                    swal("No se ha podido crear el tipo de diagnostico.", "", "error")
                    console.log(error);
                })
            },
            checkForm(event) {
                event.target.classList.add('was-validated');
                this.onSubmit(event);

            },
            checkFormD(event) {
                event.target.classList.add('was-validated');
                this.onSubmitD(event);

            },
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
      },getTypeDiagnostic (){
                const path= 'http://localhost:8000/api/v1.0/typeDiagnostic/' 
            
                axios.get(path).then((response) =>{
                    this.typeDiagnostic = response.data
                })
                .catch((error)=>{
                    console.log(error)
                })
            }              
        },
    mounted(){
      fetch('http://localhost:8000/api/v1.0/typeDiagnostic/?format=json')
        .then(res => res.json())
        .then(json => {
          let keys = ["name"];
          let entries = this.filterData(json, keys);
          this.columns = keys.map(key => {
            return {
              label: key.toUpperCase(),
              field: key,
              sort: true
            };
          });
          //rows
          entries.map(entry => this.rows.push(entry));
        })
        .catch(err => console.log(err));
    },created(){
            this.getTypeDiagnostic ()
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
    .margin-buttom {
        margin-left: -15px;
        height: 100%;
    } 
    .margin-icon {
        padding: 20% 32% 20%;
    } 
    @media all and (max-width: 1400px) {
        .margin-icon {
            padding: 20% 33% 10%;
        } 
    }
    @media all and (max-width: 1200px) {
        .margin-icon {
            padding: 30% 25% 10%;
        } 
    }
    @media all and (max-width: 992px) {
        .margin-icon {
            padding: 65% 3% 5%;
        } 
    }
    @media all and (max-width: 778px) {
        
        .margin-icon {
            padding: 25% 30% 10%;
        } 
    }
    @media all and (max-width: 767px) {
        
        .margin-icon {
            padding: 30% 25% 10%;
        } 
    }
    @media all and (max-width: 576px) {
        
        .margin-icon {
            padding: 25% 30% 10%;
        } 
    }
    @media all and (max-width: 500px) {
        
        .margin-icon {
            padding: 40% 15% 10%;
        } 
    }
</style>