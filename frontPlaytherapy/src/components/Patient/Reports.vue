<template>  
    <div>
        <Navigation />
        <main :style="{marginTop: '90px'}">              
            <mdb-container>
                <mdb-row class="mt-5 justify-content-start">
                    <h4 class="demo-title"><strong>Reportes</strong></h4>      
                </mdb-row>
                <hr />   
            <mdb-line-chart
                :data="lineChartData"
                :options="lineChartOptions"
                :width="600"
                :height="300"
            ></mdb-line-chart>
 
            </mdb-container>               
        </main>
    </div>      
</template>

<script>
    import axios from 'axios';
    import swal from 'sweetalert'
    import { 
        mdbBtn,
        mdbCol,
        mdbContainer, 
        mdbRow,
        mdbIcon, 
        mdbInput,
        mdbModal, 
        mdbModalHeader, 
        mdbModalTitle, 
        mdbModalBody, 
        mdbModalFooter, 
        mdbTbl, 
        mdbPieChart,
        mdbRadarChart,
        mdbTblHead, 
        mdbTblBody,
        mdbLineChart,
    } from "mdbvue";
    import Navigation from '@/components/Navigation/Navigation';

    export default {
        name: "InputsPage",
        name: "ChartPage",

        components: {
            mdbBtn,
            mdbCol,
            mdbPieChart,
            mdbContainer, 
            mdbRow,
            mdbIcon,
            mdbRadarChart,
            mdbContainer,
            mdbInput,
            mdbModal, 
            mdbModalHeader, 
            mdbModalTitle, 
            mdbModalBody, 
            mdbModalFooter,
            mdbTbl, 
            mdbTblHead, 
            mdbTblBody,
            mdbLineChart,
            Navigation
        },
    data() {
      return {
        lineChartData: {
          labels: [
            "Enero",
            "Febrero",
            "Marzo",
            "Abril",
            "Mayo",
            "Junio",
            "Julio"
          ],
          datasets: [
            {
              label: "My First dataset",
              backgroundColor: "rgba(255, 99, 132, 0.1)",
              borderColor: "rgba(255, 99, 132, 1)",
              borderWidth: 0.7,
              data: [65, 59, 80, 81, 56, 55, 40]
            }
          ]
        },
        lineChartOptions: {
          responsive: false,
          maintainAspectRatio: false,
          scales: {
            xAxes: [
              {
                gridLines: {
                  display: true,
                  color: "rgba(0, 0, 0, 0.1)"
                }
              }
            ],
            yAxes: [
              {
                gridLines: {
                  display: true,
                  color: "rgba(0, 0, 0, 0.1)"
                }
              }
            ]
          }
        }
      };
    }
    
  };
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