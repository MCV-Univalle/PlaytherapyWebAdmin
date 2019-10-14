<template>
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Registrar paciente {{form.name}}.</h2>              
            </div> 
        </div>       
        <div class="row">
            <div class="col">
                <div class="card">
                    <div class="card-body">
                        <form @submit="onSubmit">  
                            <div class="form-group row">
                                <label for="birthday" class="col-sm-2 col-from-label">Fecha</label>                             
                                <div class="col-sm-6">
                                    <b-form-input  type="date" name="birthday" class="form-control" v-model.trim="form.birthday"></b-form-input>                                  
                                </div>                                                                        
                            </div>      
                            <div class="form-group row">
                                <label for="genre" class="col-sm-2 col-from-label">Comidad</label>        
                                <div class="col-sm-6">
                                    <b-form-select class="mb-3" v-model.trim="form.genre">
                                        <option >1</option>
                                        <option >2</option>
                                        <option >3</option>
                                        <option >4</option>
                                        <option >5</option>
                                        <option >6</option>
                                        <option >7</option>
                                    </b-form-select>                                      
                                </div>                                                                      
                            </div> 
                            <div class="form-group row">
                            <label for="genre" class="col-sm-2 col-from-label">Meta</label>
                            <b-form-checkbox id="checkbox-1" name="checkbox-1" value="accepted" unchecked-value="not_accepted" ></b-form-checkbox>
                           </div>
                            <div class="form-group row">
                                <label for="genre" class="col-sm-2 col-from-label">Limpieza personal</label>        
                                <div class="col-sm-6">
                                    <b-form-select class="mb-3" v-model.trim="form.genre">
                                        <option >1</option>
                                        <option >2</option>
                                        <option >3</option>
                                        <option >4</option>
                                        <option >5</option>
                                        <option >6</option>
                                        <option >7</option>
                                    </b-form-select>                                      
                                </div>                                                                      
                            </div> 
                            <div class="form-group row">
                                <label for="genre" class="col-sm-2 col-from-label">Bañarse/Ducharse</label>        
                                <div class="col-sm-6">
                                    <b-form-select class="mb-3" v-model.trim="form.genre">
                                        <option >1</option>
                                        <option >2</option>
                                        <option >3</option>
                                        <option >4</option>
                                        <option >5</option>
                                        <option >6</option>
                                        <option >7</option>
                                    </b-form-select>                                      
                                </div>                                                                      
                            </div> 
                            <div class="form-group row">
                                <label for="genre" class="col-sm-2 col-from-label">Vestirse/Desvestirse Superior</label>        
                                <div class="col-sm-6">
                                    <b-form-select class="mb-3" v-model.trim="form.genre">
                                        <option >1</option>
                                        <option >2</option>
                                        <option >3</option>
                                        <option >4</option>
                                        <option >5</option>
                                        <option >6</option>
                                        <option >7</option>
                                    </b-form-select>                                      
                                </div>                                                                      
                            </div> 
                            <div class="form-group row">
                                <label for="genre" class="col-sm-2 col-from-label">Vestirse/Desvestirse Inferior</label>        
                                <div class="col-sm-6">
                                    <b-form-select class="mb-3" v-model.trim="form.genre">
                                        <option >1</option>
                                        <option >2</option>
                                        <option >3</option>
                                        <option >4</option>
                                        <option >5</option>
                                        <option >6</option>
                                        <option >7</option>
                                    </b-form-select>                                      
                                </div>                                                                      
                            </div> 
                            <div class="form-group row">
                                <label for="genre" class="col-sm-2 col-from-label">Uso del Baño</label>        
                                <div class="col-sm-6">
                                    <b-form-select class="mb-3" v-model.trim="form.genre">
                                        <option >1</option>
                                        <option >2</option>
                                        <option >3</option>
                                        <option >4</option>
                                        <option >5</option>
                                        <option >6</option>
                                        <option >7</option>
                                    </b-form-select>                                      
                                </div>                                                                      
                            </div> 
                            <div class="form-group row">
                                <label for="genre" class="col-sm-2 col-from-label">Control de Heces</label>        
                                <div class="col-sm-6">
                                    <b-form-select class="mb-3" v-model.trim="form.genre">
                                        <option >1</option>
                                        <option >2</option>
                                        <option >3</option>
                                        <option >4</option>
                                        <option >5</option>
                                        <option >6</option>
                                        <option >7</option>
                                    </b-form-select>                                      
                                </div>                                                                      
                            </div> 
                            <div class="form-group row">
                                <label for="genre" class="col-sm-2 col-from-label">Control de Orina</label>        
                                <div class="col-sm-6">
                                    <b-form-select class="mb-3" v-model.trim="form.genre">
                                        <option >1</option>
                                        <option >2</option>
                                        <option >3</option>
                                        <option >4</option>
                                        <option >5</option>
                                        <option >6</option>
                                        <option >7</option>
                                    </b-form-select>                                      
                                </div>                                                                      
                            </div> 
                            <div class="form-group row">
                                <label for="genre" class="col-sm-2 col-from-label">Cama, Silla y Silla de Ruedas</label>        
                                <div class="col-sm-6">
                                    <b-form-select class="mb-3" v-model.trim="form.genre">
                                        <option >1</option>
                                        <option >2</option>
                                        <option >3</option>
                                        <option >4</option>
                                        <option >5</option>
                                        <option >6</option>
                                        <option >7</option>
                                    </b-form-select>                                      
                                </div>                                                                      
                            </div> 
                            <div class="form-group row">
                                <label for="genre" class="col-sm-2 col-from-label">Baño</label>        
                                <div class="col-sm-6">
                                    <b-form-select class="mb-3" v-model.trim="form.genre">
                                        <option >1</option>
                                        <option >2</option>
                                        <option >3</option>
                                        <option >4</option>
                                        <option >5</option>
                                        <option >6</option>
                                        <option >7</option>
                                    </b-form-select>                                      
                                </div>                                                                      
                            </div> 
                            <div class="form-group row">
                                <label for="genre" class="col-sm-2 col-from-label">Ducha</label>        
                                <div class="col-sm-6">
                                    <b-form-select class="mb-3" v-model.trim="form.genre">
                                        <option >1</option>
                                        <option >2</option>
                                        <option >3</option>
                                        <option >4</option>
                                        <option >5</option>
                                        <option >6</option>
                                        <option >7</option>
                                    </b-form-select>                                      
                                </div>                                                                      
                            </div> 
                            <div class="form-group row">
                                <label for="genre" class="col-sm-2 col-from-label">Marcha, Silla de Ruedas y Gateo</label>        
                                <div class="col-sm-6">
                                    <b-form-select class="mb-3" v-model.trim="form.genre">
                                        <option >1</option>
                                        <option >2</option>
                                        <option >3</option>
                                        <option >4</option>
                                        <option >5</option>
                                        <option >6</option>
                                        <option >7</option>
                                    </b-form-select>                                      
                                </div>                                                                      
                            </div> 
                            <div class="form-group row">
                                <label for="genre" class="col-sm-2 col-from-label">Gradas</label>        
                                <div class="col-sm-6">
                                    <b-form-select class="mb-3" v-model.trim="form.genre">
                                        <option >1</option>
                                        <option >2</option>
                                        <option >3</option>
                                        <option >4</option>
                                        <option >5</option>
                                        <option >6</option>
                                        <option >7</option>
                                    </b-form-select>                                      
                                </div>                                                                      
                            </div> 
                            <div class="form-group row">
                                <label for="genre" class="col-sm-2 col-from-label">Compresión</label>        
                                <div class="col-sm-6">
                                    <b-form-select class="mb-3" v-model.trim="form.genre">
                                        <option >1</option>
                                        <option >2</option>
                                        <option >3</option>
                                        <option >4</option>
                                        <option >5</option>
                                        <option >6</option>
                                        <option >7</option>
                                    </b-form-select>                                      
                                </div>                                                                      
                            </div> 
                            <div class="form-group row">
                                <label for="genre" class="col-sm-2 col-from-label">Expresión</label>        
                                <div class="col-sm-6">
                                    <b-form-select class="mb-3" v-model.trim="form.genre">
                                        <option >1</option>
                                        <option >2</option>
                                        <option >3</option>
                                        <option >4</option>
                                        <option >5</option>
                                        <option >6</option>
                                        <option >7</option>
                                    </b-form-select>                                      
                                </div>                                                                      
                            </div> 
                            <div class="form-group row">
                                <label for="genre" class="col-sm-2 col-from-label">Interacción Social</label>        
                                <div class="col-sm-6">
                                    <b-form-select class="mb-3" v-model.trim="form.genre">
                                        <option >1</option>
                                        <option >2</option>
                                        <option >3</option>
                                        <option >4</option>
                                        <option >5</option>
                                        <option >6</option>
                                        <option >7</option>
                                    </b-form-select>                                      
                                </div>                                                                      
                            </div> 
                            <div class="form-group row">
                                <label for="genre" class="col-sm-2 col-from-label">Resolver Problema</label>        
                                <div class="col-sm-6">
                                    <b-form-select class="mb-3" v-model.trim="form.genre">
                                        <option >1</option>
                                        <option >2</option>
                                        <option >3</option>
                                        <option >4</option>
                                        <option >5</option>
                                        <option >6</option>
                                        <option >7</option>
                                    </b-form-select>                                      
                                </div>                                                                      
                            </div> 
                            <div class="form-group row">
                                <label for="genre" class="col-sm-2 col-from-label">Memoria</label>        
                                <div class="col-sm-6">
                                    <b-form-select class="mb-3" v-model.trim="form.genre">
                                        <option >1</option>
                                        <option >2</option>
                                        <option >3</option>
                                        <option >4</option>
                                        <option >5</option>
                                        <option >6</option>
                                        <option >7</option>
                                    </b-form-select>                                      
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
            const path= `${process.env.BASE_URI}FIM/`
            axios.post(path, this.form).then((response)=>{


                swal("FIM creado exitosamente.", "", "success")
           })
            .catch((error)=>{
                swal("No se ha podido crear el FIM.", "", "error")
                console.log(error)
            })
        }
    }
}
</script>